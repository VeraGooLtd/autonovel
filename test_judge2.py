#!/usr/bin/env python3
"""Test judge model with various prompts."""
import sys, os
os.chdir('/home/dannyryan1980/autonovel')
sys.path.insert(0, '/home/dannyryan1980/autonovel')
os.environ['AUTONOVEL_API_BASE_URL'] = 'http://localhost:20128/v1'
os.environ['AUTONOVEL_API_KEY'] = 'local'
os.environ['AUTONOVEL_JUDGE_MODEL'] = 'openrouter/nex-agi/nex-n2-pro:free'

from dotenv import load_dotenv
load_dotenv('.env')

from evaluate import call_judge

# Test 3: Eval prompt with higher max_tokens
print("Test 3: Eval prompt, high max_tokens")
raw3 = call_judge(
    'Rate this concept 1-10 and explain why in 2 sentences: A city underground where sound is deadly. End with JSON: {"score": N, "reason": "..."}',
    max_tokens=500
)
print(f'Result: {repr(raw3)}')

# Test 4: Even simpler
print("\nTest 4: Very simple")
raw4 = call_judge(
    'What is 2+2? Answer in JSON: {"answer": 4}',
    max_tokens=200
)
print(f'Result: {repr(raw4)}')

# Test 5: The actual foundation prompt style but tiny
print("\nTest 5: Foundation-style prompt")
raw5 = call_judge(
    '''Evaluate this world concept. Score 1-10.

WORLD: An underground city where sound can cause earthquakes.

Respond with JSON: {{"score": N, "gap": "...", "improvement": "..."}}''',
    max_tokens=500
)
print(f'Result: {repr(raw5)}')
