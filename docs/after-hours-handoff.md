# after hours as a playable introduction

## current entry points — 2026-09-19

`waow.tech/` remains the manifesto. The compact project directory is at `/go`,
which is the account's bio destination. After hours remains an explicit link
from the directory, with direct app links as an accessible, lightweight fallback.
The room is not ready to replace either page.

Local directory: `/Users/nate/tangled.org/waow.tech/apex`
Local room: `/Users/nate/tangled.org/zzstoatzz.io/after-hours`
Live room: `https://afterhours.waow.tech/`

This handoff records future room work; it does not claim those integrations
have been implemented or create another task.

## chimes: carry the instrument into the room

The standalone app now draws rigid, hollow tubes with material-specific finishes,
suspension cords, a wooden cap, clapper, and wind catcher. Tubes pivot at their
suspension points. A touch targets the visible rotated tube and applies motion
immediately, without a flash or delayed visual response.

Inspect `chimes/src/scene.ts`, `src/main.ts`, `src/audio.ts`, and
`public/chime-processor.js` in the sibling checkout. Start from commit `1561562`
for the rebuilt instrument, then include `30c535b` for the activity indicator and stream measurement.
The worklet's bounded voice pool, pitch calibration, and limiter are important;
preserve its audio safety tests when reusing or porting the sound.

The room already has `scripts/make_chimes.py` and a chimes touch target. Audit
those before adding another implementation. Carry the physical construction
into the Blender/Godot scene; match its lighting and materials rather than
embedding a decorative screenshot. Preserve the relationship between a touched
tube, its motion, and its note.

Standalone listening samples live atproto posts. The activity breadcrumb shows
received event and post rates, the connected source, and relay-eval's hourly
baseline with a link to Stream's stats. Preserve that distinction in the room:
a note is a sample, not one sound per network event. Provide discoverable stream
details without turning the room into a dashboard. No automatic audio before
interaction; avoid competing streams or audio players when changing surfaces.

Connect real tuning and saved sets, including PDS read/write behavior. Shared
identity does not imply that the apps already share an authorized session.

## other requested integrations

- Preserve coral's existing selection and return-to-room focus behavior.
- Add doodl through a usable drawing surface, with real save/share behavior.
- Add the race to 38 as another TV channel; stop inactive work.

`web/src/main.ts`, `web/src/room-focus.ts`, and `web/src/contracts.ts` own the web
surfaces and bridge. `blender/build_apartment.py` constructs the apartment;
Godot owns room interaction and audio. Verify current source and working diffs
before relying on historical handoffs.

## presentation and acceptance

Use source-project artwork and favicons, lowercase editorial copy, idiomatic
acronyms, and a consistently sized `waow.tech`. Explain atproto rather than
centering one microblogging app. Prefer useful actions and “things to do with
our data” over abstract ownership slogans.

Read the room's `docs/performance.md`. Measure cold/warm startup, usable controls,
walking stalls, activation, and return-to-room on desktop and phone. Include
Safari and Firefox/Zen. Load expensive surfaces only when activated; preserve
intentional background music separately from inactive rendering/network work.

Verify keyboard/touch, focus transitions, mute, visibility, failed network loads,
and signed-out visits. For each writable integration, demonstrate a real
create/save/retrieve path and identify the PDS holding it. Keep the plain
directory available when WebGL fails or visitors prefer direct links.
