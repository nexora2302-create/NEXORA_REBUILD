import { fr } from './fr'
import { Reveal, SplitWords } from './reveal'
import { ScrollRise } from './scroll-rise'
import { SpotGrid } from './spot-grid'

type Expertise = {
  word: string
  title: string
  line: string
  items: string[]
}

const VOIR: Expertise = {
  word: 'Voir',
  title: 'Communication visuelle',
  line: 'Des identités qui se reconnaissent au premier regard, déclinées sur chaque support.',
  items: ['Identité de marque', 'Direction artistique', 'Supports de communication', 'Campagnes'],
}
const BOUGER: Expertise = {
  word: 'Bouger',
  title: 'Motion design et audiovisuel',
  line: 'Des images qui respirent et des marques qui prennent vie à l’écran.',
  items: ['Logos animés', 'Motion design', 'Vidéos promotionnelles', 'Contenus audiovisuels'],
}
const HABITER: Expertise = {
  word: 'Habiter',
  title: 'Création web',
  line: 'Des sites rapides, sensibles et mémorables, du premier écran à la maintenance.',
  items: ['Sites vitrines', 'Landing pages', 'E-commerce', 'UI/UX design', 'Développement et maintenance'],
}

function Copy({ x }: { x: Expertise }) {
  return (
    <div>
      <h3 className="t-card">
        <span aria-hidden>
          {x.word}
          <span className="text-accent">.</span>
        </span>
        <span className="sr-only">
          {x.word}. {x.title}
        </span>
      </h3>
      <p className="mt-4 font-serif text-2xl italic md:text-[1.7rem]">{x.title}</p>
      <p className="mt-2 max-w-md text-[17px] leading-relaxed text-foreground/80">{fr(x.line)}</p>
      <ul className="mt-6 flex flex-wrap gap-2">
        {x.items.map((it) => (
          <li key={it} className="rounded-full border border-line px-3.5 py-1.5 text-[14px] text-foreground/85">
            {it}
          </li>
        ))}
      </ul>
    </div>
  )
}

/* Voir : une marque se construit (tracé, formes, palette) */
function VizVoir() {
  const swatches = ['#0d0c0b', '#ece5d8', '#ff4a1c', '#7a2410']
  return (
    <svg viewBox="0 0 400 240" className="viz h-full w-full" aria-hidden>
      <g stroke="rgb(236 229 216 / 0.08)" strokeWidth="1">
        {Array.from({ length: 9 }).map((_, i) => (
          <line key={`v${i}`} x1={40 + i * 40} y1="0" x2={40 + i * 40} y2="240" />
        ))}
        {Array.from({ length: 5 }).map((_, i) => (
          <line key={`h${i}`} x1="0" y1={40 + i * 40} x2="400" y2={40 + i * 40} />
        ))}
      </g>
      <g fill="none" stroke="#ece5d8" strokeWidth="1.5">
        <circle className="viz-draw" pathLength={1} cx="140" cy="110" r="70" />
        <rect className="viz-draw" pathLength={1} x="140" y="40" width="140" height="140" style={{ animationDelay: '0.3s' }} />
        <path className="viz-draw" pathLength={1} d="M70 180 L280 40" style={{ animationDelay: '0.6s' }} />
      </g>
      <circle className="viz-pop" cx="140" cy="110" r="22" fill="#ff4a1c" />
      <rect className="viz-pop" x="210" y="110" width="70" height="70" fill="#ece5d8" style={{ animationDelay: '0.2s' }} />
      {swatches.map((c, i) => (
        <rect
          key={c}
          className="viz-pop"
          x={300 + (i % 2) * 44}
          y={60 + Math.floor(i / 2) * 44}
          width="36"
          height="36"
          rx="6"
          fill={c}
          stroke="rgb(236 229 216 / 0.25)"
          style={{ animationDelay: `${0.35 + i * 0.12}s` }}
        />
      ))}
    </svg>
  )
}

/* Bouger : une timeline, ses images clés et la tête de lecture */
function VizBouger() {
  const tracks = [
    [0.08, 0.42, 0.78],
    [0.2, 0.6],
    [0.12, 0.34, 0.66, 0.9],
  ]
  const x0 = 24
  const w = 352
  return (
    <svg viewBox="0 0 400 240" className="viz h-full w-full" aria-hidden>
      <g>
        <circle className="viz-ball" cx="44" cy="56" r="14" fill="#ff4a1c" style={{ '--travel': '300px' } as React.CSSProperties} />
        <path d="M24 92 C 140 92, 220 20, 376 20" fill="none" stroke="rgb(236 229 216 / 0.25)" strokeDasharray="3 5" />
      </g>
      {tracks.map((keys, t) => {
        const y = 128 + t * 34
        return (
          <g key={t}>
            <rect x={x0} y={y - 11} width={w} height="22" rx="6" fill="rgb(236 229 216 / 0.05)" />
            {keys.map((k) => (
              <rect
                key={k}
                className="viz-key"
                x={x0 + k * w - 6}
                y={y - 6}
                width="12"
                height="12"
                transform={`rotate(45 ${x0 + k * w} ${y})`}
                stroke="#ece5d8"
                strokeWidth="1.5"
                fill="transparent"
                style={{ '--at': `${k * 5}s` } as React.CSSProperties}
              />
            ))}
          </g>
        )
      })}
      <g className="viz-playhead" style={{ '--track': `${w}px` } as React.CSSProperties}>
        <line x1={x0} y1="108" x2={x0} y2="232" stroke="#ff4a1c" strokeWidth="1.5" />
        <path d={`M${x0 - 6} 104 h12 l-6 7 z`} fill="#ff4a1c" />
      </g>
    </svg>
  )
}

