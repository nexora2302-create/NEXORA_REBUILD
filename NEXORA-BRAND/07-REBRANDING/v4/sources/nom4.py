import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from marks4 import symbol, wordmark, svg
from typo import fr_typo
CSS = open(os.path.join(HERE, 'base4.css')).read() + open(os.path.join(HERE, 'nom4.css')).read()
INK, PAP, PO, POL = '#141215', '#F4F4F1', '#6B1D52', '#D592BE'

def S(fg='currentColor', acc='var(--x)', cls='sy', label='Symbole Keraia', drop=False):
    return svg(symbol(fg, acc, drop=drop), '0 0 100 100', cls, label)
def W(fg='currentColor', acc='var(--x)', cls='wm', label='keraia'):
    i, w, h = wordmark('gloock.ttf', fg, acc); return svg(i, f'-30 0 {w+60:.0f} {h}', cls, label)

# ---------- divergence : 86 candidats ----------
# (écriture, translittération, langue, sens, référence, verdict, classe, certitude)
C = {
'Le créatif, l’artisan': [
 ('בְּצַלְאֵל', 'Betsalel', 'héb.', 'premier artisan rempli de l’Esprit', 'Ex 31:2-5', 'Académie Bezalel, école de design célèbre', 'ko', 's'),
 ('אָהֳלִיאָב', 'Oholiav', 'héb.', 'son compagnon, graveur et brodeur', 'Ex 31:6 ; 38:23', 'Imprononçable', 'ko', 's'),
 ('חֹשֵׁב', 'choshev', 'héb.', 'le concepteur (« œuvre du concepteur »)', 'Ex 26:1 ; 28:6', '« ch » guttural ; « il pense » en hébreu moderne', 'ko', 's'),
 ('מַחֲשָׁבֹת', 'machashavot', 'héb.', 'desseins, inventions', 'Ex 31:4', 'Trop long', 'ko', 's'),
 ('חִשְּׁבֹנוֹת', 'chishvonot', 'héb.', 'inventions des ingénieux : « son nom se répandit au loin »', '2 Ch 26:15', 'Imprononçable ; verset gardé pour l’histoire privée', 'mid', 's'),
 ('חָרָשׁ', 'charash', 'héb.', 'graveur, artisan', 'Ex 35:35', 'Imprononçable', 'ko', 's'),
 ('רֹקֵם', 'roqem', 'héb.', 'brodeur, tisseur de couleurs', 'Ex 26:36', 'Sonne « rocket »', 'ko', 's'),
 ('רִקְמָה', 'riqmah', 'héb.', 'broderie', 'Ez 16:10', '« Tissu » biologique en hébreu moderne', 'ko', 's'),
 ('אָמוֹן', 'amon', 'héb.', 'maître d’œuvre (la Sagesse à la création)', 'Pr 8:30', 'Amon, dieu égyptien', 'ko', 's'),
 ('יֹצֵר', 'yotser', 'héb.', 'le potier, celui qui façonne', 'Jr 18:4', 'Bénédiction liturgique « Yotser Or »', 'ko', 's'),
 ('בָּרָא', 'bara', 'héb.', 'créer', 'Gn 1:1', 'Trop connu des prédicateurs', 'ko', 's'),
 ('ποίημα', 'poiēma', 'gr.', 'l’ouvrage', 'Ep 2:10', 'Déjà courant (églises, agences)', 'ko', 's'),
 ('τεχνίτης', 'technitēs', 'gr.', 'le concepteur de la cité', 'Hé 11:10', '« Tech »', 'ko', 's'),
 ('δημιουργός', 'dēmiourgos', 'gr.', 'le bâtisseur', 'Hé 11:10', '« Démiurge » : lecture gnostique', 'ko', 's'),
 ('ἀρχιτέκτων', 'architektōn', 'gr.', 'maître bâtisseur', '1 Co 3:10', 'Saturé', 'ko', 's'),
 ('רֹקֵחַ', 'roqeach', 'héb.', 'le parfumeur de l’huile d’onction', 'Ex 30:25', 'Marque Rokeach', 'ko', 's'),
 ('מָהִיר', 'mahir', 'héb.', 'habile, prompt : « il se tiendra devant les rois »', 'Pr 22:29 ; Ps 45:2 ; Esd 7:6', 'Finaliste', 'f', 's'),
 ('סֹפֵר', 'sofer', 'héb.', 'scribe', 'Esd 7:6', 'Scribe de la Torah : lecture religieuse', 'ko', 's'),
],
'L’onction, la marque, la royauté': [
 ('מָשַׁח', 'mashach', 'héb.', 'oindre', '1 S 16:13', 'Trop proche de « Messie »', 'ko', 's'),
 ('מָשִׁיחַ', 'mashiach', 'héb.', 'l’oint', '1 S 2:10', 'Trop connu', 'ko', 's'),
 ('χρίσμα', 'chrisma', 'gr.', 'l’onction', '1 Jn 2:20, 27', 'Se lit « Christ »', 'ko', 's'),
 ('χρίω', 'chriō', 'gr.', 'oindre', 'Lc 4:18', 'Idem', 'ko', 's'),
 ('שֶׁמֶן', 'shemen', 'héb.', 'huile', '1 S 16:13', '« Semen » en anglais', 'ko', 's'),
 ('פַּךְ', 'pakh', 'héb.', 'fiole d’huile (onction de Saül)', '1 S 10:1', 'Une syllabe, sonne mal', 'ko', 's'),
 ('קֶרֶן', 'qeren', 'héb.', 'corne : d’huile, de son, de force ; rayon', '1 S 16:13 ; 2:10 ; Jos 6:5', 'Le plus riche, mais « Karen » en anglais et Keren Kayemet (lecture politique). Devenu le sens caché de Keraia', 'mid', 's'),
 ('κέρας', 'keras', 'gr.', 'corne', 'Lc 1:69 ; 1 S 16:13 (Septante)', 'Keras, bibliothèque d’IA célèbre', 'ko', 's'),
 ('κεραία', 'keraia', 'gr.', 'petite corne ; le trait d’une lettre ; antenne (grec moderne)', 'Mt 5:18 ; Lc 16:17', 'Recommandé', 'x', 's'),
 ('נֵזֶר', 'nezer', 'héb.', 'couronne, consécration', 'Ex 29:6', 'Sonne dur', 'ko', 's'),
 ('עֲטֶרֶת', 'ateret', 'héb.', 'couronne', 'Pr 12:4', 'Prénom courant, connu', 'ko', 's'),
 ('חוֹתָם', 'chotam', 'héb.', 'sceau : « je te garderai comme un sceau »', 'Ag 2:23 ; Ct 8:6', 'Hotam (association israélienne) ; khatam en arabe (« sceau des prophètes »)', 'ko', 's'),
 ('תָּו', 'tav', 'héb.', 'la marque sur le front', 'Ez 9:4', 'TAV (aéroports turcs), et un X après celui de Twitter', 'ko', 's'),
 ('σφραγίζω', 'sphragizō', 'gr.', 'marquer d’un sceau', '2 Co 1:22', 'Formule de la chrismation orthodoxe ; imprononçable', 'ko', 's'),
 ('ἀρραβών', 'arrabōn', 'gr.', 'les arrhes, le gage', '2 Co 1:22', 'Sonne « à rabot »', 'ko', 's'),
 ('χαρακτήρ', 'charaktēr', 'gr.', 'l’empreinte exacte', 'Hé 1:3', '« Caractère », générique', 'ko', 's'),
 ('ἀπαύγασμα', 'apaugasma', 'gr.', 'le rayonnement', 'Hé 1:3', 'Trop long', 'ko', 's'),
 ('נָגִיד', 'nagid', 'héb.', 'le chef désigné', '1 S 13:14', 'Nom de famille ; sonne « nag »', 'ko', 's'),
 ('צֶמַח', 'tsemach', 'héb.', 'le Germe, roi et prêtre, qui bâtira', 'Za 6:12', '« Tzemach Tzedek » (rebbe hassidique) ; « ts » et « ch »', 'mid', 's'),
 ('נֵצֶר', 'netser', 'héb.', 'le rejeton', 'Es 11:1 ; 60:21', 'Mouvement de jeunesse sioniste : lecture politique', 'ko', 's'),
 ('זֶה הוּא', 'zeh hu', 'héb.', '« c’est lui »', '1 S 16:12', 'Pas un nom : gardé comme phrase cachée', 'mid', 's'),
 ('ψῆφος', 'psēphos', 'gr.', 'le caillou blanc portant un nom nouveau', 'Ap 2:17', 'Le plus beau verset sur le nom, imprononçable', 'mid', 's'),
],
'Celui qui ouvre et met en mouvement': [
 ('פֹּרֵץ', 'porets', 'héb.', 'celui qui fait la brèche, devant leur roi', 'Mi 2:13', 'Sonne mal ; nom de famille', 'ko', 's'),
 ('פֶּרֶץ', 'perets', 'héb.', 'brèche (Pérets, ancêtre de David)', 'Gn 38:29', 'Pérez, nom courant', 'ko', 's'),
 ('פָּרַץ', 'parats', 'héb.', 'déborder, s’étendre', 'Gn 28:14', '« Rats »', 'ko', 's'),
 ('ἐφφαθά', 'ephphatha', 'aram. (en grec)', '« ouvre-toi » : il fait entendre les sourds et parler les muets', 'Mc 7:34-37', 'Finaliste', 'f', 's'),
 ('ταλιθα κουμ', 'talitha koum', 'aram.', '« fillette, lève-toi »', 'Mc 5:41', 'Trop connu', 'ko', 's'),
 ('קוּם', 'qum', 'héb.', 'lève-toi', '1 S 16:12', 'Qom, ville sainte chiite', 'ko', 's'),
 ('פָּתַח', 'patach', 'héb.', 'ouvrir', 'Es 22:22', 'Sonne mal', 'ko', 's'),
 ('מַפְתֵּחַ', 'mafteach', 'héb.', 'la clé de David', 'Es 22:22', 'Imprononçable', 'ko', 's'),
 ('κλείς', 'kleis', 'gr.', 'la clé de David', 'Ap 3:7', 'Une syllabe, faible', 'ko', 's'),
 ('צָלַח', 'tsalach', 'héb.', 'fondre sur ; faire réussir', '1 S 16:13 ; Ps 45:5', '« Salah » : la prière en arabe', 'ko', 's'),
 ('מַצְלִיחַ', 'matsliach', 'héb.', 'celui qui réussit (Joseph)', 'Gn 39:2', 'Trop long', 'ko', 's'),
 ('βοανεργές', 'boanerges', 'gr.', 'fils du tonnerre', 'Mc 3:17', 'Long ; tonnerre = cliché', 'ko', 's'),
 ('παρρησία', 'parrēsia', 'gr.', 'l’assurance de parole des hommes « sans instruction »', 'Ac 4:13, 29', 'Quatre syllabes ; Foucault', 'mid', 's'),
 ('δύναμις', 'dynamis', 'gr.', 'puissance', 'Ac 1:8', 'Trop connu', 'ko', 's'),
 ('יוֹבֵל', 'yovel', 'héb.', 'la corne de bélier (et le jubilé)', 'Jos 6:5', 'Jubilé : trop connu', 'ko', 's'),
],
'L’expansion': [
 ('רְחֹבוֹת', 'rechovot', 'héb.', '« Dieu nous a mis au large »', 'Gn 26:22', 'Rehoboth : plusieurs villes', 'ko', 's'),
 ('מֶרְחָב', 'merchav', 'héb.', 'le lieu spacieux', 'Ps 118:5', '« Espace » banal en hébreu moderne', 'ko', 's'),
 ('הַרְחִיבִי', 'harchivi', 'héb.', '« élargis l’espace de ta tente »', 'Es 54:2', 'Trop long', 'ko', 's'),
 ('יַרְחִיב', 'yarchiv', 'héb.', '« le don d’un homme lui fait de la place »', 'Pr 18:16', 'Imprononçable ; verset gardé', 'mid', 's'),
 ('מַתָּן', 'mattan', 'héb.', 'le don', 'Pr 18:16', 'Prénom courant', 'ko', 's'),
 ('רָקִיעַ', 'raqia', 'héb.', 'l’étendue qui annonce l’œuvre de ses mains', 'Gn 1:6 ; Ps 19:2', 'Rakija, eau-de-vie des Balkans', 'ko', 's'),
 ('רֹקַע', 'roqa', 'héb.', 'celui qui étend la terre', 'Es 42:5', 'Sonne « roca »', 'ko', 's'),
 ('קַו', 'qav', 'héb.', 'le cordeau, et « leur voix » qui parcourt la terre', 'Ps 19:5', 'Trop court ; terme de kabbale', 'ko', 's'),
 ('מַגְדִּיל', 'magdil', 'héb.', 'celui qui rend grand, pour son roi et son oint', 'Ps 18:51', 'Phrase connue de la prière après le repas ; « Magdala »', 'ko', 'p'),
 ('נֹבֵעַ', 'novea', 'héb.', 'qui jaillit : « source de sagesse, torrent qui jaillit »', 'Pr 18:4', 'Sonne cosmétique, générique', 'ko', 's'),
 ('יַבִּיעַ', 'yabbia', 'héb.', 'fait jaillir la parole', 'Ps 19:3', 'Imprononçable', 'ko', 's'),
 ('πλατύνω', 'platynō', 'gr.', 'élargir le cœur', '2 Co 6:11', '« Platine »', 'ko', 's'),
 ('תְּהוֹם', 'tehom', 'héb.', 'l’abîme', 'Gn 1:2', 'Sombre', 'ko', 's'),
],
'Le micro, la voix portée': [
 ('קוֹל', 'qol', 'héb.', 'voix (et kol, « tout »)', 'Es 40:3', 'Kol Nidre, Kol Israel : trop connu', 'ko', 's'),
 ('רַמְקוֹל', 'ramkol', 'héb. moderne', 'haut-parleur, « voix haute » ; écho de « élève ta voix »', 'Es 40:9 ; 58:1', 'Dur, et lu comme un mot israélien', 'mid', 's'),
 ('מַגְבִּיר', 'magbir', 'héb. moderne', 'amplificateur', '·', 'Pas biblique dans ce sens', 'ko', 's'),
 ('פֶּה', 'peh', 'héb.', 'la bouche : Aaron « te servira de bouche »', 'Ex 4:16', 'Une syllabe', 'ko', 's'),
 ('נָבִיא', 'navi', 'héb.', 'porte-parole, prophète', 'Ex 7:1', '« Prophète » trop visible', 'ko', 's'),
 ('נִיב', 'niv', 'héb.', 'le fruit des lèvres, que Dieu crée', 'Es 57:19', 'NIV, version de la Bible', 'ko', 's'),
 ('מֵלִיץ', 'melits', 'héb.', 'l’interprète', 'Gn 42:23 ; Jb 33:23', '« Langue ampoulée » en hébreu moderne', 'ko', 's'),
 ('מְבַשֵּׂר', 'mevasser', 'héb.', 'celui qui porte la bonne nouvelle', 'Es 52:7', 'Mubashshir, terme coranique', 'ko', 's'),
 ('אִמְרָה', 'imrah', 'héb.', 'la parole éprouvée au feu', 'Ps 12:7', 'Imra’a : « femme » en arabe', 'ko', 's'),
 ('κῆρυξ', 'kēryx', 'gr.', 'le héraut', '1 Tm 2:7', 'Keryx, laboratoire pharmaceutique', 'ko', 's'),
 ('ἦχος', 'ēchos', 'gr.', 'l’écho, la renommée', 'Lc 4:37', 'Saturé', 'ko', 's'),
 ('φθόγγος', 'phthongos', 'gr.', 'le son qui parcourt la terre', 'Rm 10:18', 'Imprononçable', 'ko', 's'),
 ('שׁוֹפָר', 'shofar', 'héb.', 'la trompe', 'Jos 6:4', 'Trop connu', 'ko', 's'),
 ('σάλπιγξ', 'salpinx', 'gr.', 'la trompette', '1 Co 15:52', 'Terme médical (trompe)', 'ko', 's'),
],
'La lettre, le signe, l’écriture': [
 ('ἰῶτα', 'iōta', 'gr.', 'le iota, la plus petite lettre', 'Mt 5:18', 'IOTA, cryptomonnaie', 'ko', 's'),
 ('יוֹד', 'yod', 'héb.', 'le yod', '·', 'Trop court', 'ko', 's'),
 ('תָּגִין', 'tagin', 'héb. (tradition)', 'les couronnes posées sur les lettres', 'Talmud, Menahot 29b', 'Pas biblique ; lecture religieuse', 'ko', 'p'),
 ('קֶסֶת', 'qeset', 'héb.', 'l’écritoire de celui qui marque les fronts', 'Ez 9:2', 'Sonne « cassette »', 'ko', 's'),
 ('עֵט', 'et', 'héb.', 'le stylet : « ma langue est le stylet d’un habile écrivain »', 'Ps 45:2', 'Une syllabe', 'ko', 's'),
 ('לֻחֹת', 'luchot', 'héb.', 'les tables', 'Ex 34:1', 'Connu', 'ko', 's'),
 ('κανών', 'kanōn', 'gr.', 'la règle, la mesure', '2 Co 10:13', 'Canon (marque)', 'ko', 's'),
 ('γράμμα', 'gramma', 'gr.', 'la lettre', '2 Co 3:6', '« La lettre tue » : mauvais signal', 'ko', 's'),
 ('ἐπιστολή', 'epistolē', 'gr.', 'la lettre écrite dans les cœurs', '2 Co 3:3', 'Long', 'ko', 's'),
 ('σημεῖον', 'sēmeion', 'gr.', 'le signe', 'Jn 2:11', '« Signes et prodiges » : charismatique', 'ko', 's'),
],
'Autres gisements (araméen, noms propres, sigles)': [
 ('Κηφᾶς', 'kepha', 'aram.', 'le roc', 'Jn 1:42', 'Trop connu', 'ko', 's'),
 ('Βαρναβᾶς', 'barnabas', 'aram.', 'fils de l’encouragement', 'Ac 4:36', 'Prénom connu', 'ko', 's'),
 ('Σιλωάμ', 'siloam', 'héb.', '« envoyé » : l’aveugle voit', 'Jn 9:7', 'Hôpitaux, connu', 'ko', 's'),
 ('Ταβιθά', 'tabitha', 'aram.', 'gazelle', 'Ac 9:36', 'Prénom', 'ko', 's'),
 ('Ῥαββουνί', 'rabbouni', 'aram.', 'maître', 'Jn 20:16', 'Connu', 'ko', 's'),
 ('Γαββαθᾶ', 'gabbatha', 'aram.', 'le lieu élevé', 'Jn 19:13', 'Lieu du jugement', 'ko', 's'),
 ('כּוֹרֶשׁ', 'koresh', 'héb.', 'Cyrus, appelé « oint », qui ouvre les portes', 'Es 45:1', 'Koresh : David Koresh, secte de Waco', 'ko', 's'),
 ('Ἀπολλῶς', 'apollos', 'gr.', 'l’orateur éloquent', 'Ac 18:24', 'Apollo', 'ko', 's'),
 ('Λυδία', 'lydia', 'gr.', 'marchande de pourpre', 'Ac 16:14', 'Prénom ; gardée pour la couleur', 'mid', 's'),
 ('קרן', 'KRN', 'sigle', 'les trois consonnes de qeren', '·', 'Illisible', 'ko', 's'),
 ('KERN', 'kern', 'anglais', 'l’approche typographique ; « noyau » en allemand ; qeren sans voyelle', '·', 'Une syllabe, saturé (noms de famille, marques)', 'mid', 's'),
],
}
n = sum(len(v) for v in C.values())
CERT = {'s': ('Sûr', 'ok'), 'p': ('Probable', 'mid')}
def row(o, t, l, g, r, v, c, ce):
    return f'<li class="c-{c}"><span class="og" lang="{ "he" if "héb" in l or "aram" in l else ("el" if "gr" in l else "fr") }">{o}</span><span class="tr">{t}</span><span class="lg">{l}</span><span class="gl">{g}</span><span class="rf">{r}</span><span class="vd">{v}</span><span class="tag t-{CERT[ce][1]}">{CERT[ce][0]}</span></li>'
