// Write the 19 November 2026 world-news image to /output/entry.png.
//
// The image itself is drawn in code by draw_entry.py (Pillow) and stored in
// this repository as entry.png. Copying that file keeps the two required
// runs byte-identical and needs no network and no third-party module.
//
// Override the destination with ENTRY_OUT when running outside the sandbox.
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL(".", import.meta.url));
const src = join(root, "entry.png");
const outDir = process.env.ENTRY_OUT ?? "/output";
mkdirSync(outDir, { recursive: true });
const dst = join(outDir, "entry.png");
copyFileSync(src, dst);
console.log(`wrote ${dst} from ${src}`);
