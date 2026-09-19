# favicon rollout — 2026-09-19

Nate authorized replacing these project favicons and deploying each project.
The marks preserve existing palettes, use distinct silhouettes, and were checked
at 16/24/32/64 pixels against light and dark backgrounds.

| project | mark | source commit | deployed target |
| --- | --- | --- | --- |
| chimes | suspended tubes and wind catcher; garden greens | `9250e81` | Wisp `zzstoatzz.io/chimes`, chimes.waow.tech |
| MCP atlas | folded map, route and waypoint; existing blue/gold | `cdd4c4e` | Worker `mcp-atlas`, version `240253d3-05d7-416b-8317-77bbc868a8a8` |
| typeahead | typed lines and insertion cursor; existing teal | `b51f040` | Worker `typeahead`, version `2c3b38a2-6132-44ea-97a7-3547f9fceeef` |
| pensieve | memory basin and drop; existing amber | `b57d5c3` | Worker `pensieve`, version `17f4d4eb-c142-4a47-9759-8b917c91e555` |
| pollz | checked ballot instead of a bar chart; teal | `ae45810` | Pages `pollz-waow-tech`, deployment `7ccb9a9f` |
| brand | lowercase b on an identity tag; monochrome | `b821b87` | Worker `brand`, version `6ada46a4-fe79-456c-bcfd-6d8294bf480b` |

MCP atlas, typeahead, pensieve and pollz commits were pushed to their existing
main branches. Chimes and brand have no configured remotes; their commits are
local and the services were deployed directly.

MCP atlas had extensive unrelated local changes. The content-only Cloudflare
API replaced exactly two favicon tags in the current deployed module, preserving
configuration and all other script bytes. Its prior deployed version was
`93555e6d-04ab-4448-8b18-a004e29b33fc`. The commit contains only the favicon
replacement; all unrelated working changes remain intact.

Checks: chimes audio suite and build; brand typecheck, bundle and 29 tests;
pensieve 45 tests, lint, all 11 JS files parsed, bundle, live health and expected
401 while signed out; typeahead typecheck, lint, 88 tests, bundle and live smoke
suite (admin credential-dependent checks and optional comparison skipped);
pollz production Vite build (existing tooltip accessibility warning). MCP search
and brand resolver returned 200. All six live favicon contents matched the
reviewed SVGs byte-for-byte after trimming terminal whitespace.

The initial pollz pnpm command generated an invalid build-policy stub and stopped
on an ignored esbuild install script. The installed project Vite binary built
successfully without changing build policy. The generated stub was removed.

Apex icons were fetched again from the live projects, including brand. The apex
site itself remains a local draft. Pub search and other icons were not redesigned.
README review for typeahead: only the favicon literal changed; architecture,
API behavior, deployment procedures and documented operational guarantees did
not change, so no README edit was necessary.

Tangled CI: typeahead and pollz passed on the pushed commits. MCP atlas
workflows remained queued at the final check; deployment was verified directly.

## refinement — 2026-09-19

Following feedback on legibility and generic symbolism, chimes now uses a
suspended bamboo set, pollz shows choices and their results, and atlas uses a
coordinate globe with server locations. Checked at 16/24/32/64 px on light and
dark surfaces. The remaining three icons are unchanged.

- chimes: `1561562`; Wisp deployment also rebuilds the instrument, maps taps to
  rotated tube geometry, removes flashes/weather labels, and adds pause.
  Typecheck, build, audio safety/pitch checks passed; desktop/mobile and both
  themes inspected, production listen/pause exercised.
- pollz: `001a5c8`; Pages deployment `67d7964c`.
- mcp atlas: `e05b0b4`; Worker version `3d520a5f-bb16-4b58-b7a0-18863ab36ca1`.
  Applied only the two favicon tags to the current live source via the content
  API. Unrelated local changes and deployment configuration preserved.
