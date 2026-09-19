"""Stage only public site files, never the repository or local credentials."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
dest = root / 'dist'
if dest.exists():
    shutil.rmtree(dest)
dest.mkdir()
for name in ('index.html', 'style.css', '404.html', '_redirects'):
    shutil.copy2(root / name, dest / name)
for name in ('go', 'assets', 'embeds'):
    shutil.copytree(root / name, dest / name, dirs_exist_ok=True)
print(f'Staged public files in {dest}')
