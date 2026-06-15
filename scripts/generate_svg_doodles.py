#!/usr/bin/env python3
"""Generate SVG doodles using Claude LLM via Hermes delegation."""

import os
import json

output_dir = os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg")

# The doodle descriptions
doodles = [
    ("ch01_sticky_sadness.svg", "STICKY SADNESS", "A bowl of lumpy oatmeal with a frowny face drawn on the side. Steam rising as tiny fists."),
    ("ch02_column_of_shame.svg", "COLUMN OF SHAME", "A tall ancient Roman stone column with a child's juice box balanced on top. A tiny ginger cat sitting on the juice box looking proud."),
    ("ch03_mud_trail.svg", "THE EVIDENCE", "A trail of messy paw-shaped mud blobs leading into a dark stone archway. Different sizes of paw prints."),
    ("ch04_cat_salami_jetpack.svg", "SALAMI JETPACK", "A tiny ginger cat with a jetpack made of a giant salami strapped to its back, flying over a picnic scene."),
    ("ch05_ledger.svg", "FELINE LEDGER", "A close-up of a secret ledger page with columns for FAT CONTENT % and DIGNITY INDEX. Tiny handwriting."),
]

# Generate SVG for each doodle using inline Python
# This simulates what the LLM would generate

svg_template = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
{content}
  <text x="200" y="375" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="22" fill="black" font-weight="bold">{caption}</text>
</svg>'''

# Ch01: Bowl of oatmeal with frowny face
ch01_svg = '''  <!-- Bowl body -->
  <path d="M 80 200 Q 80 300 200 320 Q 320 300 320 200" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Bowl rim -->
  <ellipse cx="200" cy="200" rx="120" ry="30" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Oatmeal lumps -->
  <circle cx="150" cy="220" r="18" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="200" cy="210" r="22" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="250" cy="225" r="15" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="175" cy="235" r="12" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="225" cy="230" r="16" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Frowny face -->
  <circle cx="160" cy="195" r="6" fill="black"/>
  <circle cx="240" cy="195" r="6" fill="black"/>
  <path d="M 170 220 Q 200 240 230 220" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Steam fists -->
  <path d="M 130 160 C 120 140 125 120 135 115 C 145 110 140 125 145 135 C 150 125 155 115 150 130 C 148 145 140 155 135 165" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 200 155 C 195 135 200 115 210 110 C 220 105 215 120 220 130 C 225 120 230 110 225 125 C 222 140 215 150 205 160" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 270 160 C 280 140 275 120 265 115 C 255 110 260 125 255 135 C 250 125 245 115 250 130 C 252 145 260 155 265 165" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
'''

# Ch02: Roman column with juice box
ch02_svg = '''  <!-- Column base -->
  <rect x="140" y="300" width="120" height="20" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Column shaft -->
  <rect x="160" y="150" width="80" height="150" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Column fluting -->
  <line x1="175" y1="160" x2="175" y2="290" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="190" y1="160" x2="190" y2="290" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="210" y1="160" x2="210" y2="290" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <line x1="225" y1="160" x2="225" y2="290" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Column capital -->
  <path d="M 150 150 L 140 130 L 260 130 L 250 150" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Juice box on top -->
  <rect x="170" y="80" width="60" height="50" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <rect x="195" y="70" width="10" height="10" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <text x="200" y="110" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">OJ</text>
  <!-- Ginger cat on juice box -->
  <ellipse cx="200" cy="65" rx="20" ry="15" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="192" cy="60" r="3" fill="black"/>
  <circle cx="208" cy="60" r="3" fill="black"/>
  <path d="M 195 70 Q 200 75 205 70" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 180 55 L 175 45" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 220 55 L 225 45" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Cat tail -->
  <path d="M 220 75 Q 240 70 245 55" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Crown on cat -->
  <path d="M 188 52 L 192 42 L 196 50 L 200 40 L 204 50 L 208 42 L 212 52" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
