# waow.tech

A small, static directory of experiments on AT Protocol. The project index is at
`/go`; the original manifesto stays at `/`. `/about/` redirects to `/`. No JavaScript, dependencies, external
fonts, or requests to Blento are needed to render the page.

## Edit and preview

The entrance shows a compact grid with real favicons and names always visible.
The headline is “things to do with our data”: emphasize possibilities and agency,
not abstract ownership slogans. The room CTA links to the existing after hours
experience. See [the room handoff](docs/after-hours-handoff.md).

The homepage and directory share a linked identity and explicit navigation. The
homepage explains the idea; `/go/` is the only project inventory. The directory
uses plain links, source favicons, and restrained hover/focus feedback,
with no JavaScript or graphics runtime. Infrastructure links are compact visible
rows, and after hours uses its own declared favicon.

Edit project links and descriptions directly in `go/index.html`; styling lives in
`style.css`. The account avatar is stored locally in `assets/avatar.jpg`. Project icons are
unaltered snapshots of each live homepage’s declared favicon, stored in
`assets/icons/`. Refresh them with `python3 scripts/refresh-icons.py`; source URLs
are recorded in `scripts/icon-sources.json`. Brand uses its selected bracketed-b favicon. Never substitute invented symbols for project branding.

```sh
python3 scripts/build.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

The build script stages an explicit allowlist of public assets. Publish `dist/`,
not the repository root. Existing embeds remain at their original paths. The
root `404.html` also prevents Cloudflare Pages from treating the site as an SPA.

Existing hosting: Cloudflare Pages, project `waow-tech`. Keep it for the initial
refresh; the same static output can move to Wisp without rewriting the page.
The approved directory is published alongside the manifesto using this existing Pages project.

## Local checkout

Moved from `~/tangled.org/zzstoatzz.io/waow.tech` to
`~/tangled.org/waow.tech/apex` on 2026-09-19. Git history and existing origin and
GitHub mirror URLs are unchanged: this is a local organization change, not a
remote repository transfer.

## Bio link

Profile link: `https://waow.tech/go`

The short `/go` path keeps the manifesto at the root. The inspected local Bluesky client
constructs rich text from profile description text and detects links itself
(`src/view/screens/Profile.tsx`, `useRichText`). A custom display-label trick
would therefore depend on client behavior; it cannot be guaranteed across forks.

## Content audit, 2026-09-19

Read public `app.blento.card` and `app.blento.section` records directly from
`https://pds.zat.dev` for `did:plc:siv7zbedip4vcet4v67piibr` (waow.tech).
The 13 cards were last updated 2026-05-11. All their destinations are retained:
the old apex card becomes the manifesto link; ken, sonify, and the two Grafana
links sit in the compact “behind the apps” section. The newer additions are doodl, chimes,
pensieve, MCP Atlas, brand, and the race to 38. Descriptions were checked against
the local project READMEs. No Blento records were modified.

Automated HTTP checks returned 200 for ken, bsky38, relay, zlay, jetstream, and
stream. Other project homepages returned 403 to the automated client; those
responses do not establish whether the applications work in a normal browser.
Full destination functionality remains unverified.

Wisp supports static files and custom domains: <https://docs.wisp.place/>.
Hosting migration is a separate choice from this content/layout refresh.


## published 2026-09-19

Cloudflare Pages deployment `87b8b2f4` serves the manifesto at `/` and directory
at `/go`. `/about/` redirects to `/`. Verified both public pages and the redirect.
The waow.tech `app.bsky.actor.profile/self` description now contains
`https://waow.tech/go`; the avatar and other record fields were preserved using
an optimistic CID check. No Blento records or DNS settings changed.
