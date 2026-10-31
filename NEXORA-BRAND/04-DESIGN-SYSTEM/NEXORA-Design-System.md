# NEXORA, Design System v1.0

Documentation des composants, des états, du responsive et du mouvement, telle qu’implémentée sur le site NEXORA (Next.js et Tailwind CSS v4). Les valeurs sont **observées** dans le code, sauf mention **[Recommandé]**.

Fichiers associés :

- `05-DESIGN-TOKENS-SOURCE-FILES/nexora-tokens.css` : variables CSS et thèmes ;
- `05-DESIGN-TOKENS-SOURCE-FILES/nexora-tokens.json` : tokens au format machine, avec les contrastes calculés ;
- `05-DESIGN-TOKENS-SOURCE-FILES/logo.tsx` et `icons.tsx` : composants React du logo et des icônes ;
- `05-DESIGN-TOKENS-SOURCE-FILES/site-globals.css` : feuille de style du site, source de vérité.

---

## 1. Principes

1. **Un seul moment fort par écran.** Le reste est calme et discipliné.
2. **La braise est rare.** Action principale, X du logo, bloc contact. Jamais en décor.
3. **Pas d’ombre au repos, pas de verre, pas de dégradé décoratif.** La profondeur vient des pas de ton.
4. **Le mouvement répond au scroll ou à la main.** Il ne détourne jamais le défilement et se met en pause hors écran.
5. **Accessible par défaut.** Contraste AA, focus visible, cibles de 44 px, réduction des animations.

---

## 2. Tokens

### Couleurs de rôle (par thème)

| Rôle | Nuit (défaut) | Os | Braise |
|---|---|---|---|
| `--nx-bg` | encre #0D0C0B | os #ECE5D8 | braise #FF4A1C |
| `--nx-fg` | os #ECE5D8 | encre #0D0C0B | encre #0D0C0B |
| `--nx-surface` | charbon #161412 | sable #E2DACB | – |
| `--nx-muted` | pierre #9A9386 | terre #4F493F | braise nuit #3A1206 |
| `--nx-accent` | braise #FF4A1C | braise profonde #B02F0B | encre #0D0C0B |
| `--nx-on-accent` | encre | os | braise |
| `--nx-line` | os 14 % | encre 16 % | encre 28 % |
| `--nx-focus` | braise | encre | encre |
| `--nx-logo-x` | braise | braise profonde | encre |

Application : la classe `.nx-theme-os` ou `.nx-theme-braise` sur une section redéfinit les rôles pour tout son contenu. Sur le site, ces classes s’appellent `theme-paper` et `theme-signal`.

### Espacements

Base 4 px : 4, 8, 12, 16, 24, 32, 48, 64, 96, 112, 144 px.

- Marges de page : 16 px (mobile), 32 px (desktop).
- Écart entre sections : 112 px (mobile), 144 px (desktop).
- Gouttière de grille : 16 à 32 px.

### Rayons

| Token | Valeur | Usage |
|---|---|---|
| `--nx-radius-pill` | 9999 px | Boutons, puces, filtres, pastilles images |
| `--nx-radius-tile` | 28 px | Tuiles d’expertise, cartes |
| `--nx-radius-inner` | 16 px | Visuel à l’intérieur d’une tuile |
| `--nx-radius-focus` | 2 px | Contour de focus |
| – | 0 | Photographies et images de projets (angles vifs) |

### Typographie

Voir la section 4 du brand book. Utilitaires du site : `t-section`, `t-card`, `t-lead`, `font-wide`.

---

## 3. Composants

### Bouton principal

- **Forme** : pilule pleine, `min-height: 48px`, padding horizontal de 24 px, texte Archivo 15 px graisse 600.
- **Couleurs** : fond `--nx-accent`, texte `--nx-on-accent`. Sur fond braise : fond encre, texte braise.
- **Icône** : flèche diagonale de 14 à 16 px, trait 1,5.
- **États** :
  - survol : `scale(1.03)` en 500 ms, la flèche glisse de 2 px vers le haut et la droite ;
  - focus : contour 2 px `--nx-focus`, décalé de 3 px ;
  - chargement : libellé « Envoi… », opacité 60 %, curseur d’attente ;
  - désactivé : opacité 60 %.
