#!/usr/bin/env python3
"""Generate all 25 SVG doodles for MDIM Book 1."""

import os

output_dir = os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg")
os.makedirs(output_dir, exist_ok=True)

SVG_HEADER = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
'''

SVG_FOOTER = '''
  <text x="200" y="385" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black" font-weight="bold">{caption}</text>
</svg>'''

# All 25 doodles with detailed content
doodles = {}

# Ch07: Lulu Chaos
doodles["ch07_lulu_chaos.svg"] = ("LULU CHAOS", '''  <!-- Chaotic kitchen scene -->
  <!-- Kitchen cabinets in background -->
  <rect x="40" y="40" width="80" height="120" fill="none" stroke="black" stroke-width="1.5"/>
  <rect x="280" y="40" width="80" height="120" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Cabinet handles -->
  <circle cx="80" cy="100" r="3" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="320" cy="100" r="3" fill="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Lulu spinning in center — DETAILED -->
  <!-- Body -->
  <ellipse cx="200" cy="200" rx="30" ry="40" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Dress with patterns -->
  <path d="M 175 180 Q 200 170 225 180" stroke="black" stroke-width="1.5"/>
  <path d="M 170 220 Q 200 240 230 220" stroke="black" stroke-width="1.5"/>
  <!-- Dress pattern — polka dots -->
  <circle cx="185" cy="195" r="2" fill="black"/>
  <circle cx="200" cy="188" r="2" fill="black"/>
  <circle cx="215" cy="198" r="2" fill="black"/>
  <circle cx="195" cy="210" r="2" fill="black"/>
  <circle cx="210" cy="208" r="2" fill="black"/>
  
  <!-- Head -->
  <circle cx="200" cy="140" r="25" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Messy pigtails — flying everywhere -->
  <path d="M 178 122 Q 155 105 148 88" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 172 130 Q 148 120 138 105" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 222 122 Q 245 105 252 88" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 228 130 Q 252 120 262 105" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Hair ribbon — flying off -->
  <path d="M 175 118 L 165 108 L 178 112" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 225 118 L 235 108 L 222 112" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Crazy spiral eyes -->
  <circle cx="190" cy="135" r="7" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="190" cy="135" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="190" cy="135" r="1.5" fill="black"/>
  <circle cx="210" cy="135" r="7" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="210" cy="135" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="210" cy="135" r="1.5" fill="black"/>
  <!-- Huge grin -->
  <path d="M 182 150 Q 200 170 218 150" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Teeth -->
  <rect x="190" y="152" width="5" height="5" fill="none" stroke="black" stroke-width="1"/>
  <rect x="198" y="152" width="5" height="5" fill="none" stroke="black" stroke-width="1"/>
  <rect x="206" y="150" width="5" height="4" fill="none" stroke="black" stroke-width="1"/>
  <!-- Ice cream smeared on face -->
  <ellipse cx="182" cy="158" rx="8" ry="5" fill="none" stroke="black" stroke-width="1.5"/>
  <ellipse cx="220" cy="155" rx="6" ry="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="185" cy="162" r="2" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="218" cy="158" r="1.5" fill="none" stroke="black" stroke-width="1"/>
  
  <!-- Arms outstretched -->
  <path d="M 172 190 Q 140 165 115 135" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 228 190 Q 260 165 285 135" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Hands with sticky fingers -->
  <circle cx="112" cy="132" r="8" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="288" cy="132" r="8" fill="none" stroke="black" stroke-width="2"/>
  <!-- Fingers spread -->
  <line x1="106" y1="126" x2="100" y2="118" stroke="black" stroke-width="1"/>
  <line x1="110" y1="124" x2="106" y2="115" stroke="black" stroke-width="1"/>
  <line x1="294" y1="126" x2="300" y2="118" stroke="black" stroke-width="1"/>
  <line x1="290" y1="124" x2="294" y2="115" stroke="black" stroke-width="1"/>
  
  <!-- Flying objects — scattered from spinning -->
  <!-- Ice cream cone — top left -->
  <path d="M 90 70 L 75 40 L 105 40 Z" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="90" cy="35" r="8" fill="none" stroke="black" stroke-width="2"/>
  <text x="82" y="38" font-family="Comic Sans MS, cursive" font-size="5" fill="black">99</text>
  
  <!-- Banana — top right -->
  <path d="M 310 80 Q 330 60 320 40" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  
  <!-- Cookie — bottom left -->
  <circle cx="70" cy="280" r="12" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="66" cy="276" r="1.5" fill="black"/>
  <circle cx="74" cy="282" r="1.5" fill="black"/>
  <circle cx="68" cy="284" r="1" fill="black"/>
  <circle cx="76" cy="278" r="1" fill="black"/>
  
  <!-- Apple — bottom right -->
  <circle cx="330" cy="290" r="10" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 330 280 L 333 272" stroke="black" stroke-width="1.5"/>
  <ellipse cx="326" cy="278" rx="3" ry="2" fill="none" stroke="black" stroke-width="1"/>
  
  <!-- Spilled milk puddle -->
  <ellipse cx="150" cy="310" rx="30" ry="8" fill="none" stroke="black" stroke-width="1.5" stroke-dasharray="3 3"/>
  <ellipse cx="260" cy="305" rx="20" ry="5" fill="none" stroke="black" stroke-width="1" stroke-dasharray="2 3"/>
  
  <!-- Motion lines around Lulu -->
  <path d="M 140 110 Q 125 95 135 85" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 260 110 Q 275 95 265 85" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 130 260 Q 115 270 120 285" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 270 260 Q 285 270 280 285" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  
  <!-- Mummy in corner — exhausted, clipboard in hand -->
  <circle cx="340" cy="320" r="15" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Mummy's tight bun -->
  <circle cx="340" cy="308" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Mummy's tired eyes — spirals -->
  <circle cx="334" cy="318" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="346" cy="318" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Clipboard -->
  <rect x="325" y="335" width="28" height="35" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="339" y="348" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">NEON</text>
  <text x="339" y="356" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">ORANGE</text>
  <line x1="328" y1="360" x2="350" y2="360" stroke="black" stroke-width="0.5"/>
  
  <!-- Schedule floating around (blown off clipboard) -->
  <rect x="50" y="320" width="40" height="25" fill="white" stroke="black" stroke-width="1" transform="rotate(15 60 332)"/>
  <text x="62" y="332" font-family="Comic Sans MS, cursive" font-size="4" fill="black" transform="rotate(15 62 332)">SWIM</text>
  <text x="62" y="338" font-family="Comic Sans MS, cursive" font-size="4" fill="black" transform="rotate(15 62 338)">LU: 3pm</text>
  
  <!-- Arrow pointing to Lulu -->
  <path d="M 60 60 L 140 120" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <text x="35" y="55" font-family="Comic Sans MS, cursive" font-size="8" fill="black">tornado</text>
  <text x="35" y="65" font-family="Comic Sans MS, cursive" font-size="8" fill="black">mode!</text>
