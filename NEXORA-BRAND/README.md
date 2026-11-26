# NEXORA Studio, identité de marque et design system

Outil de référence pour toute la communication et les futures créations de NEXORA Studio. Version 2.0 du 26 novembre 2026 : nom NEXORA Studio, logo NEXORA (Unbounded 700, E redessiné) et « Studio » manuscrit (Mr Dafoe), couleurs Braise inchangées.

| Dossier | Contenu |
|---|---|
| `01-BRAND-BOOK/` | `NEXORA-Studio-Brand-Book-v2.pdf` (25 pages, 16:9) et `NEXORA-Studio-Brand-Book-v2.md` (version éditable). Sources dans `sources-v2/`, v1 dans `archive-v1/` |
| `02-LOGO-BRAND-ASSETS/svg/` | 8 versions du logo (sur encre, sur os, sur braise, grand format, transparents, monochromes) et 4 du symbole N + S |
| `02-LOGO-BRAND-ASSETS/png/` | Les mêmes en PNG 2048 px |
| `02-LOGO-BRAND-ASSETS/favicon/` | `favicon.ico`, `favicon.svg`, PNG 16, 32, 48, 180 (Apple), 192 et 512 |
| `03-COLOR-PALETTE-TYPOGRAPHY/` | Planches PNG 1920 × 1080 : logo, construction, versions, symbole, palette, déclinaisons, contrastes, typographies, échelle, geste manuscrit |
| `04-DESIGN-SYSTEM/` | `NEXORA-Design-System.md` (v2.0) et planches des composants et des états (images de la v1 : la mise en page des composants n’a pas changé, seules les polices des titres diffèrent) |
| `05-DESIGN-TOKENS-SOURCE-FILES/` | `nexora-tokens.css`, `nexora-tokens.json`, `logo.tsx` (tracés du logo), `icons.tsx`, `site-globals.css`. Fichiers v1 dans `archive-v1/` |
| `08-CATALOGUE/` | `NEXORA-Studio-Catalogue-2026.pdf` et ses sources |
| `13-NEXORA-STUDIO/` | Logo de référence (SVG sombre, clair, braise, icône) et son générateur `sources/gen.py` |
| `06` et `07`, `09` à `12` | Explorations écartées (pistes de logo, rebranding Volta, Strobe, Rhythmos, Keraia, Next Studio). Gardées pour mémoire |

Polices : Unbounded (titres), Archivo (texte), Mr Dafoe (geste manuscrit), JetBrains Mono (données). Toutes gratuites sur Google Fonts, licence SIL Open Font.

Régénérer le brand book et les fichiers : dans `01-BRAND-BOOK/sources-v2/`, `python3 assets.py` puis `node raster.js` (logos et favicons), `python3 bb.py` puis `node pdf.js` (PDF), `node planches.js` (planches PNG).
