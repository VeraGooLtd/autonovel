#!/usr/bin/env python3
"""Use LLM to generate high-quality SVG doodles."""
import os
import subprocess
import json

output_dir = os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg_v2")
os.makedirs(output_dir, exist_ok=True)

# The doodle descriptions
doodles = [
    ("ch01_sticky_sadness.svg", "STICKY SADNESS", "A bowl of lumpy oatmeal with a frowny face drawn on the side. Steam rising as tiny fists. Include: wood grain table surface, cereal box, detailed bowl with inner shadow, oatmeal lumps with texture, frowny face with angry eyebrows and teeth, 3 steam fists with motion lines, spilled oats on table, spoon in bowl, decorative swirl and heart doodles in corners, arrow with label pointing to bowl."),
    ("ch02_column_of_shame.svg", "COLUMN OF SHAME", "A tall ancient Roman stone column with a child's juice box balanced on top. A tiny ginger cat sitting on the juice box looking proud. Include: detailed column with marble texture and cracks, fluting lines, decorative capital with scrollwork, juice box with OJ label and straw, ginger cat with crown and whiskers, annoyed bird on branch with thought bubble, ancient statue in background, speech bubble."),
    ("ch03_mud_trail.svg", "THE EVIDENCE", "A trail of messy paw-shaped mud blobs leading into a dark stone archway. Include: stone archway with cracks and dark interior, 4+ detailed paw prints of decreasing size with mud splatters, detective hand holding magnifying glass, clue tag label, arrow with label, small beetle, grass tufts."),
    ("ch04_cat_salami_jetpack.svg", "SALAMI JETPACK", "A tiny ginger cat with a jetpack made of a giant salami strapped to its back, flying over a picnic. Include: salami with fat marbling and ties, detailed cat with open screaming mouth and whiskers, straps with buckle, exhaust trail with smoke puffs, clouds in sky, tiny people on ground looking up with speech bubble, speed lines."),
    ("ch05_ledger.svg", "FELINE LEDGER", "A close-up of a secret ledger page with columns for FAT CONTENT % and DIGNITY INDEX. Include: paper with spiral binding, title text, column headers, multiple data entries (Salami 98% MAX, Tuna 85% HIGH, Cheese 72% MED, Kibble 2% ZERO), horizontal rules, cat paw print stamp, more lines."),
    ("ch06_pigeon_spy.svg", "FEATHERED FRANK", "A disheveled pigeon perched on a rusted park fence, staring intensely. Wearing a tiny spy hat. Include: detailed fence with peeling paint, pigeon with one wide eye and one squint, tiny spy hat, sweat drops, speech bubble with intel, crumbs on fence, park bench in background, arrow with label."),
    ("ch07_lulu_chaos.svg", "LULU CHAOS", "A 5-year-old girl spinning in circles with ice-cream on her face, toys flying everywhere. Include: kitchen background with cabinets, Lulu with messy pigtails and spiral eyes, ice cream smeared on face, flying objects (ice cream cone, banana, cookie, apple), motion lines, Mummy in corner with clipboard, spilled milk puddle."),
    ("ch08_henry_ride.svg", "SIR HENRY", "A very majestic horse with a tiny girl and bulldog on its back. The horse has a superhero cape. Include: Big Mud Flats terrain with mud puddles, Henry with muscular body and arched neck, flowing superhero cape with star pattern, Bea riding with determined face, Barnaby tucked in front looking worried, parents' broken-down car in background, signpost."),
    ("ch09_mud_crosssection.svg", "MUD SCIENCE", "A cross-section diagram of mud layers. Include: outer frame, three layers (SLIME with bubbles, MYSTERY GOOP with wavy lines, CLUE with paw print and hair strand), depth markers on left side, Bea's hand with magnifying glass, arrow pointing down, small note in corner."),
    ("ch10_sub_salami.svg", "SALAMI SUB", "A cross-section of a tiny submarine. The Salami is in the pilot seat wearing goggles. Include: submarine hull with conning tower and periscope, front viewport with light beam, Salami pilot in goggles at controls, control panel with buttons, depth gauge, bubbles rising, surprised fish swimming by."),
]

# Save prompts
for filename, caption, description in doodles:
    prompt = f"""Create a detailed SVG doodle in Diary of a Wimpy Kid style for "{caption}".

Description: {description}

STYLE RULES:
- viewBox="0 0 400 400"
- Thin black pencil lines (stroke-width 1.5-3)
- Childlike hand-drawn quality — slightly wobbly lines are GOOD
- No solid fills — only outlines and simple shapes
- Black lines only on transparent background
- Use stroke-linecap="round" for friendly rounded ends
- Include many visual elements, textures, small details
- Add the caption text at the bottom in Comic Sans style
- Make it look like a 9-year-old's notebook doodle

Generate ONLY the SVG code. No explanation, no markdown code fences. Start with <?xml and end with </svg>."""

    prompt_file = os.path.join(output_dir, f"prompt_{filename.replace('.svg', '.txt')}")
    with open(prompt_file, 'w') as f:
        f.write(prompt)

print(f"Generated {len(doodles)} prompt files in {output_dir}")
print("Next: Process each prompt through LLM to generate SVG")
