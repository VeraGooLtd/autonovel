#!/usr/bin/env python3
"""Run foundation eval with owl-alpha judge and save results."""
import json
import os
import sys

# Override judge model before importing evaluate
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/openrouter/owl-alpha'

from evaluate import apply_book_dir, load_layer_files, call_judge, parse_json_response, FOUNDATION_PROMPT

BOOK_DIR = '/home/dannyryan1980/MY-DOG-IS-JUDGING-ME-/content/books/the-sentinel-ridge-showdown'
OUT_PATH = '/home/dannyryan1980/MY-DOG-IS-JUDGING-ME-/content/books/the-sentinel-ridge-showdown/eval_results/foundation_postfix.json'

os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

apply_book_dir(BOOK_DIR)
layers = load_layer_files()

# Truncate layers to keep prompt manageable
truncated = {}
for k, v in layers.items():
    truncated[k] = v[:2000] if len(v) > 2000 else v

prompt = FOUNDATION_PROMPT.format(**truncated)
print(f'Prompt length: {len(prompt)} chars, ~{len(prompt)//4} tokens')

raw = call_judge(prompt, max_tokens=4000)
if raw is None:
    print('ERROR: call_judge returned None')
    sys.exit(1)

result = parse_json_response(raw)
with open(OUT_PATH, 'w') as f:
    json.dump(result, f, indent=2)
print(f'Saved to {OUT_PATH}')
print(json.dumps(result, indent=2))
