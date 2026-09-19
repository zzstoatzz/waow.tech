const examples = [
  {activity: 'photos', host: 'grain.social', url: 'https://grain.social/', alt: 'Grain’s public photo feed showing a mushroom photograph.'},
  {activity: 'code', host: 'tangled.org', url: 'https://tangled.org/zzstoatzz.io/waow.tech', alt: 'The waow.tech repository on Tangled, with files and recent commits.'},
  {activity: 'websites', host: 'wisp.place', url: 'https://wisp.place/', alt: 'Wisp’s website publishing page with its upload a folder control.'},
];
const panel = document.querySelector('#preview');
const image = document.querySelector('#preview-image');
const closeButton = document.querySelector('#preview-close');
let selected = 0;
let opener;

function show(index) {
  selected = (index + examples.length) % examples.length;
  const example = examples[selected];
  document.querySelector('#preview-name').textContent = example.host;
  document.querySelector('#preview-position').textContent = `${example.activity} · ${selected + 1} / ${examples.length}`;
  for (const id of ['#preview-open', '#preview-image-link']) document.querySelector(id).href = example.url;
  image.alt = example.alt;
  image.src = `/assets/previews/${example.activity}.jpg`;
  panel.hidden = false;
}

for (const link of document.querySelectorAll('.possibilities a')) {
  const index = examples.findIndex(example => example.host === new URL(link.href).hostname);
  if (index < 0) continue;
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'preview-trigger';
  button.textContent = 'preview';
  button.setAttribute('aria-label', `preview ${examples[index].activity}`);
  button.setAttribute('aria-controls', 'preview');
  button.addEventListener('click', () => {
    opener = button;
    show(index);
    if (matchMedia('(max-width: 700px)').matches) panel.scrollIntoView({block: 'start'});
    closeButton.focus({preventScroll: true});
  });
  link.after(button);
}
function close() {
  panel.hidden = true;
  image.removeAttribute('src');
  opener?.focus();
}
closeButton.addEventListener('click', close);
document.querySelector('#preview-previous').addEventListener('click', () => show(selected - 1));
document.querySelector('#preview-next').addEventListener('click', () => show(selected + 1));
panel.addEventListener('keydown', event => {
  if (event.key === 'Escape') close();
});
