"""Pull status counts from each client's public Notion pipeline.
Usage: python3 ops/daily-updates/pull_pipelines.py
"""
import json,sys,urllib.request,collections
def post(host,ep,body):
    r=urllib.request.Request(f"https://{host}/api/v3/{ep}",json.dumps(body).encode(),{'content-type':'application/json','user-agent':'curl/8.5.0'})
    return json.load(urllib.request.urlopen(r,timeout=30))
def v(x):
    x=x.get('value',x); return x.get('value',x)
def txt(p): return ''.join(s[0] for s in p) if p else ''
PIPELINES = [
    ("Atolea", "atolea-jewelry.notion.site", "2f4cdc5947bc804b822fc9fb18ce88ea"),
    ("Madam Muse", "pear-custard-2df.notion.site", "3a50be0b949f80238d38d1e645494e12"),
    ("LuxFord Tech", "cheddar-entrance-4f2.notion.site", "3d64214161de80c5a7bcedea3b8f449f"),
    ("Longwell & Co", "standing-tungsten-e93.notion.site", "3d531bb3a6708004afe5c5bde1844cc8"),
    ("Napper", "napper.notion.site", "3e4de684f7f180d6a42ec0960f82dbd5"),
]
for name,host,pid in PIPELINES:
    u=f"{pid[:8]}-{pid[8:12]}-{pid[12:16]}-{pid[16:20]}-{pid[20:]}"
    try:
        d=post(host,'loadPageChunk',{"pageId":u,"limit":30,"cursor":{"stack":[]},"chunkNumber":0,"verticalColumns":False})
        blocks={k:v(b) for k,b in d['recordMap']['block'].items()}
        pg=blocks[u]
        if pg['type'].startswith('collection_view'):
            cid=pg['collection_id']; vid=pg['view_ids'][0]; sp=pg['space_id']
        else:
            cv=[b for b in blocks.values() if b.get('type','').startswith('collection_view') and b.get('collection_id')][0]
            cid=cv['collection_id']; vid=cv['view_ids'][0]; sp=cv['space_id']
        q=post(host,'queryCollection',{"source":{"type":"collection","id":cid,"spaceId":sp},"collectionView":{"id":vid,"spaceId":sp},"loader":{"type":"reducer","reducers":{"r":{"type":"results","limit":500}},"searchQuery":"","userTimeZone":"America/New_York"}})
        rm=q['recordMap']; sch=v(list(rm['collection'].values())[0])['schema']
        sk=[k for k,s in sch.items() if s['type']=='status' or s['name'].lower()=='status'][0]
        ids=q['result']['reducerResults']['r']['blockIds']
        c=collections.Counter(); rfl=[]
        for i in ids:
            b=v(rm['block'][i]); p=b.get('properties',{}); st=txt(p.get(sk)) or '(none)'
            c[st]+=1
            if 'ready' in st.lower() and 'launch' in st.lower(): rfl.append(txt(p.get('title'))[:40])
        print(f"== {name}: {len(ids)} rows | "+', '.join(f'{k} {n}' for k,n in c.most_common()))
        if rfl: print('   Ready for launch:', '; '.join(rfl))
    except Exception as e: print(f"== {name}: ERROR {e}")
