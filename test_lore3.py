#!/usr/bin/env python3
"""Debug: find what causes None."""
import sys, os
os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/nex-agi/nex-n2-pro:free'

from dotenv import load_dotenv
load_dotenv('.env')

from evaluate import call_judge, load_layer_files, apply_book_dir
import json

apply_book_dir('/home/dannyryan1980/The-Silent-Strata')
layers = load_layer_files()

# Test: world only (no outline)
w = layers.get('world', '')[:400]
c = layers.get('canon', '')[:300]
o = layers.get('outline', '')[:800]

# Minimal prompt
prompt = f"""Score this SF world 1-10.

WORLD: {w}
CANON: {c}
OUTLINE: {o}

JSON: {{"tech":N,"history":N,"geo":N,"lore":N,"iceberg":N}}"""

print(f'Prompt: {len(prompt)} chars')
print(f'World snippet: {repr(w[:100])}')
raw = call_judge(prompt, max_tokens=500)
print(f'Result: {repr(raw[:300]) if raw else "None"}')

# Now test with the scoring instructions
prompt2 = f"""Evaluate this SF novel's worldbuilding. Score each dimension 1-10.

SCORING CALIBRATION:
9-10: Published-novel quality.
7-8: Strong. Skilled author could draft with minimal invention.
5-6: Functional but thin.
3-4: Sketchy. More questions than answers.
1-2: Placeholder.
Err toward lower scores.

WORLD: {w}
CANON: {c}
OUTLINE: {o}

Score: technology_rules, world_history, geography_culture, lore_interconnection, iceberg_depth.

JSON: {{"technology_rules":N,"world_history":N,"geography_culture":N,"lore_interconnection":N,"iceberg_depth":N,"gap":"1 sentence","fix":"1 sentence"}}"""

print(f'\nPrompt2: {len(prompt2)} chars')
raw2 = call_judge(prompt2, max_tokens=800)
print(f'Result2: {repr(raw2[:300]) if raw2 else "None"}')
