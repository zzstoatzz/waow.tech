const links = [...document.querySelectorAll('.possibilities a')];
const panel = document.querySelector('#preview');
const content = document.querySelector('#preview-content');
const name = document.querySelector('#preview-name');
const open = document.querySelector('#preview-open');
const position = document.querySelector('#preview-position');
const blocked = new Set(['bsky.app', 'wisp.place']);
let selected = 0;

function show(index) {
  selected = (index + links.length) % links.length;
  const link = links[selected];
  const url = new URL(link.href);
  panel.hidden = false;
  name.textContent = url.hostname;
  open.href = link.href;
  position.textContent = `${link.textContent} · ${selected + 1} / ${links.length}`;
  for (const item of links) item.removeAttribute('aria-current');
  link.setAttribute('aria-current', 'true');
  content.replaceChildren();
  if (blocked.has(url.hostname)) {
    const message = document.createElement('p');
    message.textContent = 'This site doesn’t allow embedded previews. Open it in a new tab to explore.';
    content.append(message);
  } else {
    const frame = document.createElement('iframe');
    frame.title = `${link.textContent} — ${url.hostname}`;
    frame.referrerPolicy = 'no-referrer';
    frame.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-forms allow-popups allow-popups-to-escape-sandbox');
    frame.src = link.href;
    content.append(frame);
  }
}

links.forEach((link, index) => {
  link.setAttribute('aria-controls', 'preview');
  link.addEventListener('click', (event) => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    show(index);
    if (matchMedia('(max-width: 700px)').matches) panel.scrollIntoView({block: 'start'});
    document.querySelector('#preview-close').focus({preventScroll: true});
  });
});
document.querySelector('#preview-previous').addEventListener('click', () => show(selected - 1));
document.querySelector('#preview-next').addEventListener('click', () => show(selected + 1));
function close() {
  panel.hidden = true;
  content.replaceChildren();
  for (const link of links) link.removeAttribute('aria-current');
  links[selected].focus();
}
document.querySelector('#preview-close').addEventListener('click', close);
panel.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') close();
});
