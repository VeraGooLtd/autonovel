#!/usr/bin/env python3
"""Generate SVG doodles for MDIM Book 1, chapters 7-25."""

import os

output_dir = os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg")

# All doodles ch07-25 with detailed SVG content
doodles = {
    "ch07_lulu_chaos.svg": {
        "caption": "LULU CHAOS",
        "content": '''  <!-- Kitchen floor with tile pattern -->
  <rect x="40" y="40" width="320" height="320" fill="none" stroke="black" stroke-width="1"/>
  <line x1="120" y1="40" x2="120" y2="360" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
  <line x1="200" y1="40" x2="200" y2="360" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
  <line x1="280" y1="40" x2="280" y2="360" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
  <line x1="40" y1="120" x2="360" y2="120" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
  <line x1="40" y1="200" x2="360" y2="200" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
  <line x1="40" y1="280" x2="360" y2="280" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
  
  <!-- Lulu spinning in center — body -->
  <ellipse cx="200" cy="200" rx="35" ry="45" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Head -->
  <circle cx="200" cy="140" r="25" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Messy pigtails -->
  <path d="M 175 125 Q 155 110 160 95" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 225 125 Q 245 110 240 95" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Pigtail bows -->
  <path d="M 158 92 L 152 85 L 162 88" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 242 92 L 248 85 L 238 88" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Crazy eyes — spirals -->
  <circle cx="190" cy="135" r="6" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="190" cy="135" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="210" cy="135" r="6" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="210" cy="135" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Big grinning mouth -->
  <ellipse cx="200" cy="155" rx="12" ry="8" fill="none" stroke="black" stroke-width="2"/>
  <!-- Teeth -->
  <rect x="193" y="152" width="4" height="4" fill="none" stroke="black" stroke-width="1"/>
  <rect x="203" y="152" width="4" height="4" fill="none" stroke="black" stroke-width="1"/>
  <!-- Ice cream on face -->
  <ellipse cx="185" cy="160" rx="8" ry="5" fill="none" stroke="black" stroke-width="1.5"/>
  <ellipse cx="215" cy="158" rx="6" ry="4" fill="none" stroke="black" stroke-width="1.5"/>
  
  <!-- Arms outstretched — spinning -->
  <path d="M 165 190 Q 130 170 110 140" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 235 190 Q 270 170 290 140" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Hands -->
  <circle cx="108" cy="138" r="8" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="292" cy="138" r="8" fill="none" stroke="black" stroke-width="2"/>
  
  <!-- Flying objects from spinning -->
  <!-- Ice cream cone -->
  <path d="M 100 80 L 85 50 L 115 50 Z" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="100" cy="45" r="8" fill="none" stroke="black" stroke-width="2"/>
  <!-- Banana -->
  <path d="M 300 100 Q 320 80 310 60" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Cookie -->
  <circle cx="80" cy="250" r="12" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="76" cy="246" r="1.5" fill="black"/>
  <circle cx="84" cy="252" r="1.5" fill="black"/>
  <!-- Apple -->
  <circle cx="320" cy="260" r="10" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 320 250 L 322 242" stroke="black" stroke-width="1.5"/>
  
  <!-- Motion/spin lines -->
  <path d="M 150 100 Q 140 80 155 70" stroke="black" stroke-width="1" stroke-linecap="round" stroke-dasharray="3 2"/>
  <path d="M 250 100 Q 260 80 245 70" stroke="black" stroke-width="1" stroke-linecap="round" stroke-dasharray="3 2"/>
  <path d="M 130 250 Q 115 260 120 275" stroke="black" stroke-width="1" stroke-linecap="round" stroke-dasharray="3 2"/>
  <path d="M 270 250 Q 285 260 280 275" stroke="black" stroke-width="1" stroke-linecap="round" stroke-dasharray="3 2"/>
  
  <!-- Drool strings -->
  <line x1="188" y1="162" x2="175" y2="200" stroke="black" stroke-width="0.8"/>
  <line x1="212" y1="162" x2="225" y2="195" stroke="black" stroke-width="0.8"/>
  
  <!-- Mummy in corner looking exhausted -->
  <circle cx="340" cy="320" r="15" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 332 317 Q 340 312 348 317" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Clipboard -->
  <rect x="325" y="335" width="25" height="30" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="337" y="350" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="4" fill="black">NEON</text>
  <text x="337" y="356" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="4" fill="black">ORANGE</text>
  <!-- Mummy's tired eyes -->
  <line x1="335" y1="315" x2="339" y2="315" stroke="black" stroke-width="1"/>
  <line x1="341" y1="315" x2="345" y2="315" stroke="black" stroke-width="1"/>
  
  <!-- Caption -->
  <text x="200" y="385" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black" font-weight="bold">LULU CHAOS</text>'''
    },
    "ch08_henry_ride.svg": {
        "caption": "SIR HENRY",
        "content": '''  <!-- Mud Flats ground — uneven terrain -->
  <path d="M 40 300 Q 80 290 120 295 Q 160 285 200 290 Q 240 280 280 288 Q 320 275 360 285" fill="none" stroke="black" stroke-width="2"/>
  <!-- Mud puddles -->
  <ellipse cx="100" cy="310" rx="25" ry="8" fill="none" stroke="black" stroke-width="1" stroke-dasharray="3 3"/>
  <ellipse cx="280" cy="305" rx="20" ry="6" fill="none" stroke="black" stroke-width="1" stroke-dasharray="3 3"/>
  
  <!-- Henry the Horse — majestic side view -->
  <!-- Body -->
  <ellipse cx="200" cy="200" rx="70" ry="40" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Neck -->
  <path d="M 140 180 Q 120 140 130 110" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Head -->
  <ellipse cx="125" cy="95" rx="25" ry="18" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Ears -->
  <path d="M 115 80 L 110 60 L 125 75" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 135 78 L 140 58 L 128 73" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- Eye — noble expression -->
  <circle cx="120" cy="90" r="4" fill="black"/>
  <!-- Nostril -->
  <circle cx="108" cy="100" r="2" fill="black"/>
  <!-- Mouth — slight smile -->
  <path d="M 105 108 Q 110 112 118 108" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Mane -->
  <path d="M 130 75 Q 140 65 135 55" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 135 78 Q 148 68 142 58" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 138 82 Q 152 72 148 62" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <path d="M 140 88 Q 155 78 150 68" stroke="black" stroke-width="2" stroke-linecap="round"/>
  
  <!-- Superhero cape flowing behind -->
  <path d="M 250 180 Q 300 160 320 180 Q 340 200 330 220 Q 315 235 290 230 Q 270 225 250 210" fill="none" stroke="black" stroke-width="2"/>
  <!-- Cape shine lines -->
  <path d="M 270 185 Q 290 175 300 190" stroke="black" stroke-width="1"/>
  <path d="M 280 200 Q 300 190 310 205" stroke="black" stroke-width="1"/>
  
  <!-- Legs — mid-stride -->
  <path d="M 160 235 L 150 280 L 140 295" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 180 240 L 175 285 L 165 300" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 220 240 L 230 285 L 235 298" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 250 235 L 260 275 L 268 290" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Horseshoes -->
  <path d="M 135 295 Q 140 302 148 298" stroke="black" stroke-width="1.5"/>
  <path d="M 160 300 Q 165 307 173 303" stroke="black" stroke-width="1.5"/>
  <path d="M 230 298 Q 235 305 243 301" stroke="black" stroke-width="1.5"/>
  <path d="M 263 290 Q 268 297 276 293" stroke="black" stroke-width="1.5"/>
  
  <!-- Tail flowing -->
  <path d="M 265 195 Q 290 185 300 195 Q 310 205 295 210" stroke="black" stroke-width="2" stroke-linecap="round"/>
  
  <!-- Bea and Barnaby on Henry's back -->
  <!-- Bea — sitting sideways -->
  <circle cx="195" cy="165" r="12" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 188 160 L 185 155" stroke="black" stroke-width="1.5"/>
  <path d="M 202 160 L 205 155" stroke="black" stroke-width="1.5"/>
  <circle cx="190" cy="162" r="1.5" fill="black"/>
  <circle cx="200" cy="162" r="1.5" fill="black"/>
  <!-- Bea's body -->
  <ellipse cx="195" cy="180" rx="10" ry="12" fill="none" stroke="black" stroke-width="2"/>
  <!-- Bea's legs dangling -->
  <line x1="190" y1="192" x2="185" y2="210" stroke="black" stroke-width="2"/>
  <line x1="200" y1="192" x2="205" y2="210" stroke="black" stroke-width="2"/>
  
  <!-- Barnaby — smaller, behind Bea -->
  <circle cx="220" cy="170" r="9" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 215 166 Q 220 162 225 166" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="216" cy="167" r="1.5" fill="black"/>
  <circle cx="224" cy="167" r="1.5" fill="black"/>
  
  <!-- Parents' car in background (broke down) -->
  <rect x="50" y="240" width="50" height="25" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="65" cy="270" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="90" cy="270" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Smoke from car -->
  <path d="M 70 235 Q 65 225 70 215" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <text x="75" y="230" font-family="Comic Sans MS, cursive" font-size="6" fill="black">fzzzt</text>
  
  <!-- Big Muddy Flats sign -->
  <rect x="300" y="240" width="50" height="30" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="325" y="252" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">BIG MUDDY</text>
  <text x="325" y="260" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">FLATS</text>
  
  <!-- Caption -->
  <text x="200" y="385" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black" font-weight="bold">SIR HENRY</text>'''
    },
}

# Write each SVG
for filename, data in doodles.items():
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
{data["content"]}
</svg>'''
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        f.write(svg)
    print(f'Created: {filename} ({len(svg)} bytes)')

print(f'\nTotal: {len(doodles)} doodles created')
