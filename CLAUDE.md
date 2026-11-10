# Mémoire du projet NEXORA

Fichier de contexte pour les sessions Claude. Mis à jour le 10 novembre 2026.

## Le studio

- Studio créatif basé au Bénin (Cotonou), trois associés sans hiérarchie, issus de l'audiovisuel de terrain.
- Trois pôles : communication visuelle et audiovisuel (dont prestation événementielle : son, projection, captation, location de matériel), motion design, création de sites web. Le brand design est transversal, ce n'est pas un quatrième pôle.
- Cible : particuliers, PME, événementiel, institutions, et surtout l'international. Positionnement premium accessible.
- Ne jamais citer de nom, prénom ou rôle individuel des associés dans un livrable. Pas de section « à propos » ni « équipe » pour l'instant.

## Règles de travail (demandées par l'utilisateur)

- Répondre en français. Pas de tirets cadratins dans les textes.
- Ne jamais inventer de clients, témoignages, chiffres ou projets.
- Ne jamais pousser en production (`main`) sans validation explicite.
- Ne jamais prétendre qu'un fichier a été déposé (Drive) ou qu'un nom/domaine est disponible sans confirmation réelle.
- Tester le responsive (390, 768/1024, 1440, 1920 px) et vérifier visuellement avant de livrer.
- Pas de rendu « site fait par IA » : design soigné, animé, pas de gabarit générique.

## Technique

- Dépôt : `nexora2302-create/NEXORA_REBUILD`. Branche de travail : `claude/nexora-rebuild-base`, poussée sur `main` uniquement sur demande.
- Site : `NEXORA-REBUILD/02_NEXORA_WORKING` (Next.js 16, React 19, Tailwind v4, three.js). Vercel déploie depuis `main` (dossier racine ci-dessus). URL : https://nexoraa-nu.vercel.app
- Composants principaux dans `components/nexora/` : `hero.tsx` + `nx-scene.ts` (sculpture 3D du X, affiche WebP de repli, 3D seulement avec vraie carte graphique), `manifesto.tsx` (Studio), `expertises.tsx` + `stack-cards.tsx`, `work.tsx` (galerie zoom), `method.tsx` (panneaux), `header.tsx` (barre toujours visible), `contact.tsx`, page `/realisations`.
- Reste à faire côté utilisateur : variable `NEXT_PUBLIC_FORM_ENDPOINT` dans Vercel ; activer Vercel Web Analytics ou retirer le composant.

## Marque : historique des décisions