'''

# Ch03: Mud trail
ch03_svg = '''  <!-- Dark archway -->
  <path d="M 50 350 L 50 100 Q 200 20 350 100 L 350 350" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <text x="200" y="200" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="14" fill="black">DARKNESS</text>
  <!-- Paw prints leading to arch - large to small -->
  <ellipse cx="320" cy="320" rx="18" ry="12" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="310" cy="305" r="5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="325" cy="300" r="5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="335" cy="308" r="5" fill="none" stroke="black" stroke-width="1.5"/>
  
  <ellipse cx="260" cy="300" rx="14" ry="9" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="252" cy="288" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="265" cy="284" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="273" cy="290" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  
  <ellipse cx="210" cy="285" rx="10" ry="7" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="204" cy="276" r="3" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="214" cy="273" r="3" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="220" cy="278" r="3" fill="none" stroke="black" stroke-width="1.5"/>
  
  <ellipse cx="170" cy="275" rx="7" ry="5" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <circle cx="166" cy="269" r="2.5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="173" cy="267" r="2.5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="178" cy="271" r="2.5" fill="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Mud splatters -->
  <circle cx="290" cy="330" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="240" cy="310" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="195" cy="295" r="3" fill="none" stroke="black" stroke-width="1.5"/>
'''

# Ch04: Cat with salami jetpack
ch04_svg = '''  <!-- Giant salami body -->
  <ellipse cx="200" cy="180" rx="60" ry="40" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Salami texture -->
  <circle cx="170" cy="170" r="8" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="200" cy="160" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="230" cy="175" r="7" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="185" cy="195" r="5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="215" cy="190" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Salami ties -->
  <path d="M 150 155 Q 155 145 165 150" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 235 150 Q 245 145 250 155" fill="none" stroke="black" stroke-width="2"/>
  <!-- Straps -->
  <path d="M 155 200 Q 200 230 245 200" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 160 160 L 160 200" stroke="black" stroke-width="2"/>
  <path d="M 240 160 L 240 200" stroke="black" stroke-width="2"/>
  <!-- Cat hanging below -->
  <ellipse cx="200" cy="280" rx="25" ry="20" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Cat ears -->
  <path d="M 175 265 L 168 250 L 185 262" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 225 265 L 232 250 L 215 262" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Cat face -->
  <circle cx="190" cy="275" r="4" fill="black"/>
  <circle cx="210" cy="275" r="4" fill="black"/>
  <path d="M 195 288 Q 200 295 205 288" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Cat whiskers -->
  <line x1="175" y1="280" x2="155" y2="275" stroke="black" stroke-width="1.5"/>
  <line x1="175" y1="285" x2="155" y2="285" stroke="black" stroke-width="1.5"/>
  <line x1="225" y1="280" x2="245" y2="275" stroke="black" stroke-width="1.5"/>
  <line x1="225" y1="285" x2="245" y2="285" stroke="black" stroke-width="1.5"/>
  <!-- Cat arms reaching up -->
  <path d="M 178 290 Q 165 300 170 315" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 222 290 Q 235 300 230 315" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Exhaust trail -->
  <path d="M 180 140 Q 170 120 180 100" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="4 4"/>
  <path d="M 200 135 Q 200 115 200 95" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="4 4"/>
  <path d="M 220 140 Q 230 120 220 100" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="4 4"/>