/* Habiter : une page qui se compose puis défile */
function VizHabiter() {
  const blocks: [number, number, number, number, string, number][] = [
    [32, 28, 120, 10, '#ece5d8', 0.1],
    [380, 26, 96, 14, 'rgb(236 229 216 / 0.2)', 0.2],
    [32, 74, 300, 30, '#ece5d8', 0.35],
    [32, 112, 220, 30, '#ece5d8', 0.45],
    [32, 160, 110, 32, '#ff4a1c', 0.6],
    [300, 150, 176, 150, '#7a2410', 0.7],
    [32, 230, 240, 8, 'rgb(236 229 216 / 0.3)', 0.85],
    [32, 248, 200, 8, 'rgb(236 229 216 / 0.3)', 0.9],
    [32, 320, 444, 120, 'rgb(236 229 216 / 0.08)', 1],
    [32, 460, 210, 90, 'rgb(236 229 216 / 0.08)', 1.1],
    [266, 460, 210, 90, 'rgb(236 229 216 / 0.08)', 1.15],
  ]
  return (
    <svg viewBox="0 0 520 320" className="viz h-full w-full" aria-hidden>
      <rect x="1" y="1" width="518" height="318" rx="14" fill="#0d0c0b" stroke="rgb(236 229 216 / 0.18)" />
      <g fill="rgb(236 229 216 / 0.3)">
        <circle cx="20" cy="18" r="4" />
        <circle cx="34" cy="18" r="4" />
        <circle cx="48" cy="18" r="4" fill="#ff4a1c" />
      </g>
      <line x1="1" y1="36" x2="519" y2="36" stroke="rgb(236 229 216 / 0.12)" />
      <svg x="0" y="37" width="520" height="282" viewBox="0 0 520 282">
        <g className="viz-scroll">
          {blocks.map(([x, y, w, h, fill, at], i) => (
            <rect
              key={i}
              className="viz-block"
              x={x}
              y={y}
              width={w}
              height={h}
              rx={h > 28 ? 8 : h / 2}
              fill={fill}
              style={{ '--at': `${at * 0.6}s` } as React.CSSProperties}
            />
          ))}
        </g>
      </svg>
    </svg>
  )
}

export function Expertises() {
  const tile = 'spot relative overflow-hidden rounded-[1.75rem] p-6 md:p-9'
  return (
    <section id="expertises" aria-labelledby="expertises-title" className="relative px-4 py-28 md:px-8 md:py-36">
      <Reveal className="mb-12 grid gap-6 md:mb-16 md:grid-cols-12 md:items-end">
        <h2 id="expertises-title" className="t-section md:col-span-8">
          <SplitWords text="Trois métiers," />
          <SplitWords text="un seul mouvement." offset={2} />
        </h2>
        <p className="max-w-sm text-[17px] leading-relaxed text-foreground/80 md:col-span-4">
          L’identité donne le ton, le mouvement donne le rythme, le web donne la scène. Séparément ou ensemble.
        </p>
      </Reveal>

      <SpotGrid className="rise-stage grid gap-4 md:grid-cols-12">
        <ScrollRise className="md:col-span-7">
          <Reveal as="article" className={`${tile} flex h-full flex-col gap-8`}>
            <div className="aspect-[5/3] overflow-hidden rounded-2xl bg-background/60">
              <VizVoir />
            </div>
            <Copy x={VOIR} />
          </Reveal>
        </ScrollRise>

        <ScrollRise className="md:col-span-5" delay={0.12}>
          <Reveal as="article" className={`${tile} flex h-full flex-col gap-8`}>
            <div className="aspect-[5/3] overflow-hidden rounded-2xl bg-background/60">
              <VizBouger />
            </div>
            <Copy x={BOUGER} />
          </Reveal>
        </ScrollRise>

        <ScrollRise className="md:col-span-12">
          <Reveal as="article" className={`${tile} grid items-center gap-8 md:grid-cols-12`}>
            <div className="md:col-span-5">
              <Copy x={HABITER} />
            </div>
            <div className="overflow-hidden rounded-2xl md:col-span-7">
              <VizHabiter />
            </div>
          </Reveal>
        </ScrollRise>
      </SpotGrid>
    </section>
  )
}