''')

# Ch08: Henry Ride (Big Muddy Flats)
doodles["ch08_henry_ride.svg"] = ("SIR HENRY", '''  <!-- Big Mud Flats — vast muddy terrain -->
  <!-- Undulating ground -->
  <path d="M 40 280 Q 80 270 120 275 Q 160 265 200 270 Q 240 260 280 268 Q 320 255 360 265" fill="none" stroke="black" stroke-width="2"/>
  <!-- Mud puddles -->
  <ellipse cx="80" cy="290" rx="20" ry="6" fill="none" stroke="black" stroke-width="1" stroke-dasharray="3 3"/>
  <ellipse cx="300" cy="285" rx="25" ry="7" fill="none" stroke="black" stroke-width="1" stroke-dasharray="3 3"/>
  <ellipse cx="200" cy="295" rx="15" ry="5" fill="none" stroke="black" stroke-width="1" stroke-dasharray="2 3"/>
  
  <!-- Distant hills -->
  <path d="M 40 250 Q 100 230 160 245" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 240 240 Q 300 220 360 235" fill="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Henry the Horse — majestic side view, mid-stride -->
  <!-- Body — muscular -->
  <ellipse cx="200" cy="180" rx="75" ry="42" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Neck — arched nobly -->
  <path d="M 135 165 Q 115 130 125 100" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Head — refined -->
  <ellipse cx="122" cy="85" rx="28" ry="20" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Ears — alert -->
  <path d="M 112 68 L 105 48 L 120 64" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 135 66 L 142 46 L 128 62" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Forelock between ears -->
  <path d="M 118 68 Q 122 58 126 68" stroke="black" stroke-width="1.5"/>
  <!-- Eye — noble, slightly concerned -->
  <ellipse cx="115" cy="80" rx="5" ry="4" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="115" cy="80" r="2" fill="black"/>
  <!-- Nostril — flaring -->
  <ellipse cx="98" cy="90" rx="4" ry="3" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Mouth — clenched jaw, determined -->
  <path d="M 100 100 Q 110 105 118 100" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Mane — flowing back -->
  <path d="M 132 70 Q 145 55 138 45" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 138 75 Q 152 58 145 48" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 142 82 Q 158 62 152 52" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 146 90 Q 162 68 156 58" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  
  <!-- SUPERHERO CAPE — flowing dramatically -->
  <path d="M 260 160 Q 310 140 335 155 Q 355 170 345 195 Q 330 215 305 210 Q 280 205 265 190" fill="none" stroke="black" stroke-width="2"/>
  <!-- Cape shine -->
  <path d="M 280 165 Q 305 150 320 165" stroke="black" stroke-width="1"/>
  <path d="M 290 180 Q 310 168 325 182" stroke="black" stroke-width="1"/>
  <!-- Cape pattern — star on back -->
  <path d="M 295 175 L 298 185 L 308 185 L 300 192 L 303 202 L 295 195 L 287 202 L 290 192 L 282 185 L 292 185 Z" fill="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Legs — powerful stride -->
  <path d="M 150 215 L 140 265 L 130 285" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 175 220 L 168 270 L 158 290" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 225 220 L 235 270 L 242 288" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 255 215 L 268 260 L 278 280" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Horseshoes -->
  <path d="M 125 285 Q 130 293 138 288" stroke="black" stroke-width="2"/>
  <path d="M 153 290 Q 158 298 166 293" stroke="black" stroke-width="2"/>
  <path d="M 237 288 Q 242 296 250 291" stroke="black" stroke-width="2"/>
  <path d="M 273 280 Q 278 288 286 283" stroke="black" stroke-width="2"/>
  
  <!-- Tail — flowing dramatically -->
  <path d="M 270 185 Q 300 175 315 190 Q 325 205 310 210" stroke="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 272 190 Q 295 182 308 195" stroke="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Bea riding Henry — balanced on back -->
  <!-- Bea's body -->
  <ellipse cx="200" cy="145" rx="12" ry="18" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Bea's head -->
  <circle cx="200" cy="122" r="12" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Bea's determined face -->
  <circle cx="195" cy="118" r="2" fill="black"/>
  <circle cx="205" cy="118" r="2" fill="black"/>
  <path d="M 196 128 Q 200 132 204 128" stroke="black" stroke-width="2"/>
  <!-- Bea's hair — flying back -->
  <path d="M 190 115 Q 180 108 175 112" stroke="black" stroke-width="2"/>
  <path d="M 210 115 Q 220 108 225 112" stroke="black" stroke-width="2"/>
  <!-- Bea's arms holding mane -->
  <path d="M 190 145 Q 175 150 165 155" stroke="black" stroke-width="2"/>
  <path d="M 210 145 Q 225 150 230 148" stroke="black" stroke-width="2"/>
  
  <!-- Barnaby tucked in front of Bea — small and round -->
  <circle cx="200" cy="155" r="15" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="195" cy="152" r="2" fill="black"/>
  <circle cx="205" cy="152" r="2" fill="black"/>
  <path d="M 196 160 Q 200 164 204 160" stroke="black" stroke-width="1.5"/>
  <!-- Barnaby's worried expression -->
  <path d="M 192 148 L 190 144" stroke="black" stroke-width="1"/>
  <path d="M 208 148 L 210 144" stroke="black" stroke-width="1"/>
  
  <!-- Parents' car in background — broken down -->
  <rect x="50" y="230" width="55" height="28" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="62" cy="262" r="7" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="92" cy="262" r="7" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Flat tire on one -->
  <circle cx="62" cy="262" r="3" fill="black"/>
  <!-- Smoke from hood -->
  <path d="M 75 225 Q 70 215 75 205" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 72 220 Q 67 212 70 202" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <!-- Daddy peering under hood -->
  <circle cx="80" cy="215" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="83" y1="220" x2="90" y2="230" stroke="black" stroke-width="1.5"/>
  
  <!-- Big Muddy Flats signpost -->
  <rect x="310" y="200" width="6" height="60" fill="none" stroke="black" stroke-width="2"/>
  <rect x="295" y="195" width="40" height="20" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="315" y="205" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">BIG MUDDY</text>
  <text x="315" y="212" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">FLATS</text>
  
  <!-- Arrow pointing to Henry -->
  <path d="M 140 50 L 160 90" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <text x="105" y="45" font-family="Comic Sans MS, cursive" font-size="8" fill="black">noble</text>
  <text x="105" y="55" font-family="Comic Sans MS, cursive" font-size="8" fill="black">steed!</text>
''')

# Write all doodles
for filename, (caption, content) in doodles.items():
    svg = SVG_HEADER + content + SVG_FOOTER.format(caption=caption)
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        f.write(svg)
    lines = svg.count('\n')
    print(f'{filename}: {lines} lines, {len(svg)} bytes')

print(f'\nCreated {len(doodles)} SVG doodles')