field = ''.join(f'<div class="fld"><h3 class="eyebrow">{k} · {len(v)}</h3><ul>' + ''.join(row(*x) for x in v) + '</ul></div>' for k, v in C.items())

DROP = [
 ('Qeren, la corne', 'Le mot le plus riche de toute la recherche : la corne d’huile qui oint David, la corne de bélier qui fait tomber Jéricho, la corne qui « élève la force de son oint », le rayon sur le visage de Moïse. Mais en anglais américain, « Keren » se prononce comme « Karen », devenu une insulte de mème. Et Keren Kayemet est une institution sioniste : lecture politique dans le Golfe. Je n’ai pas jeté le sens : je l’ai caché sous Keraia.'),
 ('Betsalel', 'Le patron rêvé des créatifs, mais l’Académie Bezalel de Jérusalem est l’une des écoles de design les plus connues au monde. Impossible de s’en distinguer.'),
 ('Tav, la marque au front', 'Ezéchiel 9:4 : l’homme à l’écritoire marque d’un tav le front de ceux qui veillent. Le tav s’écrivait en X : votre ancien logo NEXORA en était un, sans le savoir. Mais un X après celui de Twitter, et TAV (groupe aéroportuaire turc) : mort.'),
 ('Ephphatha', 'Le plus proche du « micro » : la langue déliée, « il fait entendre les sourds et parler les muets ». Finaliste, mais connu dans le rite catholique du baptême.'),
 ('Psēphos', 'Apocalypse 2:17 : un caillou blanc sur lequel est écrit un nom nouveau, que seul celui qui le reçoit connaît. Le verset parfait pour une recherche de nom. Le mot, lui, est imprononçable.'),
 ('Ramkol', '« Haut-parleur » en hébreu moderne, littéralement « voix haute », en écho à « élève ta voix avec force » (Es 40:9). Le sens était là ; la musique non, et le mot se lit israélien.'),
 ('Chotam, le sceau', 'Aggée 2:23 : « je te garderai comme un sceau, car je t’ai choisi ». Mais en arabe, khatam renvoie au « sceau des prophètes » : lecture religieuse forte dans le Golfe.'),
 ('Mahir', 'Le plus solide sur le métier (« vois-tu un homme habile ? il se tiendra devant les rois »). Finaliste, mais c’est un prénom courant et les domaines sont pris.'),
]
drop = ''.join(f'<article><h3 class="d3">{a}</h3><p>{b}</p></article>' for a, b in DROP)

