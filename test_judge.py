#!/usr/bin/env python3
"""Test judge model directly."""
import sys, os
os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/nex-agi/nex-n2-pro:free'

from dotenv import load_dotenv
load_dotenv('.env')

from evaluate import call_judge

# Test 1: Simple JSON response
print("Test 1: Simple JSON")
raw = call_judge('Respond with valid JSON: {"test": true}', max_tokens=50)
print(f'Result: {repr(raw)}')

# Test 2: Short eval prompt
print("\nTest 2: Short eval")
raw2 = call_judge('Rate this concept 1-10: A city underground where sound is deadly. Respond with JSON: {"score": N}', max_tokens=100)
print(f'Result: {repr(raw2)}')
