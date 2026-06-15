#!/usr/bin/env python3
"""Generate SVG doodles ch09-25 for MDIM Book 1."""

import os

output_dir = os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg")

SVG_HEADER = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
'''

SVG_FOOTER = '''
  <text x="200" y="385" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black" font-weight="bold">{caption}</text>
</svg>'''

doodles = {}

# Ch09: Mud Crosssection
doodles["ch09_mud_crosssection.svg"] = ("MUD SCIENCE", '''  <!-- Science diagram style — cross-section of mud layers -->
  <!-- Outer frame -->
  <rect x="60" y="60" width="280" height="280" fill="none" stroke="black" stroke-width="2.5"/>
  
  <!-- Top layer: SLIME (greenish) -->
  <rect x="60" y="60" width="280" height="70" fill="none" stroke="black" stroke-width="2"/>
  <text x="200" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="18" fill="black">SLIME</text>
  <!-- Slime bubbles -->
  <circle cx="100" cy="85" r="5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="150" cy="78" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="250" cy="90" r="4" fill="none" stroke="black" stroke-width="1.2"/>
  <circle cx="310" cy="80" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Slime drips -->
  <path d="M 120 130 Q 115 145 125 150" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 200 130 Q 205 140 198 148" fill="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Middle layer: MYSTERY GOOP -->
  <rect x="60" y="130" width="280" height="70" fill="none" stroke="black" stroke-width="2"/>
  <text x="200" y="170" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="16" fill="black">MYSTERY GOOP</text>
  <!-- Goop texture — wavy lines -->
  <path d="M 80 150 Q 120 145 160 152 Q 200 158 240 148 Q 280 142 320 150" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 90 165 Q 130 160 170 167 Q 210 172 250 163 Q 290 158 330 165" fill="none" stroke="black" stroke-width="1"/>
  <!-- Suspicious bubbles -->
  <circle cx="130" cy="155" r="4" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="270" cy="160" r="3" fill="none" stroke="black" stroke-width="1"/>
  
  <!-- Bottom layer: CLUE -->
  <rect x="60" y="200" width="280" height="70" fill="none" stroke="black" stroke-width="2"/>
  <text x="200" y="240" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="18" fill="black">CLUE</text>
  <!-- Clue items — paw print -->
  <ellipse cx="150" cy="230" rx="12" ry="8" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="142" cy="222" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="155" cy="219" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="163" cy="224" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Clue items — hair strand -->
  <path d="M 230 225 Q 240 235 235 245" stroke="black" stroke-width="1.5"/>
  <path d="M 235 228 Q 245 238 240 248" stroke="black" stroke-width="1"/>
  
  <!-- Depth markers on left side -->
  <text x="45" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">0m</text>
  <text x="45" y="170" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">2m</text>
  <text x="45" y="240" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">4m</text>
  <!-- Depth line -->
  <line x1="55" y1="130" x2="55" y2="270" stroke="black" stroke-width="1"/>
  <line x1="52" y1="130" x2="58" y2="130" stroke="black" stroke-width="1"/>
  <line x1="52" y1="200" x2="58" y2="200" stroke="black" stroke-width="1"/>
  <line x1="52" y1="270" x2="58" y2="270" stroke="black" stroke-width="1"/>
  
  <!-- Bea's hand holding magnifying glass at bottom -->
  <path d="M 320 300 Q 335 290 330 275" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="328" y2="270" r="15" fill="none" stroke="black" stroke-width="2.5"/>
  <line x1="338" y1="280" x2="350" y2="295" stroke="black" stroke-width="3" stroke-linecap="round"/>
  <!-- Glint -->
  <circle cx="322" cy="265" r="2" fill="none" stroke="black" stroke-width="0.8"/>
  
  <!-- Arrow pointing down -->
  <path d="M 200 300 L 200 340" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <text x="200" y="355" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">dig here!</text>
  
  <!-- Small note in corner -->
  <rect x="280" y="280" width="50" height="30" fill="white" stroke="black" stroke-width="1" transform="rotate(5 305 295)"/>
  <text x="305" y="292" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black" transform="rotate(5 305 292)">note: smells</text>
  <text x="305" y="300" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black" transform="rotate(5 305 300)">TERRIBLE</text>
