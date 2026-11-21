#!/usr/bin/env python3
"""Debug: test lore prompt directly."""
import sys, os
os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/nex-agi/nex-n2-pro:free'

from dotenv import load_dotenv
load_dotenv('.env')

from evaluate import call_judge, load_layer_files, apply_book_dir

apply_book_dir('/home/dannyryan1980/The-Silent-Strata')
layers = load_layer_files()

# Test with JUST world (no outline)
world_short = layers.get('world', '')[:600]
canon_short = layers.get('canon', '')[:500]

prompt = f"""Evaluate this SF worldbuilding. Score 1-10.

WORLD: {world_short}

CANON: {canon_short}

Score: technology_rules, world_history, geography_culture, lore_interconnection, iceberg_depth.

JSON: {{"technology_rules":N,"world_history":N,"geography_culture":N,"lore_interconnection":N,"iceberg_depth":N,"gap":"1 sentence","fix":"1 sentence"}}"""

print(f'Prompt: {len(prompt)} chars')
raw = call_judge(prompt, max_tokens=1200)
print(f'Raw length: {len(raw) if raw else 0}')
print(f'Raw: {repr(raw[:500]) if raw else "None"}')