FIN = [
 ('Keraia', 'κεραία', 'Le trait d’une lettre ; l’antenne ; la petite corne.', 'Mt 5:18 ; Lc 16:17 · corne d’onction 1 S 16:13', 'Recommandé', 'x', 'Toutes les couches dans un mot : le détail (design), la voix portée (antenne), l’onction (corne). Mot inconnu des fidèles, beau à l’oreille. keraia.studio libre.'),
 ('Effata', 'ἐφφαθά', '« Ouvre-toi » : la langue déliée, l’oreille ouverte.', 'Mc 7:34-37', 'Finaliste', 'f', 'Le plus fort sur la voix. Mais connu du rite catholique du baptême et de nombreuses communautés : un client catholique sur trois peut le reconnaître. effata.studio libre ; effata.com à vendre.'),
 ('Mahir', 'מָהִיר', 'Habile, prompt : il se tiendra devant les rois.', 'Pr 22:29 ; Ps 45:2 ; Esd 7:6', 'Finaliste', 'f', 'Le plus juste sur le métier, et compris en arabe et en turc (« habile »). Mais c’est un prénom courant : le studio aura l’air de porter le nom d’une personne. mahir.studio, mahir.design et mahirstudio.com sont pris.'),
]
fin = ''.join(f'<article class="fc c-{c}"><p class="eyebrow">{st}</p><h3 class="fn">{a}</h3><p class="fo">{b}</p><p>{d}</p><p class="small">{r}</p><p>{v}</p></article>' for a, b, d, r, st, c, v in FIN)

