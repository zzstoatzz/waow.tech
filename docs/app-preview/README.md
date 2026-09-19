# on-demand app preview

Prototype: https://app-preview.waow-tech-evb.pages.dev/
Local: /docs/app-preview/ (serve repository root). Not in the production build.

One selected iframe, created on click and removed on close or replacement.
No frames or external app requests on initial load. Direct links work without
JavaScript and modified clicks still open the original destination. The
external-open control remains available. On narrow screens the preview stacks.

2026-09-19 checks: bsky.app sends X-Frame-Options SAMEORIGIN; wisp.place
sends DENY and frame-ancestors none. These receive an explicit external-open
message. GET checks found no equivalent header on the other seven destinations.
This is not proof that those apps function when framed.

In-app browser testing kept leaflet, grain, and plyr frames on about:blank,
with and without sandbox, both localhost and the secure preview deployment.
No browser error was surfaced. Cause unresolved. Do not promote this prototype
until actual rendering, mobile interaction and third-party load costs are verified.

The deployed prototype uses the sandbox. No runtime or preview CSS is shipped
on the production homepage. The iframe idea remains separate from any future
JEV organization of activities and applications.
