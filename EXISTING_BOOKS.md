# Applying Autonovel to Existing Books

This guide explains how to use the autonovel pipeline's evaluation and revision tools on manuscripts that are already written (not generated from scratch).

## Overview

The autonovel pipeline has four phases:
1. **Foundation** — world, characters, outline (skip for existing books)
2. **Drafting** — write chapters (skip for existing books)
3. **Revision** — evaluate, edit, rewrite (USE THIS)
4. **Export** — typeset, generate art, audiobook (USE THIS)

For existing books, we only need **Phase 3 (Revision)** and **Phase 4 (Export)**.

## Setup

```bash
cd ~/autonovel
cp .env.example .env
# Add your Anthropic API key to .env
uv sync
```

## Per-Book Process

### Step 1: Prepare the manuscript

Each book needs its chapters in a `chapters/` directory. For single-file manuscripts, split into chapters:

```bash
# Create a branch for the book
git checkout -b autonovel/mycoformed-mars-1

# Create chapters directory
mkdir chapters

# Copy your book file(s) into the repo
cp "~/Mycoformed Mars Saga/Mycoformed Mars Book 1. The Genesis Engine 5 x 8 in Published.docx.md" manuscript.md

# Split into individual chapter files (manual or scripted)
# Each file should be named: ch01.md, ch02.md, etc.
```

### Step 2: Run evaluation

```bash
# Score the whole novel
uv run python evaluate.py --full

# Score individual chapters
uv run python evaluate.py --chapter=1
uv run python evaluate.py --chapter=5
```

This produces slop scores, banned word hits, AI tell detection, and structural analysis.

### Step 3: Adversarial editing

```bash
# Find suggested cuts across all chapters
uv run python adversarial_edit.py all

# Apply specific cut types
uv run python apply_cuts.py all --types OVER-EXPLAIN REDUNDANT
```

### Step 4: Reader panel evaluation

Requires Anthropic API key.

```bash
# 4-persona full-novel evaluation
uv run python reader_panel.py
```

### Step 5: Opus review loop

Requires Anthropic API key.

```bash
# Deep prose-level dual-persona review
uv run python review.py
```

### Step 6: Generate revision briefs and rewrite

```bash
# Auto-generate revision briefs from feedback
uv run python gen_brief.py --auto

# Rewrite specific chapters from briefs
uv run python gen_revision.py 5 briefs/ch05.md
```

### Step 7: Export

```bash
# Generate ePub
uv run python run_pipeline.py --phase export

# Generate audiobook (requires ELEVENLABS_API_KEY)
uv run python gen_audiobook_script.py
uv run python gen_audiobook.py

# Generate cover art (requires FAL_KEY)
uv run python gen_art.py style
uv run python gen_art.py curate cover --n=6
```

## Books to Process

### Priority 1: Published books (ebook first)
These are already published and need to go through D2D as ebooks first.

1. **Mycoformed Mars Saga Book 1** — The Genesis Engine
2. **Mycoformed Mars Saga Book 2** — The Martian Spore
3. **Mycoformed Mars Saga Book 3** — The Crimson Bloom
4. **Sporefall Book 1** — Sporefall
5. **Sporefall Book 2** — Mycelial Tide
6. **Sporefall Book 3** — Mycelial Earth
7. **Station Zero**
8. **The Salami Saboteur** (MDIM Book 1)

### Priority 2: Near-complete books
9. **The Glass Vaults Gambit** (MDIM Book 2)
10. **The Echo Chamber**

### Priority 3: In-progress books
11. **The Silent Strata**

## Checklist Per Book

- [ ] All old ISBNs stripped
- [ ] No "Coming 2025" or "Pre-order" text
- [ ] Character names consistent across series
- [ ] Backmatter added (About the Author + Also by)
- [ ] Slop evaluation run (evaluate.py --full)
- [ ] Adversarial cuts applied
- [ ] Reader panel completed
- [ ] Revision briefs generated
- [ ] Chapters rewritten from briefs
- [ ] Final evaluation score > 7.0
- [ ] ePub exported
- [ ] Cover art generated
- [ ] Audiobook script generated
- [ ] New ISBNs added (from D2D)