DOM = [('keraia.studio', 'Libre', 'ok', 'RDAP du registre (Identity Digital) : 404'), ('keraia.design', 'Libre', 'ok', 'RDAP du registre .design : 404'), ('keraiastudio.com · studiokeraia.com · wearekeraia.com', 'Libres', 'ok', 'RDAP Verisign : 404'), ('keraia.co · keraia.io', 'Probablement libres', 'mid', 'DNS : domaine inexistant (non vérifié au registre)'), ('keraia.bj', 'Probablement libre', 'mid', 'Aucune délégation DNS ; pas de RDAP pour le .bj'), ('keraia.com', 'Pris', 'ko', 'RDAP : 200 ; site derrière une protection, usage inconnu'), ('keraia.gr', 'Pris', 'ko', 'Site d’actualités régionales en Grèce (Corinthie)')]
dom = ''.join(f'<tr><th scope="row"><code>{a}</code></th><td><span class="tag t-{c}">{b}</span></td><td>{d}</td></tr>' for a, b, c, d in DOM)

# construction du symbole
cons = f'''<svg class="cons" viewBox="-6 -2 112 104" role="img" aria-label="Construction du symbole">
<g stroke="var(--rule)" stroke-width=".3">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="100"/>' for x in range(0, 101, 10))}{''.join(f'<line x1="0" y1="{y}" x2="100" y2="{y}"/>' for y in range(0, 101, 10))}</g>
{symbol('var(--fg)', 'var(--x)')}
<line x1="50" y1="30" x2="50" y2="100" stroke="var(--x)" stroke-width=".4" stroke-dasharray="1 1"/>
<g class="cl"><text x="-4" y="104">iota : tige 16 × 46</text><text x="66" y="12">keraia : corne effilée</text><text x="66" y="18">embouchure sur l’axe</text></g></svg>'''

