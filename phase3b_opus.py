#!/usr/bin/env python3
"""Phase 3b: Full manuscript Opus review (split into 2 passes)."""
import sys, os, json, re
from datetime import datetime
from pathlib import Path

os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_BASE_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/openrouter/owl-alpha'

from dotenv import load_dotenv
load_dotenv(Path('/home/dannyryan1980/autonovel/.env'))

import evaluate
BOOK_DIR = '/home/dannyryan1980/The-Silent-Strata'
evaluate.apply_book_dir(BOOK_DIR)

layers = evaluate.load_layer_files()
chapters = evaluate.load_all_chapters(evaluate.CHAPTERS_DIR, evaluate.BOOK_LAYOUT)

# Build chapter summaries (title + first 300 words)
summaries = []
for ch_num in sorted(chapters.keys()):
    ch_text = chapters[ch_num]
    title_line = ''
    for line in ch_text.split('\n')[:10]:
        if '###' in line:
            title_line = line.replace('###', '').strip()
            break
    pov_line = ''
    for line in ch_text.split('\n')[:5]:
        if 'Viewpoint' in line:
            pov_line = line.replace('*', '').replace('Viewpoint:', '').strip()
            break
    excerpt = ' '.join(ch_text[:300].split())
    summaries.append(f"Ch {ch_num} [{pov_line}] — {title_line}:\n{excerpt}")

full_summary = '\n\n'.join(summaries)

outline = layers.get('outline', '')[:2500]
characters = layers.get('characters', '')[:1500]
world = layers.get('world', '')[:1000]

# Pass 1: Narrative structure
PROMPT1 = """Senior editor review of a 26-chapter SF novel. Score 1-10 (6=draft; 7=good; 8=publishable with polish).

OUTLINE: {outline}

CHAPTER SUMMARIES (first 300 words each):
{summaries}

Score:
- narrative_arc: Three-act structure? Climax earned? Ending satisfies?
- pacing: Where does it drag/rush? Unnecessary chapters?
- thematic_coherence: Central theme consistent?
- pov_structure: Rotating POV work? Any weak POV characters?
- structural_issues: Wrong chapter order? Missing/redundant scenes?

JSON: {{"narrative_arc":N,"pacing":N,"thematic_coherence":N,"pov_structure":N,"structural_issuesN,"narrative_notes":"2-3 sentences","top_3_narrative_fixes":["fix1","fix2","fix3"]}}"""

# Pass 2: Character, world, prose
PROMPT2 = """Senior editor review of a 26-chapter SF novel. Score 1-10.

CHARACTERS: {characters}
WORLD: {world}

CHAPTER SUMMARIES:
{summaries}

Score:
- character_arcs: Each POV character have complete arc? Flat characters?
- world_integration: World woven into narrative or exposition-heavy?
- dialogue: Distinct voices? Generic dialogue?
- prose_quality: Overall prose. Consistent weaknesses?

JSON: {{"character_arcs":N,"world_integration":N,"dialogue":N,"prose_quality":N,"character_notes":"2-3 sentences","top_3_character_fixes":["fix1","fix2","fix3"]}}"""

print('=== Pass 1: Narrative Structure ===')
p1 = PROMPT1.format(outline=outline, summaries=full_summary)
print(f'Prompt: {len(p1)} chars')
raw1 = evaluate.call_judge(p1, max_tokens=1500)
result1 = None
if raw1:
    result1 = evaluate.parse_json_response(raw1)
    if not result1:
        m = re.search(r'\{.*\}', raw1, re.DOTALL)
        if m:
            try: result1 = json.loads(m.group())
            except: pass
    if result1:
        print(f'Scores: { {k:v for k,v in result1.items() if isinstance(v,(int,float))} }')
        print(f'Notes: {result1.get("narrative_notes","")[:200]}')
        fixes = result1.get("top_3_narrative_fixes", [])
        for i, fix in enumerate(fixes, 1):
            print(f'  Fix {i}: {fix}')
    else:
        print(f'Parse failed: {repr(raw1[:200])}')
else:
    print('None')

print('\n=== Pass 2: Character, World, Prose ===')
p2 = PROMPT2.format(characters=characters, world=world, summaries=full_summary)
print(f'Prompt: {len(p2)} chars')
raw2 = evaluate.call_judge(p2, max_tokens=1500)
result2 = None
if raw2:
    result2 = evaluate.parse_json_response(raw2)
    if not result2:
        m = re.search(r'\{.*\}', raw2, re.DOTALL)
        if m:
            try: result2 = json.loads(m.group())
            except: pass
    if result2:
        print(f'Scores: { {k:v for k,v in result2.items() if isinstance(v,(int,float))} }')
        print(f'Notes: {result2.get("character_notes","")[:200]}')
        fixes = result2.get("top_3_character_fixes", [])
        for i, fix in enumerate(fixes, 1):
            print(f'  Fix {i}: {fix}')
    else:
        print(f'Parse failed: {repr(raw2[:200])}')
else:
    print('None')

# Merge
if result1 and result2:
    merged = {**result1, **result2}
    all_scores = [v for k,v in merged.items() if isinstance(v,(int,float))]
    merged['overall_score'] = round(sum(all_scores)/len(all_scores), 1) if all_scores else 0
    
    print(f'\n=== OVERALL: {merged["overall_score"]}/10 ===')
    
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    out_dir = Path(BOOK_DIR) / 'audit'
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f'phase3b_opus_{ts}.json'
    with open(out_file, 'w') as f:
        json.dump(merged, f, indent=2)
    print(f'Saved: {out_file}')