- **Libellés** : un verbe qui dit ce qui se passe (« Démarrer un projet », « Préparer l’e-mail », « Parler de votre projet »).

### Bouton grand avec pastille

- 56 px de haut, padding gauche de 28 px.
- Pastille ronde de 40 px à droite, couleurs inversées, avec la flèche.
- Survol : la pastille tourne de 45°.
- Usage : appels à l’action de fin de section (« Voir toutes les réalisations »).

### Lien texte

- Soulignement de 1 px qui se dessine de gauche à droite au survol (0,6 s, ease-in-out quint).
- Cible minimale de 44 px de haut.

### Navigation (desktop)

- **Disposition** : monogramme NX (3 colonnes), quatre liens calés sur une grille de 4 colonnes égales (6 colonnes), bouton principal (3 colonnes). Liens Archivo 15 px graisse 500.
- **Survol** : le libellé « roule » vers le haut et laisse place à son double (500 ms).
- **Section active** : point braise de 6 px devant le libellé, et `aria-current`.
- **Barre** :
  - transparente en haut de page, fond plein une fois le défilement commencé ;
  - masquée quand on descend, rendue quand on remonte ;
  - prend le thème de la section qu’elle survole (attribut `data-header`).
- **Bouton** : apparaît seulement après le hero, pour ne pas doubler celui du hero.

### Navigation (mobile)

- Monogramme, pastille « Contact » (après le hero), bouton « Menu » de 44 × 44 px.
- **Menu** : plein écran en thème braise, liens Archivo largeur 125 à 10,5vw, heure de Cotonou, e-mail.
- **Accessibilité** :
  - le focus va sur « Fermer » à l’ouverture et reste piégé dans le menu ;
  - Échap ferme le menu, et le focus revient au bouton « Menu ».

### Tuile (expertise)

- **Base** : fond `--nx-surface`, rayon 28 px, padding de 24 à 36 px.
- **Halo** : dégradé radial braise à 9 %, de 520 px, qui suit le pointeur (variables `--mx`, `--my`).
- **Filet** : bordure lumineuse de 1 px, braise près du pointeur.
- **Contenu** :
  - visuel animé (rayon 16 px) ;
  - mot-titre Archivo largeur 112, terminé par un point braise ;
  - sous-titre en serif italique, phrase de 17 px, puces.
- **Apparition** : la tuile monte de 140 px, se redresse de 16° (`rotateX`) et passe de 90 à 100 % d’échelle selon sa progression dans l’écran.

### Puce

Contour 1 px `--nx-line`, pilule, padding de 6 × 14 px, 14 px.

### Filtre (page Réalisations)

- Puce cliquable de 44 px de haut, avec un compteur de 13 px.
- Actif : plein `--nx-accent`, `aria-pressed="true"`.
- Changement de filtre animé avec la View Transitions API (si le navigateur la propose).

### Champ de formulaire

- Libellé 14 px graisse 500 au-dessus du champ.
- Champ souligné de 1 px, 17 px, fond transparent ; au focus, le soulignement prend la couleur du texte.
- **Erreur** : texte 14 px gras en `--nx-danger`, relié par `aria-describedby`, `aria-invalid="true"`, focus déplacé sur le premier champ en erreur.
- **Anti-spam** : champ caché (honeypot).
- **Envoi** :
  - avec `NEXT_PUBLIC_FORM_ENDPOINT` : requête POST en JSON, états envoi, réussite et erreur ;
  - sans cette variable : préparation d’un e-mail dans la messagerie du visiteur.

### Accordéon (FAQ)

- Élément natif `details` / `summary`, ligne de 64 px minimum, question 20 à 24 px graisse 600.
- Bouton rond de 40 px avec un plus, qui tourne de 45° et passe en braise à l’ouverture.
- Hauteur animée (`interpolate-size`) quand le navigateur le permet.

### Carte de réalisation

- Image à angles vifs, aperçu flou (`blurDataURL`), recadrage possible (`crop`).
- Rideau d’entrée : `clip-path` de bas en haut en 1,2 s, l’image passe de 112 à 100 %.
- Texte :
  - discipline en accent (15 px) ;
  - titre `t-card` ;
  - mention « Concept studio, année » ;
  - idée (17 px) et pistes explorées en puces.