''')

# Ch10: Salami Sub
doodles["ch10_sub_salami.svg"] = ("SALAMI SUB", '''  <!-- Cross-section of a tiny submarine — the Salami Sub -->
  <!-- Submarine outer hull -->
  <ellipse cx="200" cy="200" rx="100" ry="50" fill="none" stroke="black" stroke-width="3"/>
  <!-- Conning tower -->
  <rect x="175" y="120" width="50" height="35" fill="none" stroke="black" stroke-width="2.5"/>
  <rect x="185" y="105" width="30" height="15" fill="none" stroke="black" stroke-width="2"/>
  <!-- Periscope -->
  <line x1="200" y1="105" x2="200" y2="70" stroke="black" stroke-width="2.5"/>
  <rect x="195" y="60" width="10" height="8" fill="none" stroke="black" stroke-width="2"/>
  <!-- Periscope eye -->
  <circle cx="200" cy="58" r="3" fill="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Propeller -->
  <ellipse cx="310" cy="200" rx="15" ry="25" fill="none" stroke="black" stroke-width="2"/>
  <line x1="310" y1="175" x2="310" y2="225" stroke="black" stroke-width="1.5"/>
  <line x1="298" y1="200" x2="322" y2="200" stroke="black" stroke-width="1.5"/>
  
  <!-- Front viewport -->
  <circle cx="100" cy="190" r="20" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="100" cy="190" r="12" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Light beam from viewport -->
  <path d="M 80 180 L 40 160" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 80 190 L 35 180" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 80 200 L 40 200" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  
  <!-- Interior — Salami in pilot seat -->
  <!-- Pilot seat -->
  <rect x="160" y="210" width="40" height="25" fill="none" stroke="black" stroke-width="2"/>
  <!-- Salami pilot — round with face -->
  <circle cx="180" cy="200" r="15" fill="none" stroke="black" stroke-width="2"/>
  <!-- Salami pilot goggles -->
  <rect x="170" y="193" width="20" height="8" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="175" cy="197" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="185" cy="197" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Salami pilot smile -->
  <path d="M 175 207 Q 180 212 185 207" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Salami pilot arms on controls -->
  <path d="M 168 210 Q 155 220 148 215" stroke="black" stroke-width="2"/>
  <path d="M 192 210 Q 205 220 212 215" stroke="black" stroke-width="2"/>
  
  <!-- Control panel -->
  <rect x="140" y="230" width="80" height="15" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Buttons and dials -->
  <circle cx="155" cy="237" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="170" cy="237" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="185" cy="237" r="3" fill="none" stroke="black" stroke-width="1"/>
  <rect x="195" y="233" width="10" height="8" fill="none" stroke="black" stroke-width="1"/>
  <text x="200" y="239" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="4" fill="black">GO</text>
  
  <!-- Depth gauge -->
  <circle cx="250" cy="170" r="15" fill="none" stroke="black" stroke-width="2"/>
  <text x="250" y="168" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">DEPTH</text>
  <text x="250" y="178" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">42m</text>
  <!-- Gauge needle -->
  <line x1="250" y1="170" x2="260" y2="160" stroke="black" stroke-width="1.5"/>
  
  <!-- Bubbles rising -->
  <circle cx="150" cy="100" r="4" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="170" cy="80" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="140" cy="60" r="5" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="185" cy="50" r="2" fill="none" stroke="black" stroke-width="0.8"/>
  <circle cx="155" cy="40" r="3" fill="none" stroke="black" stroke-width="0.8"/>
  
  <!-- Fish swimming by -->
  <ellipse cx="50" cy="150" rx="15" ry="8" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 35 150 L 25 142 L 25 158 Z" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="55" cy="147" r="1.5" fill="black"/>
  <!-- Fish expression — surprised -->
  <circle cx="58" cy="152" r="2" fill="none" stroke="black" stroke-width="1"/>
  
  <!-- Caption -->
  <text x="200" y="385" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black" font-weight="bold">SALAMI SUB</text>''')

# Write all
for filename, (caption, content) in doodles.items():
    svg = SVG_HEADER + content + SVG_FOOTER.format(caption=caption)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        f.write(svg)
    lines = svg.count('\n')
    print(f'{filename}: {lines} lines, {len(svg)} bytes')

print(f'\nCreated {len(doodles)} SVG doodles')
