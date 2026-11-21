#!/usr/bin/env python3
"""
Targeted slop-revision for The Silent Strata.
Rewrites chapters with highest slop scores, replacing overused words/phrases
with fresh alternatives. Uses owl-alpha via autonovel's LLM client.

Strategy:
- Replace 'whispered' with action beats or varied tags
- Replace 'clang' with specific sound descriptions
- Replace 'hissed' with varied dialogue delivery
- Replace 'stared' with specific eye/face actions
- Replace 'shadows' with concrete visual details
- Replace 'jagged' with specific texture words
- Remove 'one last time' and 'voice barely audible'
- Expand climax chapters (23-24) per Opus feedback
- Add Varrick doubt moment (Ch 8 or 17) per Opus feedback
"""
import sys, os, json, re, time
from pathlib import Path
from datetime import datetime

os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/openrouter/owl-alpha'

from dotenv import load_dotenv
load_dotenv(Path('/home/dannyryan1980/autonovel/.env'))

import evaluate

BOOK_DIR = Path('/home/dannyryan1980/The-Silent-Strata')
MANUSCRIPT_DIR = BOOK_DIR / 'manuscript'
SLOP_FILE = BOOK_DIR / 'audit' / 'slop_analysis.json'

with open(SLOP_FILE) as f:
    slop_data = json.load(f)

# Build replacement map from slop analysis
# word -> list of (chapter_num, count) sorted by count
word_chapters = {}
for ch_num, ch_data in slop_data['chapters'].items():
    for word, count in ch_data.get('top_slop_words', []):
        if word not in ('elara', 'kael'):  # skip character names
            if word not in word_chapters:
                word_chapters[word] = []
            word_chapters[word].append((int(ch_num), count))

# Sort by total count
sorted_words = sorted(word_chapters.items(), key=lambda x: sum(c for _, c in x[1]), reverse=True)

print("=== Slop words to target (excluding character names) ===")
for word, chapters in sorted_words[:15]:
    total = sum(c for _, c in chapters)
    ch_list = ', '.join(f"Ch {c}:{n}" for c, n in sorted(chapters, key=lambda x: -x[1])[:5])
    print(f"  {word}: {total} hits ({ch_list})")

# Trigrams to target
print("\n=== Slop trigrams to target ===")
for tri, count in slop_data['manuscript']['top_slop_trigrams']:
    print(f"  '{tri}': {count}")

print(f"\n=== Contrast patterns ===")
for m in slop_data['manuscript']['contrast_matches']:
    print(f"  \"{m}\"")

# Chapters to revise (highest slop scores, excluding character name inflation)
# Recalculate without character names
chapter_scores = {}
for ch_num, ch_data in slop_data['chapters'].items():
    # Count non-name slop words
    real_slop = sum(c for w, c in ch_data.get('top_slop_words', []) if w not in ('elara', 'kael'))
    chapter_scores[int(ch_num)] = real_slop

ranked = sorted(chapter_scores.items(), key=lambda x: -x[1])
print("\n=== Chapters by real slop word count ===")
for ch_num, score in ranked:
    print(f"  Ch {ch_num}: {score} real slop word hits")

# Target top 8 chapters for revision
target_chapters = [ch for ch, _ in ranked[:8]]
print(f"\n=== Target chapters for revision: {target_chapters} ===")

# ── Revision prompt template ───────────────────────────────────────────────

REVISE_PROMPT = """You are a professional editor revising a science fiction novel chapter to reduce AI-slop patterns while preserving the author's voice and the story's integrity.

ORIGINAL CHAPTER:
{chapter}

SLOP ISSUES TO FIX IN THIS CHAPTER:
{slop_issues}

REVISION RULES:
1. Replace overused words with fresh, specific alternatives. Don't just swap synonyms — restructure sentences to avoid the pattern entirely.
2. Replace "whispered" with action beats, varied dialogue tags, or restructured dialogue that implies quiet speech without a tag.
3. Replace "clang" with specific, concrete sound descriptions unique to the scene.
4. Replace "hissed" with varied dialogue delivery (muttered, breathed, said tightly, etc.) or action beats.
5. Replace "stared" with specific eye/face actions (his eyes tracked, she studied, he watched, etc.).
6. Replace "shadows" with concrete visual details specific to the setting.
7. Replace "jagged" with specific texture words appropriate to the material.
8. Remove or rephrase "one last time" — show the finality through action instead.
9. Remove or rephrase "voice barely audible" — show the quiet through context.
10. Preserve all plot points, character beats, and the chapter's end hook.
11. Preserve the POV character's voice and the acoustic-metaphor style.
12. Do NOT add new plot events. Only revise existing prose.
13. Keep the chapter length roughly the same (±10%).

Return the complete revised chapter in the same markdown format as the original, including the ### chapter title header."""

