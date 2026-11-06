# Exploration du logo NEXORA (deuxième tour)

Trois pistes, à comparer avant toute intégration au site :

1. **Courbe** : le N dessiné par la courbe d'animation du site, `cubic-bezier(0.83, 0, 0.17, 1)`. Piste recommandée.
2. **Décalage** : logotype NEXORA dont la branche montante du X a glissé d'un sixième de la hauteur.
3. **Entrelacs** : deux lames qui se croisent, prolongement du hero 3D.

- `planche-pistes-logo.html` : planche de présentation (ouvrir dans un navigateur).
- `svg/` : symboles et logotypes de chaque piste, en couleur (fond sombre, fond clair), noir et blanc.
- `sources/` : scripts de génération (Python ; contours d'Archivo largeur 125, graisse 900, instanciés avec fontTools).

Le site n'est pas modifié à cette étape.

## Deuxième tour : Entrelacs approfondi

- `svg/entrelacs-v2/` : nouveau symbole (rubans tordus, face os et tranche braise), six agencements de couleurs, versions transparentes, version réduite pour 32 px et moins, symbole animé (SVG natif), mot signature.
- `sources/entfinal.py` : dessin du symbole ; `sources/x3d.js` : logo 3D animé (mêmes rubans que la sculpture du hero).