---

## 4. États (récapitulatif)

| Élément | Repos | Survol | Focus clavier | Actif / chargement |
|---|---|---|---|---|
| Bouton principal | Braise pleine | Échelle 1,03, flèche qui glisse | Contour 2 px, décalé de 3 px | « Envoi… », opacité 60 % |
| Lien de navigation | Opacité 75 % | Texte qui roule | Contour 2 px | Point braise |
| Tuile | Charbon | Halo braise | Contour 2 px | Visuel animé quand visible |
| Image de projet | Rideau fermé | Zoom 1,04 à 1,06 | Contour 2 px | Rideau ouvert |
| Champ | Soulignement 1 px | – | Soulignement couleur texte | Erreur en alerte |
| Filtre | Contour fin | Contour renforcé | Contour 2 px | Plein braise |

Surfaces du navigateur [Observé] :

- sélection de texte en braise ;
- curseur de saisie en braise ;
- barre de défilement en cendre ;
- soulignements décalés de 0,2 em.

---

## 5. Responsive

- **Points de rupture** : 768 px (grille 12 colonnes) ; 1024 px (affichage de l’heure dans la barre).
- **Hauteurs basses** (moins de 560 px) : mot-signature réduit à 15vw et aligné à gauche, paragraphe du hero masqué.
- **Typographie fluide** : `clamp()` pour les titres, vw pour le mot-signature (21vw, calé pour tenir dans la largeur, souris comprise).
- **Images** : AVIF et WebP servis par Next.js, tailles adaptées (`sizes`), aperçu flou.
- **Garantie** : aucun défilement horizontal de 390 à 2 560 px (vérifié).

---

## 6. Mouvement

### Tokens

| Token | Valeur | Usage |
|---|---|---|
| Ease-out expo | `cubic-bezier(0.16, 1, 0.3, 1)` | Entrées, survols, états |
| Ease-in-out quint | `cubic-bezier(0.83, 0, 0.17, 1)` | Rideaux, tracés, soulignements |
| Rapide | 300 ms | Couleurs, filtres |
| Base | 500 ms | Survols, barre de navigation |
| Lent | 700 ms | Étapes de la méthode, transitions de page |
| Apparition | 1 100 ms, décalage de 45 ms par mot | Titres en masque |
| Rideau | 1 200 ms | Images de projets |

### Signatures

| Moment | Comportement |
|---|---|
| Hero | Soie WebGL, rendue à demi-résolution, démarrée après le chargement, en pause hors écran ; lettres qui montent une à une (70 ms d’écart) puis s’élargissent près du pointeur |
| Expertises | Apparition 3D liée au scroll |
| Réalisations (accueil) | Galerie zoom : section collante sur 300vh, sept images qui grandissent chacune à sa vitesse (×4 à ×9) |
| Méthode | Grand numéro qui défile, barre de progression en quatre segments, titre actif mis en avant |
| Inter-pages | View Transitions entre l’accueil et `/realisations` (l’image cliquée se transforme) |

### Règles

- Transform et opacité uniquement (sauf `clip-path` pour les rideaux).
- Un seul écouteur de scroll par type d’effet, cadencé par `requestAnimationFrame`.
- Les animations hors écran sont mises en pause.
- **Réduction des animations** :
  - plus d’épinglage ni de trajet : l’état final s’affiche ;
  - le fond animé se fige sur une image ;
  - les transitions de page sont coupées.

---

## 7. Intégration rapide

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Instrument+Serif:ital@1&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="nexora-tokens.css">

<section class="nx-theme-os">
  <h2 style="font-family:var(--nx-font-display);font-size:var(--nx-type-section);font-weight:900;font-variation-settings:'wdth' 125;letter-spacing:var(--nx-tracking-display);line-height:var(--nx-leading-display)">Du brief à l’image.</h2>
</section>
```

[Recommandé] Dans le code du site, remplacer progressivement les valeurs codées en dur (illustrations, fond animé, logo) par ces variables.