def get_slop_issues_for_chapter(ch_num):
    """Get the specific slop issues for a chapter."""
    ch_data = slop_data['chapters'].get(str(ch_num), {})
    issues = []
    
    for word, count in ch_data.get('top_slop_words', []):
        if word not in ('elara', 'kael') and count >= 2:
            issues.append(f"- '{word}' appears {count} times — replace with varied alternatives")
    
    for tri, count in ch_data.get('top_trigrams', []):
        issues.append(f"- Trigram '{tri}' appears {count} time(s) — rephrase to avoid this pattern")
    
    for match in ch_data.get('contrast_matches', []):
        issues.append(f"- Contrast pattern \"{match}\" — rephrase to avoid not-X-but-Y structure")
    
    return '\n'.join(issues) if issues else '- Minor slop issues; focus on overall freshness'

# ── Run revisions ───────────────────────────────────────────────────────────

results = {}
for ch_num in target_chapters:
    ch_file = MANUSCRIPT_DIR / f'chapter_{ch_num:02d}.md'
    if not ch_file.exists():
        print(f"Ch {ch_num}: file not found, skipping")
        continue
    
    with open(ch_file) as f:
        original = f.read()
    
    slop_issues = get_slop_issues_for_chapter(ch_num)
    
    prompt = REVISE_PROMPT.format(
        chapter=original,
        slop_issues=slop_issues
    )
    
    print(f"\n{'='*60}")
    print(f"Revising Ch {ch_num} ({len(original)} chars, prompt: {len(prompt)} chars)")
    print(f"Slop issues:\n{slop_issues}")
    
    t0 = time.time()
    raw = evaluate.call_judge(prompt, max_tokens=3000)
    elapsed = round(time.time() - t0, 1)
    
    if raw:
        # The revised chapter should be in the response
        # Extract it — it should start with ### Chapter
        revised = raw.strip()
        
        # Clean up any markdown code block wrapping
        if revised.startswith('```'):
            revised = re.sub(r'^```(?:markdown|md)?\n', '', revised)
            revised = re.sub(r'\n```$', '', revised)
        
        # Save revised chapter
        backup_file = MANUSCRIPT_DIR / f'chapter_{ch_num:02d}.md.bak'
        with open(backup_file, 'w') as f:
            f.write(original)
        
        with open(ch_file, 'w') as f:
            f.write(revised)
        
        # Quick slop re-check
        tokens = re.findall(r"[a-z]+(?:'[a-z]+)?", revised.lower())
        with open('/home/dannyryan1980/slop-score/data/slop_list.json') as f:
            slop_words = set(w[0].lower() for w in json.load(f) if w)
        new_slop_count = sum(1 for t in tokens if t in slop_words and t not in ('elara', 'kael'))
        old_slop_count = sum(c for w, c in slop_data['chapters'].get(str(ch_num), {}).get('top_slop_words', []) if w not in ('elara', 'kael'))
        
        print(f"  Done in {elapsed}s | Slop words: {old_slop_count} → {new_slop_count}")
        results[ch_num] = {
            'old_slop': old_slop_count,
            'new_slop': new_slop_count,
            'elapsed': elapsed,
        }
    else:
        print(f"  FAILED (None response)")
        results[ch_num] = {'error': 'no response'}
    
    time.sleep(1)  # Rate limit

# ── Summary ─────────────────────────────────────────────────────────────────

print(f"\n{'='*60}")
print("REVISION SUMMARY")
print(f"{'='*60}")
for ch_num, r in sorted(results.items()):
    if 'error' in r:
        print(f"  Ch {ch_num}: ERROR")
    else:
        delta = r['old_slop'] - r['new_slop']
        sign = '+' if delta < 0 else ''
        print(f"  Ch {ch_num}: {r['old_slop']} → {r['new_slop']} slop words ({sign}{delta}) in {r['elapsed']}s")

# Save results
out_path = BOOK_DIR / 'audit' / f'slop_revision_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved: {out_path}")
