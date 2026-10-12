"""Render square-peg/index.html from the tech.waow.squarepeg.figure records on the PDS.

    python3 scripts/build_square_peg.py

The page is static HTML: record text is baked in here, images load from the PDS
blob endpoint. Re-run after figures are added, edited, or retracted.
"""
from html import escape
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import json

DID = 'did:plc:siv7zbedip4vcet4v67piibr'
PDS = 'https://pds.zat.dev'
COLLECTION = 'tech.waow.squarepeg.figure'
root = Path(__file__).resolve().parents[1]


def xrpc(method, **params):
    with urlopen(f'{PDS}/xrpc/{method}?{urlencode(params)}', timeout=30) as res:
        return json.load(res)


def figure(record):
    value = record['value']
    rkey = record['uri'].rsplit('/', 1)[1]
    blob = f"{PDS}/xrpc/com.atproto.sync.getBlob?{urlencode({'did': DID, 'cid': value['image']['ref']['$link']})}"
    ratio = value.get('aspectRatio', {})
    size = f' width="{ratio["width"]}" height="{ratio["height"]}"' if ratio else ''
    status = escape(value['status'])
    label = f'{status}, partly retracted' if 'retraction' in value and status != 'retracted' else status
    flagged = ' figure-status-retracted' if 'retraction' in value or status == 'retracted' else ''
    caption = ''.join(f'<p>{escape(p)}</p>' for p in value['caption'].split('\n\n'))
    retraction = f'<p class="figure-retraction"><strong>retracted:</strong> {escape(value["retraction"])}</p>' if 'retraction' in value else ''
    source = f"{PDS}/xrpc/com.atproto.repo.getRecord?{urlencode({'repo': DID, 'collection': COLLECTION, 'rkey': rkey})}"
    return (
        f'<li class="figure" id="{escape(rkey)}"><p class="figure-status{flagged}">{label}</p>'
        f'<h2 class="figure-title">{escape(value["title"])}</h2>'
        f'<a class="figure-image" href="{escape(blob)}"><img src="{escape(blob)}"{size} loading="lazy" alt="{escape(value["alt"])}"></a>'
        f'{caption}{retraction}'
        f'<p class="figure-meta">{escape(value["createdAt"][:10])} · <a href="{escape(source)}">record</a></p></li>'
    )


records = xrpc('com.atproto.repo.listRecords', repo=DID, collection=COLLECTION, limit=100)['records']
records.sort(key=lambda r: (r['value']['createdAt'][:10], r['uri']))
description = 'pictures from work on the inscribed square problem, each labelled with how much it establishes.'
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>square peg pictures — waow.tech</title><meta name="description" content="{description}">
<meta property="og:title" content="square peg pictures — waow.tech"><meta property="og:description" content="{description}"><meta property="og:url" content="https://waow.tech/square-peg/"><meta property="og:type" content="website"><meta property="og:image" content="https://waow.tech/assets/avatar.jpg"><meta name="twitter:card" content="summary"><link rel="canonical" href="https://waow.tech/square-peg/"><link rel="icon" href="/assets/avatar.jpg"><link rel="stylesheet" href="/style.css"></head>
<body><a class="skip-link" href="#main">skip to content</a><div class="shell"><header class="site-header"><a class="identity" href="/" aria-label="waow.tech home"><img src="/assets/avatar.jpg" width="48" height="48" alt=""><span>waow</span></a></header><main id="main" tabindex="-1"><h1>square peg pictures.</h1><p class="figures-lede">does every closed loop in the plane pass through the four corners of some square? nobody knows. these are pictures from working on it. each one says how much it establishes: proved, sketched, numerical, or retracted. so far every one is numerical, which means computed on polygons or sampled curves, not proved.</p><ol class="figures">
{chr(10).join(figure(r) for r in records)}
</ol></main><footer class="site-footer"><span>{len(records)} records in <code>{COLLECTION}</code>, read from the PDS</span></footer></div></body></html>
'''
out = root / 'square-peg'
out.mkdir(exist_ok=True)
(out / 'index.html').write_text(page)
print(f'Wrote {out / "index.html"} from {len(records)} records')