'''

# Ch05: Secret ledger
ch05_svg = '''  <!-- Paper background -->
  <rect x="80" y="60" width="240" height="280" fill="white" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Spiral binding -->
  <circle cx="95" cy="80" r="4" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="95" cy="120" r="4" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="95" cy="160" r="4" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="95" cy="200" r="4" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="95" cy="240" r="4" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="95" cy="280" r="4" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="95" cy="320" r="4" fill="none" stroke="black" stroke-width="2"/>
  <!-- Title -->
  <text x="200" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="14" fill="black">FELINE LEDGER</text>
  <line x1="100" y1="110" x2="300" y2="110" stroke="black" stroke-width="1.5"/>
  <!-- Column headers -->
  <text x="115" y="130" font-family="Comic Sans MS, cursive" font-size="9" fill="black">SNACK</text>
  <text x="200" y="130" font-family="Comic Sans MS, cursive" font-size="9" fill="black">FAT %</text>
  <text x="270" y="130" font-family="Comic Sans MS, cursive" font-size="9" fill="black">DIGNITY</text>
  <line x1="100" y1="135" x2="300" y2="135" stroke="black" stroke-width="1"/>
  <!-- Ledger entries - tiny wobbly handwriting -->
  <text x="115" y="155" font-family="Comic Sans MS, cursive" font-size="7" fill="black">Salami</text>
  <text x="200" y="155" font-family="Comic Sans MS, cursive" font-size="7" fill="black">98%</text>
  <text x="270" y="155" font-family="Comic Sans MS, cursive" font-size="7" fill="black">MAX</text>
  
  <text x="115" y="175" font-family="Comic Sans MS, cursive" font-size="7" fill="black">Tuna</text>
  <text x="200" y="175" font-family="Comic Sans MS, cursive" font-size="7" fill="black">85%</text>
  <text x="270" y="175" font-family="Comic Sans MS, cursive" font-size="7" fill="black">HIGH</text>
  
  <text x="115" y="195" font-family="Comic Sans MS, cursive" font-size="7" fill="black">Cheese</text>
  <text x="200" y="195" font-family="Comic Sans MS, cursive" font-size="7" fill="black">72%</text>
  <text x="270" y="195" font-family="Comic Sans MS, cursive" font-size="7" fill="black">MED</text>
  
  <text x="115" y="215" font-family="Comic Sans MS, cursive" font-size="7" fill="black">Kibble</text>
  <text x="200" y="215" font-family="Comic Sans MS, cursive" font-size="7" fill="black">2%</text>
  <text x="270" y="215" font-family="Comic Sans MS, cursive" font-size="7" fill="black">ZERO</text>
  <!-- More lines -->
  <line x1="100" y1="220" x2="300" y2="220" stroke="black" stroke-width="0.5"/>
  <line x1="100" y1="240" x2="300" y2="240" stroke="black" stroke-width="0.5"/>
  <line x1="100" y1="260" x2="300" y2="260" stroke="black" stroke-width="0.5"/>
  <line x1="100" y1="280" x2="300" y2="280" stroke="black" stroke-width="0.5"/>
  <!-- Cat paw print stamp -->
  <ellipse cx="260" cy="310" rx="15" ry="10" fill="none" stroke="black" stroke-width="1.5" transform="rotate(-10 260 310)"/>
  <circle cx="250" cy="298" r="4" fill="none" stroke="black" stroke-width="1.5" transform="rotate(-10 250 298)"/>
  <circle cx="262" cy="295" r="4" fill="none" stroke="black" stroke-width="1.5" transform="rotate(-10 262 295)"/>
  <circle cx="272" cy="300" r="4" fill="none" stroke="black" stroke-width="1.5" transform="rotate(-10 272 300)"),
'''

# Write the SVGs
svgs = [
    ("ch01_sticky_sadness.svg", ch01_svg, "STICKY SADNESS"),
    ("ch02_column_of_shame.svg", ch02_svg, "COLUMN OF SHAME"),
    ("ch03_mud_trail.svg", ch03_svg, "THE EVIDENCE"),
    ("ch04_cat_salami_jetpack.svg", ch04_svg, "SALAMI JETPACK"),
    ("ch05_ledger.svg", ch05_svg, "FELINE LEDGER"),
]

for filename, content, caption in svgs:
    svg_full = svg_template.format(content=content, caption=caption)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        f.write(svg_full)
    print(f'Created: {filename}')

print(f'\nCreated {len(svgs)} SVG doodles in {output_dir}')