- Identité actuelle en ligne (« Braise ») : encre #0D0C0B, os #ECE5D8, braise #FF4A1C ; Archivo largeur 125 graisse 900 ; logo NX. Brand book v1 dans `NEXORA-BRAND/01` à `05`.
- Logo : exploration dans `NEXORA-BRAND/06-LOGO-EXPLORATION`. Pistes Courbe, Décalage, Entrelacs. **Entrelacs retenu** (deux rubans tordus en X, prolongement du hero 3D), animation : arrivée du fond puis tour sur l'axe vertical. Pas encore intégré au site.
- Atelier de marque (4 directions de couleurs, logo Entrelacs) : `NEXORA-BRAND/07-REBRANDING/atelier-4-directions.html`. Recommandation : **Indigo** (nuit indigo, indigo, coton, braise conservée pour l'action ; Gloock + Archivo). Non validé.
  - Correction demandée et non terminée : le X (symbole) n'est pas centré dans le mot NEXORA de l'atelier ; recadrer le symbole sur sa forme réelle (boîte ~215–983 × 273–927 dans le repère 1200) et l'espacer comme une lettre.
- Rebranding complet (nouveau nom) : `NEXORA-BRAND/07-REBRANDING/rebrand-3-propositions.html` (Volta, Sillage, Avant ; « Next Studio » écarté) et `volta-identite-et-maquette.html` (identité complète + maquette d'accueil clair/sombre). **Recommandation : Volta**, tagline « On met le courant. / We switch brands on. », symbole à trois faisceaux en V. **En attente de décision des associés.**
  - Domaines testés (RDAP, 9 nov. 2026) : .com et .studio exacts des trois noms pris ; thevoltastudio.com, maisonvolta.com, maisonvolta.studio libres à cette date. Restent à vérifier par l'utilisateur : .bj, réseaux sociaux, OAPI/WIPO/EUIPO/INPI/USPTO (classes 35, 41, 42), sens en fon, yoruba, espagnol, portugais, arabe.
- **Audit v2 (10 nov. 2026) : Volta abandonné, recommandation STROBE.** Fichiers dans `NEXORA-BRAND/07-REBRANDING/v2/` (`Volta_v2_audit.html`, `Volta_v2_identité_et_site.html`, sources Python/CSS/JS dans `v2/sources/`, générer avec `python3 audit.py` et `python3 site.py`).
  - Raison : au moins six studios de design s'appellent déjà Volta (Porto, Berne, Utrecht, Anvers, Sheffield, Toronto/Québec) ; Haute-Volta coloniale ; volta.design pris. Écartés aussi : Takt (agence Vancouver), Gobo (Studio Gobo, Brighton). Alternative francophone : Raccord.
  - Strobe : concept « le flash qui fige le mouvement, l'image qui reste ». Domaine principal visé strobe.design (RDAP registre 404 = libre le 10 nov. 2026), thisisstrobe.com et strobe-studio.com libres ; strobe.com/.studio/.co pris ; strobe.bj sans délégation DNS (à vérifier). Compte visé @strobe.design (non vérifié).
  - Logo : disque décalé (disque coupé à l'horizontale, moitiés glissées de 17 % du diamètre, forme un S), sert de O dans le logotype (Anybody 900, wdth 100). Version animée : mot en trois bandes qui se calent au flash.
  - Slogans : maîtresse « Ça marque. / Burned in. » ; pôles : « Pas de deuxième prise. / No second takes. », « Chaque image frappe. / Every frame hits. », « Vite chargé, dur à oublier. / Loads fast. Lands hard. » ; CTA « On tourne ? / Ready to roll? », bouton « Envoyer le brief ».
  - Identité : noir salle #0B0C0E, blanc flash #F3F5F2, xénon #22E1FF (jamais en texte sur blanc), xénon profond #006F84 (texte en clair) ; Anybody + Schibsted Grotesk (+ Martian Mono pour les données). Motion « le flash » 900 ms (dérive, charge, flash unique, rémanence), max 3 flashs/s. Signature sonore 1,5 s (charge, clac + coup sourd, quinte qui s'éteint), prototype Web Audio.
  - **En attente de décision des associés.** Rien n'est intégré au site.
- **Nom v3 (10 nov. 2026) : recommandation RHYTHMOS** (Strobe = plan B ; « 911 Studio » écarté). Brief modifié par l'utilisateur : poids des pôles = motion design, identité/communication visuelle, web d'abord ; audiovisuel au second plan ; nom à sens profond (langues anciennes), slogans longs + version courte, logo à idée cachée, son = bonus. Fichiers dans `NEXORA-BRAND/07-REBRANDING/v3/` (`propositions_nom_v3.html`, `identité_et_site_rhythmos.html`, sources `v3/sources/` : `props.py`, `site3.py`, `marks3.py`).
  - Rhythmos (grec ῥυθμός) : avant « rythme », voulait dire « forme », la forme d'une chose qui bouge (Benveniste 1951 ; Aristote, Métaphysique 985b : Démocrite, « A diffère de N par la forme »). Logo : R = Ρ grec (rhô) + jambe détachée qui « fait un pas » ; logotype Mona Sans 800 en mètre (larges 125 / étroites 75, fin d'hexamètre). Couleur kyanos #2340D8 (clair #6E86FF en sombre), plâtre #F2F3F5, encre #121214 ; Mona Sans + Newsreader italique. Motion : forme / ordre / position, 100 BPM. Son : le dactyle (la, mi, mi, la).
  - Signature : « Avant de dire « rythme », rhythmos voulait dire « forme »… Nous dessinons des marques qui bougent sans jamais perdre la leur. » Courte : « Garder la forme. / In motion. In shape. »
  - Domaines (RDAP registre, 10 nov. 2026) : rhythmos.studio, rhythmos.design, rhythmosstudio.com libres ; rhythmos.com pris (société d'analyse énergétique, risque classe 42), rhythmos.co pris (conseil aux églises). Compte visé @rhythmos.studio (non vérifié).
  - Autres planches : Roshem (hébreu רֹשֶׁם, empreinte ; sceau et empreinte en miroir ; risque politique Golfe) et Àmì (yoruba, signe ; accents = àmì ohùn ; AMI Paris). Tons yoruba de l'exemple ọkọ à faire valider par un locuteur ; fon/goun non couverts.
  - **En attente de décision des associés.**
- **Nom v4 (10 nov. 2026) : recommandation KERAIA** (l'utilisateur n'a « rien ressenti » avec Strobe ni Rhythmos ; il veut une lecture publique moderne + une lecture cachée biblique, type ICHTHYS, pas trop connue). Fichier unique `NEXORA-BRAND/07-REBRANDING/v4/nom_v4_keraia.html` (sources `v4/sources/nom4.py`, `marks4.py`). Identité complète et site NON construits : l'utilisateur valide d'abord le nom.
  - κεραία : « petite corne » ; le trait d'une lettre (Mt 5:18 « pas un iota, pas un trait » ; Lc 16:17) ; « antenne » en grec moderne. Lecture cachée : la corne d'huile de l'onction de David (1 S 16:13, « τὸ κέρας τοῦ ἐλαίου » dans la Septante ; qeren en hébreu), 1 S 2:10, Jos 6:5, Lc 1:69. Phrase privée : « Lève-toi, oins-le, car c'est lui » (1 S 16:12).
  - Logo : un i dont le point est une petite corne inclinée qui « verse » sur la tige (iota + keraia ; lu aussi comme micro sur pied, antenne). Logotype « keraia » en minuscules, Gloock. Couleur pourpre #6B1D52 (clair #D592BE en sombre), lin #F4F4F1, encre #141215 ; Gloock + Hanken Grotesk.
  - Slogans : longue « En grec, keraia, c'est le plus petit trait d'une lettre, et c'est l'antenne qui porte une voix au loin… » ; courte « Jusqu'au dernier trait. / Down to the last stroke. » ; campagne « C'est lui. / This is the one. »
  - Finalistes : Effata (Mc 7:34-37 ; connu du rite catholique), Mahir (Pr 22:29 ; prénom courant, domaines pris). Écartés notables : Qeren (« Karen », Keren Kayemet), Betsalel (Académie Bezalel), Tav (X de Twitter, TAV), Chotam (khatam en arabe), Ramkol.
  - Domaines (RDAP, 10 nov. 2026) : keraia.studio, keraia.design, keraiastudio.com libres ; keraia.com et keraia.gr pris. À vérifier : .bj, comptes, marques, hellénophone, arabophone (proximité « karāhiya »), locuteurs fon/yoruba.

## Artefacts publiés (privés, compte de l'utilisateur)

- Planche logo : https://claude.ai/artifact/SsBfugxB9n33WY8H44C9yo
- Atelier 4 directions : https://claude.ai/artifact/CTrTexL7UF3dQzfMrE2BZU
- Rebranding 3 propositions : https://claude.ai/artifact/8JhJxGKmC5z2rK4f55k8pJ
- Identité Volta + maquette : https://claude.ai/artifact/F2bvJF72i1eu61WpWSPGj7
- Audit v2 (Volta → Strobe) : https://claude.ai/artifact/KjG6PnY4nG3A2hoHEvGdGX
- Identité Strobe + maquette du site : https://claude.ai/artifact/CLyyn7L7bPa7hNubkHJMpj
- Propositions de nom v3 : https://claude.ai/artifact/UP5iJ6DBqS5RRkRChtpHkK
- Identité Rhythmos + maquette du site : https://claude.ai/artifact/Je7ZA4EwjgrjrekBUE44fY
- Nom v4 Keraia : https://claude.ai/artifact/RuVE6f8coVCJgngHArSgUo

## Prochaines étapes probables

1. Décision des associés sur le nom (Volta ou autre) et la direction de couleurs.
2. Finaliser le logo choisi, puis l'intégrer au site (en-tête, pied de page, favicon, icône Apple, image de partage) sans toucher au reste.
3. Mettre à jour le brand book et les fichiers de logo.
