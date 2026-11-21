#!/usr/bin/env python3
"""Phase 1: Run foundation eval v6 - more content, better balance."""
import sys, os, json, re
from datetime import datetime
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
print(f'Layers: {list(layers.keys())}')
print(f'Chapters: {len(chapters)}')

# Key insight: the judge needs to see FULL character sheets for all POV characters
# and the FULL outline. We'll send more content by being more selective.

# For lore: world (tech rules section only) + canon + outline Acts I-II
world_tech = '\n'.join([l for l in layers.get('world','').split('\n') if 'Sound Physics' in l or 'Technology Costs' in l or 'Liquefaction' in l or 'Resonance' in l or 'Echo-Doubling' in l or 'Fungal' in l or 'Helm' in l or 'Chladni' in l or 'Sönn-Hvísl' in l or 'The Bell' in l])
t = {
    'world_tech': world_tech[:1500],
    'canon': layers.get('canon', '')[:800],
    'outline_i_ii': layers.get('outline', '')[:2500],  # Acts I + II
    'outline_iii': layers.get('outline', '')[-1500:],  # Act III
    'characters': layers.get('characters', '')[:2000],  # More character content
    'voice': layers.get('voice', '')[:500],
}

# ---- Part 1: Lore ----
lore_prompt = f"""Evaluate this SF novel's worldbuilding. Score 1-10 (err low; 8+ = zero gaps).

SCORING: 9-10=Published quality. 7-8=Strong. 5-6=Thin. 3-4=Sketchy. 1-2=Placeholder.

WORLD (technology and physics):
{t['world_tech']}

CANON (facts, rules, timeline):
{t['canon']}

OUTLINE (Acts I-II):
{t['outline_i_ii']}

OUTLINE (Act III):
{t['outline_iii']}

Score:
- technology_rules: Hard rules with costs/limits. Can climax be resolved using ONLY established rules?
- world_history: Timeline creating present-day tensions.
- geography_culture: Distinct locations, conflict-generating cultures.
- lore_interconnection: How tech/history/geography connect.
- iceberg_depth: Visible vs implied depth.

Check for INTERNAL CONTRADICTIONS.

JSON only:
{{"technology_rules":N,"world_history":N,"geography_culture":N,"lore_interconnection":N,"iceberg_depth":N,"lore_gap":"biggest gap","lore_fix":"specific fix"}}"""

# ---- Part 2: Character ----
char_prompt = f"""Evaluate this SF novel's characters and structure. Score 1-10 (err low; 8+ = zero gaps).

SCORING: 9-10=Published quality. 7-8=Strong. 5-6=Thin. 3-4=Sketchy. 1-2=Placeholder.

CHARACTERS (all POV and major characters):
{t['characters']}

VOICE:
{t['voice']}

OUTLINE (Acts I-II):
{t['outline_i_ii']}

OUTLINE (Act III):
{t['outline_iii']}

Score:
- character_depth: Wound/want/need/lie/arc for each major character? Specific and consequential?
- character_distinctiveness: Can you tell characters apart by goals, voice, methods?
- character_secrets: Secrets with plot consequences?
- outline_completeness: All major scenes/beats? Three acts clear? Foreshadowing tracked?
- foreshadowing_balance: Planted elements pay off. No deus ex machina.
- internal_consistency: No contradictions. Convenient gaps vs deliberate mystery?

JSON only:
{{"character_depth":N,"character_distinctiveness":N,"character_secrets":N,"outline_completeness":N,"foreshadowing_balance":N,"internal_consistency":N,"char_gap":"biggest gap","char_fix":"specific fix"}}"""

print(f'Lore prompt: {len(lore_prompt)} chars')
print(f'Char prompt: {len(char_prompt)} chars')

def run_part(name, prompt, mt=1200):
    print(f'\n--- {name} ---')
    raw = evaluate.call_judge(prompt, max_tokens=mt)
    if not raw:
        print('None'); return None
    result = evaluate.parse_json_response(raw)
    if not result:
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            try: result = json.loads(m.group())
            except: pass
    if result:
        scores = {k:v for k,v in result.items() if isinstance(v,(int,float))}
        print(f'Scores: {scores}')
        for k in result:
            if 'gap' in k or 'fix' in k:
                print(f'  {k}: {result[k]}')
    else:
        print(f'Parse failed: {repr(raw[:200])}')
    return result

result1 = run_part('Lore', lore_prompt)
result2 = run_part('Character', char_prompt)

if result1 and result2:
    merged = {**result1, **result2}
    scores = [v for k, v in merged.items() if isinstance(v, (int, float))]
    overall = round(sum(scores) / len(scores), 1) if scores else 0
    merged['overall'] = overall
    
    print(f'\n=== FOUNDATION SCORE: {overall}/10 ===')
    for k, v in sorted(merged.items()):
        print(f'  {k}: {v}')
    
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    out_dir = Path(BOOK_DIR) / 'audit'
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f'phase1_foundation_{ts}.json'
    with open(out_file, 'w') as f:
        json.dump(merged, f, indent=2)
    print(f'\nSaved: {out_file}')
else:
    print(f'\nPartial: result1={bool(result1)}, result2={bool(result2)}')
