#!/usr/bin/env python3
"""Test: evaluate chapter 1 only."""
import sys, os, json, re
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
print(f'Judge model: {evaluate.JUDGE_MODEL}')
print(f'Chapters: {len(chapters)}')

# Get chapter 1
ch_text = chapters[1]
print(f'Ch 1 length: {len(ch_text)} chars')

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

ch_outline = ' '.join(chapter_outlines.get(1, []))[:500]
print(f'Outline: {ch_outline[:200]}')

t = {
    'voice': layers.get('voice', '')[:400],
    'world': layers.get('world', '')[:600],
    'characters': layers.get('characters', '')[:500],
}

prompt = f"""Evaluate this SF novel chapter. Score 1-10 (err low; 6=competent draft; 7=does something generic AI wouldn't; 8=human editor keeps with minor notes).

VOICE:
{t['voice']}

WORLD (key rules):
{t['world']}

CHARACTERS:
{t['characters']}

OUTLINE FOR THIS CHAPTER:
{ch_outline}

THIS CHAPTER (first 2500 words):
{ch_text[:2500]}

Score each 1-10:
- voice_adherence: Prose matches voice definition? Sentence rhythm variation?
- beat_coverage: All outline beats hit? Dramatized or summarized?
- character_voice: Dialogue distinct per character? Sounds like speech not prose?
- world_consistency: Any lore violations?
- emotional_authenticity: Emotions shown not told? Matches character psychology?
- pacing: Chapter moves? Where does it drag?
- prose_quality: Sentence rhythm variation? Specific word choice? Any AI slop?
- engagement: Would you keep turning pages?

JSON only:
{{"voice_adherence":N,"beat_coverage":N,"character_voice":N,"world_consistency":N,"emotional_authenticity":N,"pacing":N,"prose_quality":N,"engagement":N,"overall_score":N,"weakest_dimension":"name","top_suggestion":"1 sentence fix"}}"""

print(f'Prompt length: {len(prompt)} chars (~{len(prompt)//4} tokens)')
print('Calling judge...')
raw = evaluate.call_judge(prompt, max_tokens=1000)
print(f'Response length: {len(raw) if raw else 0}')
if raw:
    result = evaluate.parse_json_response(raw)
    if result:
        print(f'Score: {result.get("overall_score", "N/A")}/10')
        print(f'Weakest: {result.get("weakest_dimension", "")}')
        print(f'Suggestion: {result.get("top_suggestion", "")}')
        print(f'All scores: { {k:v for k,v in result.items() if isinstance(v,(int,float))} }')
    else:
        print(f'Parse failed: {repr(raw[:300])}')
else:
    print('None')
