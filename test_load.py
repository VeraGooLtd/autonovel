#!/usr/bin/env python3
"""Quick test: load chapters and eval ch1."""
import sys, os
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 1)
os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '.')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/openrouter/owl-alpha'
from dotenv import load_dotenv
load_dotenv('.env')
import evaluate
print('Imported', flush=True)
evaluate.apply_book_dir('/home/dannyryan1980/The-Silent-Strata')
print('Book dir set', flush=True)
layers = evaluate.load_layer_files()
print(f'Layers: {list(layers.keys())}', flush=True)
chapters = evaluate.load_all_chapters(evaluate.CHAPTERS_DIR, evaluate.BOOK_LAYOUT)
print(f'Chapters: {len(chapters)}', flush=True)
print(f'Ch 1: {len(chapters[1])} chars', flush=True)

# Quick eval of ch 1
ch_text = chapters[1]
prompt = f"""Score this SF chapter 1-10. JSON only: {{"score":N,"weakest":"name","fix":"1 sentence"}}

CHAPTER: {ch_text[:1500]}"""

print('Calling judge...', flush=True)
raw = evaluate.call_judge(prompt, max_tokens=500)
print(f'Result: {repr(raw[:200]) if raw else "None"}', flush=True)
