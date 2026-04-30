"""
remap_images.py
---------------
Reorganises the GTZAN images_original/ folder from 10 genre subfolders
into 3 super-genre subfolders (Acoustic / Rhythmic / Electric).
 
Before:
    images_original/
        blues/          classical/      jazz/
        country/        reggae/         rock/       hiphop/
        disco/          pop/            metal/
 
After:
    images_remapped/
        Acoustic/       (blues, classical, jazz)
        Rhythmic/       (country, reggae, rock, hiphop)
        Electric/       (disco, pop, metal)
 
The original folder is NOT modified — files are copied, not moved.
"""
 
import shutil
from pathlib import Path
 
# ── Mapping: genre folder name → super-genre group ───────────────────────────
GENRE_TO_GROUP = {
    # Acoustic
    'blues'    : 'Acoustic',
    'classical': 'Acoustic',
    'jazz'     : 'Acoustic',
    # Rhythmic
    'country'  : 'Rhythmic',
    'reggae'   : 'Rhythmic',
    'rock'     : 'Rhythmic',
    'hiphop'   : 'Rhythmic',
    # Electric
    'disco'    : 'Electric',
    'pop'      : 'Electric',
    'metal'    : 'Electric',
}
 
# ── Paths — adjust if your folder is somewhere else ──────────────────────────
SOURCE_DIR = Path('images_original')
TARGET_DIR = Path('images_remapped')
 
# ── Sanity check ─────────────────────────────────────────────────────────────
if not SOURCE_DIR.exists():
    raise FileNotFoundError(
        f"Could not find '{SOURCE_DIR}'. "
        "Make sure you run this script from the directory that contains images_original/."
    )
 
# ── Create target subfolders ──────────────────────────────────────────────────
for group in set(GENRE_TO_GROUP.values()):
    (TARGET_DIR / group).mkdir(parents=True, exist_ok=True)
 
# ── Copy files ────────────────────────────────────────────────────────────────
counts = {group: 0 for group in set(GENRE_TO_GROUP.values())}
skipped = []
 
for genre_folder in SOURCE_DIR.iterdir():
    if not genre_folder.is_dir():
        continue
 
    genre = genre_folder.name.lower()
 
    if genre not in GENRE_TO_GROUP:
        print(f"  [SKIP] Unknown genre folder: '{genre_folder.name}' — not in mapping.")
        skipped.append(genre_folder.name)
        continue
 
    group = GENRE_TO_GROUP[genre]
 
    for img_file in genre_folder.iterdir():
        if img_file.suffix.lower() not in {'.png', '.jpg', '.jpeg'}:
            continue
 
        # Prefix filename with genre so names stay unique across groups
        # e.g.  blues.00000.png  (already unique in GTZAN, but explicit is safer)
        dest = TARGET_DIR / group / img_file.name
        shutil.copy2(img_file, dest)
        counts[group] += 1
 
# ── Summary ───────────────────────────────────────────────────────────────────
print("\n✓ Remapping complete!")
print(f"  Source : {SOURCE_DIR.resolve()}")
print(f"  Target : {TARGET_DIR.resolve()}")
print()
print("  Images per group:")
for group, n in sorted(counts.items()):
    print(f"    {group:<10} {n:>4} images")
 
total = sum(counts.values())
print(f"\n  Total copied : {total}")
 
if skipped:
    print(f"\n  ⚠ Skipped folders: {skipped}")
else:
    print("  No folders were skipped.")
 
