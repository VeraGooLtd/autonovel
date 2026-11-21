#!/usr/bin/env python3
"""Check chapter key format."""
import sys, os
os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/openrouter/owl-alpha'
from dotenv import load_dotenv
load_dotenv('.env')
import evaluate
evaluate.apply_book_dir('/home/dannyryan1980/The-Silent-Strata')
chapters = evaluate.load_all_chapters(evaluate.CHAPTERS_DIR, evaluate.BOOK_LAYOUT)
print('Keys:', list(chapters.keys())[:10])
print('Type of first key:', type(list(chapters.keys())[0]))
print('First key value:', repr(list(chapters.keys())[0]))
