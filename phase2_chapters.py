#!/usr/bin/env python3
"""Phase 2: Evaluate all 26 chapters with log file output."""
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

LOG_FILE = '/home/dannyryan1980/The-Silent-Strata/audit/phase2_progress.log'

def log(msg):
    ts = datetime.now().strftime('%H:%M:%S')
    line = f'[{ts}] {msg}'
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')

log('Starting Phase 2')
evaluate.apply_book_dir('/home/dannyryan1980/The-Silent-Strata')
layers = evaluate.load_layer_files()
chapters = evaluate.load_all_chapters(evaluate.CHAPTERS_DIR, evaluate.BOOK_LAYOUT)
log(f'Loaded {len(chapters)} chapters, layers: {list(layers.keys())}')
log(f'Judge: {evaluate.JUDGE_MODEL}')

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
    return ' '.join(lines)[:500] if lines else 'No outline'

PROMPT_TMPL = """Evaluate this SF novel chapter. Score 1-10 (6=competent draft; 7=above average; 8=editor keeps with minor notes).

VOICE: {voice}
WORLD: {world}
CHARACTERS: {characters}
OUTLINE: {chapter_outline}
PREV CHAPTER END: {prev_tail}

CHAPTER: {chapter_text}

JSON only: {{"voice_adherence":N,"beat_coverage":N,"character_voice":N,"world_consistency":N,"emotional_authenticity":N,"pacing":N,"prose_quality":N,"engagement":N,"overall_score":N,"weakest_dimension":"name","top_suggestion":"1 sentence"}}"""

t = {
    'voice': layers.get('voice', '')[:400],
    'world': layers.get('world', '')[:600],
    'characters': layers.get('characters', '')[:500],
}

results = {}
ch_list = sorted(chapters.keys())
total = len(ch_list)

for i, ch_num in enumerate(ch_list):
    ch_text = chapters[ch_num]
    prev_tail = ""
    if i > 0:
        prev_text = chapters[ch_list[i-1]]
        prev_tail = prev_text[-300:] if len(prev_text) > 300 else prev_text

    prompt = PROMPT_TMPL.format(
        voice=t['voice'], world=t['world'], characters=t['characters'],
        chapter_outline=get_outline(ch_num),
        prev_tail=prev_tail[-300:],
        chapter_text=ch_text[:2500]
    )

    t0 = time.time()
    raw = evaluate.call_judge(prompt, max_tokens=800)
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
            log(f'Ch {ch_num:2d}/{total}: {overall}/10 ({weakest}) [{elapsed}s]')
            results[ch_num] = result
        else:
            log(f'Ch {ch_num:2d}/{total}: PARSE FAIL [{elapsed}s]')
            results[ch_num] = {'overall_score': 0, 'error': 'parse_fail'}
    else:
        log(f'Ch {ch_num:2d}/{total}: NONE [{elapsed}s]')
        results[ch_num] = {'overall_score': 0, 'error': 'no_response'}

# Summary
scored = {k:v for k,v in results.items() if v.get('overall_score', 0) > 0}
if scored:
    scores_list = [v['overall_score'] for v in scored.values()]
    avg = round(sum(scores_list)/len(scores_list), 1)
    below_6 = sorted([k for k,v in scored.items() if v['overall_score'] < 6])
    log(f'\n=== SUMMARY ===')
    log(f'Evaluated: {len(scored)}/{total}')
    log(f'Average: {avg}/10')
    log(f'Below 6.0: {below_6 if below_6 else "none"}')
    for ch_num in sorted(scored.keys()):
        v = scored[ch_num]
        log(f'  Ch {ch_num:2d}: {v["overall_score"]}/10 [{v.get("weakest_dimension","?")}] {v.get("top_suggestion","")[:60]}')

ts = datetime.now().strftime('%Y%m%d_%H%M%S')
out_file = Path('/home/dannyryan1980/The-Silent-Strata/audit') / f'phase2_chapters_{ts}.json'
with open(out_file, 'w') as f:
    json.dump(results, f, indent=2)
log(f'Saved: {out_file}')
