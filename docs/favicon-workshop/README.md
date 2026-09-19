# typeahead and brand favicon studies

Workshop, 2026-09-19. Nate selected typeahead A and brand C; both are now published. Other candidates remain studies.
Open `index.html` through the local preview server. Selecting a study changes the
simulated tab and directory entry; production favicons are unaffected.

## references

Inspected the live typeahead homepage and `/stats`, plus `src/pages/theme.ts`,
`src/pages/home.ts`, `src/pages/stats.ts` and their relevant history. The identity
is monospace text with a teal rectangular cursor after the wordmark. Chart colors
are teal `#44aa99`, blue `#58a6ff`, violet `#bc8cff`; dark panel is `#101211`.

Inspected brand's live homepage, README, and `src/worker.ts`. Its identity is
monochrome monospace, black `#101012`, white `#eee`, gray `#999`, with namespace
resolution expressed as `f(namespace) → brand assets`.

## critique

- Typeahead A reduces the existing wordmark to a lowercase t and block cursor.
  It is the strongest continuation of the live identity. The cursor is static.
- Typeahead B uses two initials. It retains more of the name but is denser.
- Typeahead C borrows chart colors for result rows. It is less specific to the name.
- Brand A removes the tag metaphor and makes one bold lowercase letter legible.
- Brand B explores resolution between endpoints; distinctive but abstract.
- Brand C places the letter in namespace-like brackets; more contextual, less
  readable at 16 px.

All glyphs are SVG paths, with no runtime font dependency. The review includes
current marks, 16/24/32 px samples, 64 px inspection, dark/light backgrounds,
and tab/directory contexts. Selection is for comparison only.

Next: refine the chosen direction, replace the source project's shared favicon,
run its build/deployment gates, verify the live asset, then refresh apex icons.

Selected assets: typeahead `994993b`, brand `c5b2427`. Both builds and tests passed; typeahead’s deployment smoke gate passed (credentialed admin checks and optional comparison skipped). README review: no API or behavior documentation changes required in either source project.
