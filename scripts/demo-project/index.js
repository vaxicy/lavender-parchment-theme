// Lavender Parchment Theme — quiet lavender, parchment and warm beige
import { readFile } from 'node:fs/promises';

const PAPER_PALETTE = {
  lavender: '#CCC2D1',
  parchment: '#F6F1E5',
  beige: '#D6BEB3',
  violet: '#826F95',
};

export class LavenderParchment {
  constructor(name = 'Morning sky') {
    this.name = name;
    this.colors = Object.values(PAPER_PALETTE);
  }

  /** Blend two colors into a soft parchment-inspired shade. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) => [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channels = a.map((value, i) => Math.round(value * (1 - ratio) + b[i] * ratio));
    return '#' + channels.map((value) => value.toString(16).padStart(2, '0')).join('');
  }

  async describe(file) {
    const content = await readFile(file, 'utf8');
    return { name: this.name, colors: this.colors, content };
  }
}

const cloud = new LavenderParchment();
console.log(cloud.blend(PAPER_PALETTE.lavender, PAPER_PALETTE.parchment));