HTML = f'''<title>Keraia, le nom</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gloock&family=Hanken+Grotesk:ital,wght@0,400..700;1,400&family=JetBrains+Mono:wght@400..600&family=Noto+Serif:wght@500&family=Noto+Serif+Hebrew:wght@500&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="wrap"><a class="lg" href="#top">{W(cls='wm', label='keraia')}</a>
<nav aria-label="Parties"><a href="#raisonnement">Raisonnement</a><a href="#candidats">{n} candidats</a><a href="#finalistes">Finalistes</a><a href="#keraia">Keraia</a><a href="#logo">Logo</a><a href="#verifs">Vérifications</a></nav>
<button class="tg" type="button" id="themeBtn">Thème</button></div></header>
<main id="top">
<section class="wrap hero"><p class="eyebrow">Nom v4 · 10 novembre 2026 · deux lectures</p>
<div class="hgrid"><div class="hl"><h1 class="hn">{W(cls='wm hwm', label='keraia')}</h1>
<p class="lead">En grec, <b>keraia</b>, c’est le plus petit trait d’une lettre, celui qui distingue un signe d’un autre. En grec d’aujourd’hui, c’est aussi l’<b>antenne</b> : ce qui porte une voix au loin. Et, mot à mot, c’est une <b>petite corne</b>.</p>
<p class="small">Le reste de cette page dit ce que cette petite corne cache.</p></div>
<div class="hs night">{S(PAP, POL, 'sy hsy', drop=False)}</div></div></section>

<section class="wrap sec" id="raisonnement"><header><p class="eyebrow">Le raisonnement</p><h2 class="d2">Cinq fils, un seul mot.</h2></header>
<div class="cols"><div class="prose">
<p>Vous m’avez donné cinq fils : le créatif, l’onction, celui qui met en mouvement, l’expansion, le micro. J’ai d’abord cherché un mot par fil, puis j’ai compris que le bon mot n’en choisirait pas un : il les tiendrait tous par un seul objet.</p>
<p>Cet objet, c’est la <b>corne</b>. En hébreu, qeren. C’est la corne d’huile avec laquelle Samuel oint David, le plus jeune, qu’on était allé chercher aux champs (1 S 16:13). C’est la corne de bélier qui fait tomber les murs de Jéricho (Jos 6:5) : la première voix amplifiée de la Bible. C’est la « corne de son oint » que Dieu élève (1 S 2:10) : la royauté. Et le verbe de la même racine dit le visage de Moïse qui rayonne (Ex 34:29) : l’expansion.</p>
<p>Qeren ne passait pas les tests publics (voir plus bas). En grec, la corne se dit keras, et la Bible grecque l’emploie pour l’onction de David : « Samuel prit la corne d’huile ». Son diminutif, <b>keraia</b>, « petite corne », est le mot que Jésus emploie pour le plus petit trait d’une lettre : « pas un iota, pas un trait ne passera » (Mt 5:18). En grec moderne, c’est l’antenne.</p>
<p>Le créatif est dans le trait de lettre, le micro dans l’antenne, l’onction et la royauté dans la corne. Un mot de trois syllabes, que presque aucun croyant ne reconnaît en deux secondes.</p></div>
<ol class="method"><li><b>Divergence.</b> {n} candidats, sept gisements : hébreu, araméen, grec du Nouveau Testament et de la Septante, noms propres, sigles.</li><li><b>Destruction.</b> Six tests : bouche, notoriété, neutralité publique, homonymes, domaine, sens métier.</li><li><b>Convergence.</b> Trois finalistes, un recommandé.</li><li><b>Hypothèse déclarée.</b> Le logo est en minuscules : sans minuscule, pas de point sur le i, donc pas de keraia.</li></ol></div>
<h3 class="eyebrow">Les pistes les plus fortes que j’ai écartées</h3><div class="grid drops">{drop}</div></section>

<section class="wrap sec" id="candidats"><header><p class="eyebrow">Divergence et destruction</p><h2 class="d2">{n} candidats.</h2><p class="small">Références vérifiées dans les textes hébreux, grecs et la Septante quand elles portent le sens ; numérotation des Psaumes de la Bible hébraïque et de la Segond (le titre compte pour un verset). Sens tirés de Strong, Brown-Driver-Briggs et Thayer.</p></header>
<details class="all"><summary>Afficher les {n} candidats</summary><div class="fields">{field}</div></details></section>

<section class="wrap sec" id="finalistes"><header><p class="eyebrow">Convergence</p><h2 class="d2">Trois finalistes.</h2><p class="small">Strobe reste en réserve. Keraia le bat sur le sens, la profondeur et la beauté du mot, et l’égale sur le domaine.</p></header>
<div class="fins">{fin}</div></section>

<section class="wrap sec rec" id="keraia"><header><p class="eyebrow">Le recommandé</p><h2 class="d1">Keraia.</h2></header>
<div class="cols">
<dl class="fiche">
<dt>Écriture</dt><dd><span lang="el" class="gk">κεραία</span></dd>
<dt>Translittération</dt><dd>keraia</dd>
<dt>Prononciation</dt><dd>FR « ké-RAÏ-a » · EN « keh-RYE-uh » · en grec moderne « ké-ré-A »</dd>
<dt>Racine</dt><dd>Diminutif de κέρας (keras), la corne. Sens littéral : « petite corne », ce qui dépasse en forme de corne.</dd>
<dt>Sens anciens</dt><dd>Extrémité, pointe ; chez les grammairiens, les accents et signes posés sur les lettres ; dans les évangiles, le petit trait qui distingue une lettre hébraïque d’une autre (ד et ר, par exemple).</dd>
<dt>Grec moderne</dt><dd>Antenne (radio, télévision), et antenne d’insecte.</dd>
<dt>Références</dt><dd>Mt 5:18 ; Lc 16:17 (seules occurrences du Nouveau Testament). Lien caché : κέρας, « la corne d’huile », 1 S 16:13 dans la Septante ; qeren en hébreu.</dd>
<dt>Langue du texte</dt><dd>Grec du Nouveau Testament ; hébreu et grec de la Septante pour la corne.</dd>
<dt>Certitude</dt><dd><span class="tag t-ok">Sûr</span> pour les sens et les références (Strong G2762, Thayer, Septante) · <span class="tag t-mid">À faire confirmer</span> la prononciation moderne par un hellénophone</dd></dl>
<ol class="layers">
<li><span class="eyebrow">Lecture publique</span><p>Le plus petit trait d’une lettre, et l’antenne qui porte une voix au loin. Un studio qui soigne le détail et fait porter le message. Aucune église, aucun prosélytisme : un mot grec élégant, inconnu, qui se dit facilement.</p></li>
<li><span class="eyebrow">Le métier</span><p>Identité et communication visuelle : le trait, la typographie, le signe qui distingue. Motion et web : le signal, la diffusion. Audiovisuel, au second plan : l’antenne, le son porté.</p></li>
<li class="hid"><span class="eyebrow">Lecture cachée</span><p>« Pas un iota, pas un trait (keraia) de la Loi ne passera » (Mt 5:18) : la fidélité jusqu’au plus petit trait. Et la petite corne, c’est la corne d’huile de l’onction : « Samuel prit la corne d’huile et l’oignit au milieu de ses frères » (1 S 16:13), la corne du son qui fait tomber les murs (Jos 6:5), « il élèvera la corne de son oint » (1 S 2:10), « une corne de salut dans la maison de David » (Lc 1:69).</p></li></ol></div>
<div class="cols">
<div class="story"><p class="eyebrow">L’histoire à raconter à un client</p><p>En grec ancien, keraia désignait le petit trait qui termine une lettre : le détail qui fait qu’un signe n’est pas un autre. En grec d’aujourd’hui, le même mot veut dire « antenne » : ce qui porte une voix au loin. Notre studio vit entre les deux : le soin du plus petit trait, et la portée du message. Dans notre logo, le point du i est devenu ce petit trait. Regardez bien : on y voit aussi un micro sur son pied.</p></div>
<div class="story priv night"><p class="eyebrow">Ce que vous pouvez dire, en privé, à vos associés</p><p>Keraia, c’est le mot de Jésus en Matthieu 5:18 : pas un iota, pas un trait ne passera. Et keraia veut dire « petite corne » : la corne d’huile avec laquelle Samuel a oint David, le plus jeune, celui qu’on était allé chercher aux champs pendant que ses frères défilaient. Quand David est entré, Dieu a dit à Samuel : « Lève-toi, oins-le, car c’est lui » (1 S 16:12). Notre i, c’est un iota surmonté d’une corne d’huile. On vient du terrain, comme lui.</p></div></div></section>

<section class="wrap sec" id="logo"><header><p class="eyebrow">Le signe codé</p><h2 class="d2">Un iota et sa petite corne.</h2>
<p class="small">Interdits respectés : ni croix, ni poisson, ni colombe, ni flamme, ni éclair, ni onde, ni objectif, ni triangle, ni globe, ni point plein dans un O, ni disque décalé.</p></header>
<div class="cols"><figure class="pane">{cons}<figcaption>La tige est un iota. Son point est remplacé par une corne effilée dont l’embouchure tombe sur l’axe de la tige, comme pour verser. La corne suit un arc quadratique ; sa largeur croît de zéro à la pointe jusqu’à 62 % du rayon à l’embouchure.</figcaption></figure>
<div class="reads"><h3 class="eyebrow">Ce que chacun y voit</h3>
<ul><li><b>Tout le monde :</b> un i dont le point est devenu un trait de plume. Un détail de typographe.</li><li><b>Au deuxième regard :</b> un micro sur son pied, ou une antenne.</li><li><b>Ceux qui savent :</b> l’iota et la keraia de Matthieu 5:18, réunis en une lettre. Et une corne d’huile inclinée au-dessus d’une tête : l’onction.</li></ul>
<h3 class="eyebrow">L’animation (survolez le symbole)</h3>
<div class="anim night" tabindex="0" aria-label="Animation du symbole : survolez ou touchez">{S(PAP, POL, 'sy asy', drop=True)}</div>
<p class="small">La corne se redresse, s’incline, une goutte tombe sur la tige, et la tige grandit. En public : le point du i se pose. En privé : l’onction, puis l’élan.</p></div></div>
<div class="vers">
<div class="vv day bd">{W(INK, PO)}</div><div class="vv night">{W(PAP, POL)}</div>
<div class="vv day bd sq">{S(INK, PO)}</div><div class="vv night sq">{S(PAP, POL)}</div><div class="vv sq xb">{S(PAP, PAP)}</div><div class="vv day bd sq">{S(INK, INK)}</div></div>
<div class="tests">
<figure><div class="tst day bd">{S(INK, INK, 's16')}{S(INK, INK, 's24')}{S(INK, PO, 's32')}</div><figcaption>16, 24 et 32 px</figcaption></figure>
<figure><div class="tst day bd blr">{S(INK, INK)}</div><figcaption>Flou, sans le nom : une tige et une virgule renversée, reconnaissable</figcaption></figure>
<figure><div class="tst night">{S(PAP, PAP)}</div><figcaption>Négatif monochrome</figcaption></figure>
<figure><div class="tst ph">{S(PAP, PAP)}</div><figcaption>Sur image (fond simulé)</figcaption></figure></div></section>

<section class="wrap sec" id="slogans"><header><p class="eyebrow">Slogans</p><h2 class="d2">Jusqu’au dernier trait.</h2></header>
<div class="cols"><div class="slog"><p class="eyebrow">Ligne maîtresse · FR</p><p class="big">En grec, keraia, c’est le plus petit trait d’une lettre, et c’est l’antenne qui porte une voix au loin. Nous soignons le premier pour que la seconde soit entendue.</p>
<p class="eyebrow">Master line · EN</p><p class="big" lang="en">In Greek, keraia is the smallest stroke of a letter, and the antenna that carries a voice far away. We take care of the first, so the second gets heard.</p></div>
<div class="slog"><p class="eyebrow">Version courte</p><p class="d2">Jusqu’au dernier trait.</p><p class="d3 it" lang="en">Down to the last stroke.</p>
<p class="small">Double sens. En public : le soin du détail, jusqu’au dernier trait. Pour ceux qui savent : Matthieu 5:18, « pas un trait ne passera, jusqu’à ce que tout soit accompli ». En anglais, « stroke » est le trait de plume et aussi le coup décisif.</p>
<p class="eyebrow">Ligne de campagne, à garder pour un lancement</p><p class="d3">C’est lui. <span class="it" lang="en">This is the one.</span></p><p class="small">En public : ce qu’on dit quand on voit enfin la bonne identité. Pour ceux qui savent : 1 Samuel 16:12, « Lève-toi, oins-le, car c’est lui ». La NIV anglaise dit exactement « this is the one ».</p></div></div></section>

<section class="wrap sec" id="couleur"><header><p class="eyebrow">Couleur et typographie</p><h2 class="d2">Une pourpre, un caractère à empattements.</h2></header>
<div class="cols"><div class="pal">
<div class="pc" style="background:{PO};color:{PAP}"><b>Pourpre</b><code>#6B1D52</code><span>La couleur des rois, et celle de Lydie, « marchande de pourpre » (Ac 16:14) : la couleur d’un métier d’artisan devenue celle de la royauté. Sur lin : 9,9:1.</span></div>
<div class="pc" style="background:{POL};color:{INK}"><b>Pourpre clair</b><code>#D592BE</code><span>Pour le mode sombre. Sur encre : 7,7:1.</span></div>
<div class="pc" style="background:{PAP};color:{INK}"><b>Lin</b><code>#F4F4F1</code><span>Encre #141215 dessus : 16,9:1.</span></div></div>
<div class="tyl"><p class="eyebrow">Titrage · Gloock</p><p class="tA">keraia, le trait juste</p><p class="small">Un caractère à fort contraste dont les empattements en coin sont, littéralement, des keraiai : les petites cornes qui terminent les lettres.</p>
<p class="eyebrow">Texte · Hanken Grotesk</p><p class="tB">Identité, motion, web. Et, le jour J, le son et l’image en salle.</p></div></div></section>

<section class="wrap sec" id="verifs"><header><p class="eyebrow">Vérifications</p><h2 class="d2">Ce qui est vérifié, ce qui reste à faire.</h2></header>
<div class="cols"><div><h3 class="eyebrow">Homonymes (recherche web du 10 nov. 2026)</h3><ul class="vl"><li>Aucun studio de design, motion, branding ou web nommé Keraia trouvé.</li><li>KE.RA Design Studio : architecture d’intérieur en Indonésie. Nom différent, risque faible.</li><li>keraia.gr : site d’actualités régionales grec. keraia.com : usage inconnu (site protégé).</li><li>« Keraia » est un mot courant en Grèce (antenne) : on ne pourra pas l’interdire en grec, seulement le protéger comme marque de studio.</li></ul></div>
<div><h3 class="eyebrow">Domaines (10 nov. 2026, 02 h 57 UTC)</h3><div class="tbl"><table><tbody>{dom}</tbody></table></div>
<p class="small"><b>Domaine principal visé :</b> keraia.studio. Compte : @keraia.studio (non vérifié).</p></div></div>
<div class="todo"><h3 class="d3">À vérifier par vous</h3><ul>
<li><b>.bj</b> auprès d’un bureau d’enregistrement agréé ; comptes @keraia.studio et @keraiastudio sur Instagram, TikTok, Behance, LinkedIn, YouTube.</li>
<li><b>Marques :</b> OAPI, WIPO, EUIPO, INPI, USPTO, classes 35, 41 et 42.</li>
<li><b>Une personne qui lit le grec :</b> la prononciation moderne, et l’absence de sens familier gênant pour « keraia » en Grèce (c’est un mot du quotidien : antenne).</li>
<li><b>Une personne qui lit l’hébreu et le grec biblique :</b> la chaîne qeren → keras → keraia, et la formulation de la lecture cachée.</li>
<li><b>Un arabophone :</b> que « keraia » n’évoque pas « karāhiya » (la haine) à l’oreille.</li>
<li><b>Des locuteurs fon, yoruba et goun :</b> aucun sens parasite.</li></ul></div></section>

<section class="wrap sec end"><div class="bet night"><p class="eyebrow">Le nom que je parierais</p><p class="lead">Keraia. C’est le seul mot qui tienne vos cinq fils par un seul objet, la petite corne, et qui reste, en surface, un beau mot grec de studio que personne ne lit comme une église. Son logo n’est pas collé dessus : c’est le mot lui-même, un iota et sa keraia, dessiné.</p></div>
<div class="grid ends"><article><h3 class="eyebrow">La phrase pour vos associés</h3><p class="d3">« Notre i est un iota surmonté d’une corne d’huile : pas un trait ne passera, et c’est lui. »</p></article>
<article><h3 class="eyebrow">Les trois risques qui restent</h3><ol class="vl"><li><b>Prononciation :</b> on hésitera entre « ké-raï-a » et « ké-ré-a » ; il faudra choisir et le dire partout.</li><li><b>Marque :</b> un mot courant en grec moderne (antenne) peut être plus difficile à protéger en Grèce et à Chypre ; la protection portera sur le studio et le logo.</li><li><b>Lecture cachée trop savante :</b> elle ne frissonne que si on la raconte bien ; écrite noir sur blanc dans un livrable public, elle cesserait d’être cachée.</li></ol></article></div></section>
<p class="wrap small src">Sources : <a href="https://www.blueletterbible.org/lexicon/g2762/kjv/tr/ss1/0-1">Blue Letter Bible, G2762 keraia</a> · <a href="https://biblehub.com/greek/2762.htm">Bible Hub, keraia (Thayer)</a> · <a href="https://kaikki.org/dictionary/All%20languages%20combined/meaning/%CE%BA/%CE%BA%CE%B5/%CE%BA%CE%B5%CF%81%CE%B1%CE%AF%CE%B1.html">Wiktionnaire, κεραία</a> · <a href="https://www.blueletterbible.org/sample/lxx/1sa/16/1">Septante, 1 S 16</a> · <a href="https://bibliaparalela.com/bhcv/1_samuel/16.htm">Texte hébreu, 1 S 16:12</a> · <a href="https://biblehub.com/hebrew/strongs_4106.htm">Bible Hub, mahir</a></p>
</main>
<script>
(()=>{{const r=document.documentElement,b=document.getElementById('themeBtn');
const cur=()=>r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
const lab=()=>{{b.textContent=cur()==='dark'?'Thème clair':'Thème sombre'}};
try{{const t=localStorage.getItem('t4');if(t)r.dataset.theme=t}}catch(e){{}}lab();
b.addEventListener('click',()=>{{r.dataset.theme=cur()==='dark'?'light':'dark';lab();try{{localStorage.setItem('t4',r.dataset.theme)}}catch(e){{}}}});}})();
</script>'''
HTML = fr_typo(HTML)
open(os.path.join(HERE, '..', 'nom_v4_keraia.html'), 'w').write(HTML)
print('ok', len(HTML), n, HTML.count('—'))
