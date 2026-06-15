# D2D Publishing Pipeline — Complete Status

## Model
- **Current**: nvidia/nemotron-3-ultra-550b-a55b:free (550B params, 1M context)
- **Fallback**: google/gemma-4-31b-it:free

## Books Ready for D2D Upload

### Mycoformed Mars Saga (3 books) — Middle Grade SF
| # | Title | EPUB | Words | Price | Metadata |
|---|-------|------|-------|-------|----------|
| 1 | The Genesis Engine | ✓ 70KB | 18,974 | $3.99 | ✓ |
| 2 | The Martian Spore | ✓ 60KB | 16,025 | $3.99 | ✓ |
| 3 | The Crimson Bloom | ✓ 59KB | 15,983 | $3.99 | ✓ |

### Sporefall Cycle (3 books) — YA SF/Horror
| # | Title | EPUB | Words | Price | Metadata |
|---|-------|------|-------|-------|----------|
| 1 | Sporefall | ✓ 106KB | 28,494 | $4.99 | ✓ |
| 2 | Mycelial Tide | ✓ 67KB | 25,947 | $4.99 | ✓ |
| 3 | Mycelial Earth | ✓ 91KB | 24,871 | $4.99 | ✓ |

### Standalone (1 book)
| Title | EPUB | Words | Price | Metadata |
|-------|------|-------|-------|----------|
| Station Zero | ✓ 39KB | 10,909 | $3.99 | ✓ |

### My Dog Is Judging Me (2 books) — Middle Grade Mystery/Humor
| # | Title | EPUB | Words | Doodles | Price | Metadata |
|---|-------|------|-------|---------|-------|----------|
| 1 | The Salami Saboteur | ✓ 56KB | 14,489 | Stripped | $2.99 | ✓ |
| 2 | The Glass Vaults Gambit | ✓ 33KB | 6,718 | Stripped | $2.99 | ✓ |

### Standalone — Near Complete
| Title | EPUB | Words | Status | Price |
|-------|------|-------|--------|-------|
| The Echo Chamber | ✓ 101KB | 51,979 | Near-complete | $3.99 |
| The Silent Strata | ✓ 74KB | 31,982 | In progress | $3.99 |

## D2D Upload Checklist

### Per-Book Requirements
- [ ] EPUB file (generated ✓)
- [ ] Cover image (1600x2400 JPEG) — **NOT YET CREATED**
- [ ] Title
- [ ] Author name (Last, First)
- [ ] Description (HTML supported)
- [ ] Short blurb
- [ ] BISAC codes (1-2)
- [ ] Keywords (up to 7)
- [ ] Price (USD, UK, AU, EU)
- [ ] Distribution channels
- [ ] ISBN (D2D provides free one)

### D2D Account Info
- **Account exists**: Yes (Sporefall Book 1 already published)
- **Login**: draft2digital.com
- **No API available** — must use browser automation

### Distribution Channels
- Apple Books
- Barnes & Noble
- Kobo
- Google Play
- Scribd
- OverDrive
- Axis 360
- Baker & Taylor

## Next Steps

1. **Create cover images** for all books (1600x2400 JPEG minimum)
2. **Login to D2D** and upload books one by one
3. **Fill metadata** from metadata.json files
4. **Set pricing** per marketplace
5. **Publish** and verify on storefronts
6. **Add ISBNs** to backmatter after D2D assigns them
7. **Update website** with purchase links

## File Locations

### EPUBs
```
~/Mycoformed Mars Saga/The-Genesis-Engine.epub
~/Mycoformed Mars Saga/The-Martian-Spore.epub
~/Mycoformed Mars Saga/The-Crimson-Bloom.epub
~/Sporefall/Sporefall.epub
~/Sporefall/Mycelial-Tide.epub
~/Sporefall/Mycelial-Earth.epub
~/StationZero/Station-Zero.epub
~/MY-DOG-IS-JUDGING-ME-/content/books/salami-saboteur/The-Salami-Saboteur.epub
~/MY-DOG-IS-JUDGING-ME-/content/books/the-glass-vaults-gambit/The-Glass-Vaults-Gambit.epub
~/TheEchoChamber/The-Echo-Chamber.epub
~/The-Silent-Strata/The-Silent-Strata.epub
```

### Metadata (with D2D fields)
```
~/Mycoformed Mars Saga/metadata.json (Book 1)
~/Mycoformed Mars Saga/metadata-book2.json (Book 2)
~/Mycoformed Mars Saga/metadata-book3.json (Book 3)
~/Sporefall/metadata.json (Book 1)
~/Sporefall/metadata-book2.json (Book 2)
~/Sporefall/metadata-book3.json (Book 3)
~/StationZero/metadata.json
~/MY-DOG-IS-JUDGING-ME-/content/books/salami-saboteur/metadata.json
~/MY-DOG-IS-JUDGING-ME-/content/books/the-glass-vaults-gambit/metadata.json
~/TheEchoChamber/metadata.json
~/The-Silent-Strata/metadata.json
```

### Scripts
```
~/autonovel/scripts/md_to_epub.py — Markdown to EPUB converter
~/autonovel/scripts/gen_remaining_epubs.py — Batch EPUB generator
~/autonovel/scripts/publish.sh — Publishing helper
~/autonovel/D2D_PIPELINE.md — D2D workflow documentation
~/autonovel/PUBLISHING_STATUS.md — Status tracker
```

## Notes
- All old KDP ISBNs stripped — D2D will assign new ones
- MDIM doodles stripped — publish without illustrations
- No "Coming" dates or "Pre-order" text remaining
- All backmatter says "Available"
- Model: nvidia/nemotron-3-ultra-550b-a55b:free
