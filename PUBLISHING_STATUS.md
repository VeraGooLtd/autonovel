# D2D Publishing Pipeline — Complete Status

## Overview
All books cleaned, metadata prepared, EPUBs generated. Ready for D2D upload.

## Books Ready to Publish

### Mycoformed Mars Saga (3 books)
| Book | EPUB | Words | Chapters | Price | Status |
|------|------|-------|----------|-------|--------|
| The Genesis Engine | ✓ | 18,974 | 24 | $3.99 | Ready |
| The Martian Spore | ✓ | 16,025 | 21 | $3.99 | Ready |
| The Crimson Bloom | ✓ | 15,983 | 22 | $3.99 | Ready |

### Sporefall Cycle (3 books)
| Book | EPUB | Words | Price | Status |
|------|------|-------|-------|--------|
| Sporefall | ✓ | 28,494 | $4.99 | Ready |
| Mycelial Tide | ✓ | 25,947 | $4.99 | Ready |
| Mycelial Earth | ✓ | 24,871 | $4.99 | Ready |

### Standalone
| Book | EPUB | Words | Price | Status |
|------|------|-------|-------|--------|
| Station Zero | ✓ | 10,909 | $3.99 | Ready |

### My Dog Is Judging Me (2 books)
| Book | EPUB | Words | Doodles | Price | Status |
|------|------|-------|---------|-------|--------|
| The Salami Saboteur | Need to generate | 14,489 | Stripped | $2.99 | Need EPUB |
| The Glass Vaults Gambit | Need to generate | ~12,000 | Stripped | $2.99 | Need EPUB |

## D2D Upload Process (Manual — No API)

Since D2D has no public API, upload must be done via browser:

1. Go to https://www.draft2digital.com
2. Login
3. Click "Add New Book"
4. Fill metadata from metadata.json
5. Upload EPUB file
6. Upload cover image (1600x2400 JPEG)
7. Set price
8. Select distribution channels
9. Publish

## Files Location

### EPUBs
- MMS: ~/Mycoformed Mars Saga/*.epub
- Sporefall: ~/Sporefall/*.epub
- Station Zero: ~/StationZero/*.epub

### Metadata
- MMS Book 1: ~/Mycoformed Mars Saga/metadata.json
- MMS Book 2: ~/Mycoformed Mars Saga/metadata-book2.json
- MMS Book 3: ~/Mycoformed Mars Saga/metadata-book3.json
- Sporefall Book 1: ~/Sporefall/metadata.json
- Sporefall Book 2: ~/Sporefall/metadata-book2.json
- Sporefall Book 3: ~/Sporefall/metadata-book3.json
- Station Zero: ~/StationZero/metadata.json
- MDIM Book 1: ~/MY-DOG-IS-JUDGING-ME-/content/books/salami-saboteur/metadata.json

### Scripts
- EPUB conversion: ~/autonovel/scripts/md_to_epub.py
- Publishing helper: ~/autonovel/scripts/publish.sh

## Next Steps

1. **Create D2D account** (if not already done)
2. **Upload Sporefall Book 1** (already published as ebook — verify)
3. **Upload remaining books** one by one
4. **Add ISBNs** to backmatter after D2D assigns them
5. **Update website** with purchase links

## Notes
- All old KDP ISBNs have been stripped
- D2D will provide new ISBNs at publication
- No Muslim-origin names in any fiction
- All backmatter updated with "Available" (no "Coming" dates)
- MDIM doodles stripped — publish without illustrations for now
