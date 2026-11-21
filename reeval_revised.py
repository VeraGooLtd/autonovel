#!/usr/bin/env python3
"""Re-evaluate revised chapters 8, 10, 23, 24 with autonovel."""
import sys, os, json, re, time
from datetime import datetime
from pathlib import Path

os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/openrouter/owl-alpha'

from dotenv import load_dotenv
load_dotenv(Path('/home/dannyryan1980/autonovel/.env'))

import evaluate
BOOK_DIR = '/home/dannyryan1980/The-Silent-Strata'
evaluate.apply_book_dir(BOOK_DIR)

layers = evaluate.load_layer_files()
chapters = evaluate.load_all_chapters(evaluate.CHAPTERS_DIR, evaluate.BOOK_LAYOUT)

# Build outline lookup
outline_text = layers.get('outline', '')
chapter_outlines = {}
current_ch = None
for line in outline_text.split('\n'):
    ch_match = re.match(r'### Chapter (\d+):', line)
    if ch_match:
        current_ch = int(ch_match.group(1))
        chapter_outlines[current_ch] = []
    elif current_ch and line.strip():
        chapter_outlines[current_ch].append(line.strip())

def get_outline(ch_num):
    lines = chapter_outlines.get(ch_num, [])
    return '\n'.join(lines)[:800] if lines else 'No outline'

t = {
    'voice': layers.get('voice', '')[:500],
    'world': layers.get('world', '')[:800],
    'characters': layers.get('characters', '')[:600],
}

PROMPT = """Evaluate this SF novel chapter. Score 1-10 (6=competent; 7=above average; 8=editor keeps).

VOICE: {voice}
WORLD: {world}
CHARACTERS: {characters}
OUTLINE: {outline}
PREV CHAPTER END: {prev}

FULL CHAPTER:
{chapter}

JSON: {{"voice_adherence":N,"beat_coverage":N,"character_voice":N,"world_consistency":N,"emotional_authenticity":N,"pacing":N,"prose_quality":N,"engagement":N,"overall_score":N,"weakest_dimension":"name","top_suggestion":"1 sentence"}}"""

ch_list = sorted(chapters.keys())
test_chapters = [8, 10, 23, 24]

# Load previous scores for comparison
prev_scores_path = Path(BOOK_DIR) / 'audit' / 'phase2_chapters_20260615_201616.json'
if prev_scores_path.exists():
    with open(prev_scores_path) as f:
        prev_data = json.load(f)
    prev_scores = {int(k): v for k, v in prev_data.get('chapters', {}).items()}
else:
    prev_scores = {}

results = {}
for ch_num in test_chapters:
    if ch_num not in chapters:
        print(f'Ch {ch_num}: not found')
        continue
    
    i = ch_list.index(ch_num)
    ch_text = chapters[ch_num]
    prev_tail = ""
    if i > 0:
        prev_text = chapters[ch_list[i-1]]
        prev_tail = prev_text[-400:] if len(prev_text) > 400 else prev_text
    
    prompt = PROMPT.format(
        voice=t['voice'], world=t['world'], characters=t['characters'],
        outline=get_outline(ch_num),
        prev=prev_tail,
        chapter=ch_text
    )
    
    prev_score = prev_scores.get(ch_num, {}).get('overall_score', '?')
    print(f'\n=== Ch {ch_num} (prev: {prev_score}/10) ===')
    t0 = time.time()
    raw = evaluate.call_judge(prompt, max_tokens=1200)
    elapsed = round(time.time() - t0, 1)
    
    if raw:
        result = evaluate.parse_json_response(raw)
        if not result:
            m = re.search(r'\{.*\}', raw, re.DOTALL)
            if m:
                try: result = json.loads(m.group())
                except: pass
        if result:
            overall = result.get('overall_score', 0)
            weakest = result.get('weakest_dimension', '')
            sugg = result.get('top_suggestion', '')[:120]
            scores = {k:v for k,v in result.items() if isinstance(v,(int,float))}
            print(f'Score: {overall}/10 (was {prev_score}) [{elapsed}s]')
            print(f'Scores: {scores}')
            print(f'Weakest: {weakest}')
            print(f'Suggestion: {sugg}')
            results[ch_num] = result
        else:
            print(f'Parse failed: {repr(raw[:200])}')
    else:
        print('None')
    
    time.sleep(1)

# Summary
print(f'\n{"="*60}')
print('REVISION RESULTS SUMMARY')
print(f'{"="*60}')
for ch_num in test_chapters:
    if ch_num in results and ch_num in prev_scores:
        old = prev_scores[ch_num].get('overall_score', '?')
        new = results[ch_num].get('overall_score', '?')
        delta = ''
        if isinstance(old, (int, float)) and isinstance(new, (int, float)):
            d = new - old
            delta = f' ({d:+.1f})'
        print(f'  Ch {ch_num}: {old} → {new}{delta}')

# Save
ts = datetime.now().strftime('%Y%m%d_%H%M%S')
out_path = Path(BOOK_DIR) / 'audit' / f'reeval_{ts}.json'
with open(out_path, 'w') as f:
    json.dump(results, f, indent=2)
print(f'\nSaved: {out_path}')
