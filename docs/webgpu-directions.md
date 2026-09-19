# playable waow.tech experiments

Research, 2026-09-19. These are proposals, not an implementation or a decision to
replace the manifesto or directory.

## CRT reference

Explored https://crt.vibe-coded.com/ with actual keyboard input and inspected its
public `crt-bundle.js`. Also inspected https://vibe-coded.com/ and its control
legend. The rendering bundle instantiates Three.js WebGPURenderer. That renderer
can fall back to WebGL2; its presence does not prove which backend ran locally.
Reference: https://threejs.org/docs/pages/WebGPURenderer.html

Verified on-screen menu navigation with Tab and arrows, shader switching, and
literal `asdf` entry in Terminal mode. The source clarifies the mappings:

- Tab toggles the on-screen menu.
- Menu: up/down or W/S chooses rows; left/right or A/D changes choices and values.
  In its input grid, arrows move the selection. Enter activates buttons/text edits.
- Julia/Mandelbrot: WASD pans, Q/E zooms, R resets, P cycles palettes.
- Julia specifically: arrows change the complex parameter; Shift makes larger steps.
- Map: WASD pans, Q/E zooms, arrows control pitch/bearing, R resets, M changes style.
  Source-inspected only; no map token was supplied and no map service was configured.
- Ordinary letters type in Terminal mode. F has no universal standalone binding.
- The physical keyboard mirrors keydown/up via mesh displacement. Pointer raycasts
  identify clickable keys and dispatch the same key handling. Key sounds use
  sampled solenoid recordings. Audio quality was not independently evaluated.

The strength is coherence: curved geometry, phosphor persistence, beam behavior,
bloom, screen-derived keyboard lighting, and moving keys describe one object.
The parent site's text can become difficult to read through the effects; retain
an ordinary HTML route to every meaningful action. No performance benchmark or
mobile GPU compatibility claim was established in this exploration.

## directions

1. **atmosphere receiver** — a physical tuning instrument. Channels reveal public
   record types or existing apps. A/S/D/F trigger distinct visual/audio responses;
   arrows tune parameters; pointer/touch controls are visibly labeled equivalents.
   A sampled post can leave a phosphor trace; selecting it reveals its actual
   source. Show sampling and source details as in chimes. Build this as one
   standalone object, then place it on the desk or TV in after hours.
2. **doodl ink instrument** — keys release pigments; dragging bends their flow.
   GPU feedback/advection makes the interaction interesting. Freeze a frame into
   a real doodl drawing through the app's existing save flow, with explicit sign-in
   when required. The output must be useful beyond the shader.
3. **record loom** — sampled collection activity weaves threads into a moving
   textile. Controls set weave/tension rather than randomly changing effects.
   Follow a thread to inspect the record it represents. Bound input and geometry,
   explain sampling, and keep public record inspection available outside the canvas.

Recommended first experiment: the receiver. It can connect coral, chimes, and the
race to 38 to a tangible control scheme without rebuilding the whole apartment.
Keep `/` as manifesto and `/go` as direct links. Lazy-load the experiment after
explicit entry, cap pixel ratio and working buffers, and measure phone startup,
frame time, and sustained heat before calling it fast. GPU compute needs its own
fallback design; a renderer's WebGL fallback is not a blanket compute fallback.
