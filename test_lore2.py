#!/usr/bin/env python3
"""Debug: test lore prompt with outline."""
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

# Test with world + canon + outline (Acts I only)
world_short = layers.get('world', '')[:600]
canon_short = layers.get('canon', '')[:500]
outline_short = layers.get('outline', '')[:1500]  # Just Act I

prompt = f"""Evaluate this SF novel's worldbuilding. Score each dimension 1-10.

SCORING: 9-10=Published quality. 7-8=Strong. 5-6=Thin. 3-4=Sketchy. Err low.

WORLD: {world_short}

CANON: {canon_short}

OUTLINE: {outline_short}

Score (1-10):
- technology_rules: Hard rules with costs/limits. Can climax use ONLY established rules?
- world_history: Timeline creating present-day tensions.
- geography_culture: Distinct locations, cultures generating conflict.
- lore_interconnection: How tech/history/geography connect.
- iceberg_depth: Visible vs implied depth.

Check for INTERNAL CONTRADICTIONS.

JSON only: {{"technology_rules":N,"world_history":N,"geography_culture":N,"lore_interconnection":N,"iceberg_depth":N,"lore_gap":"1 sentence","lore_fix":"1 sentence"}}"""

print(f'Prompt: {len(prompt)} chars (~{len(prompt)//4} tokens)')
raw = call_judge(prompt, max_tokens=1200)
print(f'Raw length: {len(raw) if raw else 0}')
if raw:
    import json, re
    m = re.search(r'\{.*\}', raw, re.DOTALL)
    if m:
        try:
            result = json.loads(m.group())
            print(f'Scores: { {k:v for k,v in result.items() if isinstance(v,(int,float))} }')
            print(f'Gap: {result.get("lore_gap","")}')
        except Exception as e:
            print(f'JSON parse error: {e}')
            print(f'Raw: {repr(raw[:500])}')
    else:
        print(f'No JSON found. Raw: {repr(raw[:300])}')
else:
    print('None')
