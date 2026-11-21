#!/usr/bin/env python3
"""Test judge with actual Silent Strata content."""
import sys, os
os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/nex-agi/nex-n2-pro:free'

from dotenv import load_dotenv
load_dotenv('.env')

from evaluate import call_judge, parse_json_response, load_layer_files, apply_book_dir

apply_book_dir('/home/dannyryan1980/The-Silent-Strata')
layers = load_layer_files()

# Use very short truncation
truncated = {k: (v[:400] if v and len(v) > 400 else v) for k, v in layers.items()}

prompt = f"""Evaluate this SF novel's worldbuilding. Score each dimension 1-10.

WORLD: {truncated.get('world', '')}

CANON: {truncated.get('canon', '')}

OUTLINE: {truncated.get('outline', '')}

Score these dimensions (1-10 each):
- technology_rules: Hard rules with costs/limitations
- world_history: Timeline creating present-day tensions
- geography_culture: Distinct locations with sensory signatures
- lore_interconnection: How systems connect to each other
- iceberg_depth: Ratio of visible to implied depth

Respond with valid JSON only:
{{"technology_rules": N, "world_history": N, "geography_culture": N, "lore_interconnection": N, "iceberg_depth": N, "biggest_gap": "...", "top_improvement": "..."}}"""

print(f'Prompt length: {len(prompt)} chars')
raw = call_judge(prompt, max_tokens=800)
print(f'Raw length: {len(raw) if raw else 0}')
print(f'Raw: {repr(raw[:500]) if raw else "None"}')

if raw:
    result = parse_json_response(raw)
    if result:
        print(f'Parsed: {json.dumps(result, indent=2)}')
    else:
        print('Parse failed')
        # Try to find JSON in the response
        import re
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            print(f'Found JSON: {m.group()}')
