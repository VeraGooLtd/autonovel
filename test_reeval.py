#!/usr/bin/env python3
"""Re-evaluate 3 weakest chapters with corrected outline."""
import sys, os, json, re, time
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

# Evaluate chapters 2, 19, 22 (weakest from Phase 2)
test_chapters = [2, 19, 22]

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
        chapter=ch_text  # FULL chapter this time
    )
    
    print(f'\n=== Ch {ch_num} ({len(ch_text)} chars, prompt: {len(prompt)} chars) ===')
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
            sugg = result.get('top_suggestion', '')[:100]
            scores = {k:v for k,v in result.items() if isinstance(v,(int,float))}
            print(f'Score: {overall}/10 ({weakest}) [{elapsed}s]')
            print(f'Scores: {scores}')
            print(f'Suggestion: {sugg}')
        else:
            print(f'Parse failed: {repr(raw[:200])}')
    else:
        print('None')
