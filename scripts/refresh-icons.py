"""Snapshot each project's declared favicon without changing its artwork."""
import base64
import json
from html.parser import HTMLParser
from pathlib import Path
import subprocess
from urllib.parse import unquote_to_bytes, urljoin

ROOT = Path(__file__).resolve().parents[1]
HOSTS = ('doodl', 'chimes', 'pollz', 'slides', 'pub-search', 'pensieve',
         'coral', 'typeahead', 'bsky38', 'mcp', 'brand')

class Icons(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and 'icon' in attrs.get('rel', '').split():
            if attrs.get('href'):
                self.hrefs.append(attrs['href'])

def fetch(url):
    return subprocess.run(['curl', '--fail', '--silent', '--show-error',
                           '--location', '--max-time', '20', url],
                          check=True, capture_output=True).stdout

sources = {}
for host in HOSTS:
    page = f'https://{host}.waow.tech/'
    parser = Icons()
    parser.feed(fetch(page).decode())
    if not parser.hrefs:
        sources[host] = {'page': page, 'icon': None,
                         'note': 'No favicon declared; render without an icon.'}
        continue
    href = parser.hrefs[0]
    if href.startswith('data:'):
        metadata, payload = href.split(',', 1)
        data = base64.b64decode(payload) if ';base64' in metadata else unquote_to_bytes(payload)
        source = href
    else:
        source = urljoin(page, href)
        data = fetch(source)
    if b'<svg' in data[:1024]:
        extension = 'svg'
    elif data.startswith(b'\x89PNG\r\n\x1a\n'):
        extension = 'png'
    elif data.startswith(b'\x00\x00\x01\x00'):
        extension = 'ico'
    else:
        raise ValueError(f'Unrecognized favicon content for {host}')
    name = f'assets/icons/{host}.{extension}'
    (ROOT / name).write_bytes(data)
    sources[host] = {'page': page, 'icon': source, 'file': name}
(ROOT / 'scripts/icon-sources.json').write_text(json.dumps(sources, indent=2) + '\n')
print(f'Saved {sum(bool(s.get("file")) for s in sources.values())} declared favicons.')
