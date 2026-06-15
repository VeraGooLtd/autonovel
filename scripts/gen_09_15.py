#!/usr/bin/env python3
"""Generate SVG doodles ch09-25 for MDIM Book 1."""
import os
D=os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg")
H='''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
'''
F='''
  <text x="200" y="385" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black" font-weight="bold">{c}</text>
</svg>'''

# Ch09: Mud Crosssection
open(D+"/ch09_mud_crosssection.svg","w").write(H+'''
  <rect x="60" y="60" width="280" height="280" fill="none" stroke="black" stroke-width="2.5"/>
  <rect x="60" y="60" width="280" height="70" fill="none" stroke="black" stroke-width="2"/>
  <text x="200" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="18" fill="black">SLIME</text>
  <circle cx="100" cy="85" r="5" fill="none" stroke="black" stroke-width="1.5"/><circle cx="150" cy="78" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="250" cy="90" r="4" fill="none" stroke="black" stroke-width="1.2"/><circle cx="310" cy="80" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 120 130 Q 115 145 125 150" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 200 130 Q 205 140 198 148" fill="none" stroke="black" stroke-width="1.5"/>
  <rect x="60" y="130" width="280" height="70" fill="none" stroke="black" stroke-width="2"/>
  <text x="200" y="170" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="16" fill="black">MYSTERY GOOP</text>
  <path d="M 80 150 Q 120 145 160 152 Q 200 158 240 148 Q 280 142 320 150" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 90 165 Q 130 160 170 167 Q 210 172 250 163 Q 290 158 330 165" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="130" cy="155" r="4" fill="none" stroke="black" stroke-width="1"/><circle cx="270" cy="160" r="3" fill="none" stroke="black" stroke-width="1"/>
  <rect x="60" y="200" width="280" height="70" fill="none" stroke="black" stroke-width="2"/>
  <text x="200" y="240" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="18" fill="black">CLUE</text>
  <ellipse cx="150" cy="230" rx="12" ry="8" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="142" cy="222" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="155" cy="219" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="163" cy="224" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 230 225 Q 240 235 235 245" stroke="black" stroke-width="1.5"/>
  <path d="M 235 228 Q 245 238 240 248" stroke="black" stroke-width="1"/>
  <text x="45" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">0m</text>
  <text x="45" y="170" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">2m</text>
  <text x="45" y="240" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">4m</text>
  <line x1="55" y1="130" x2="55" y2="270" stroke="black" stroke-width="1"/>
  <line x1="52" y1="130" x2="58" y2="130" stroke="black" stroke-width="1"/>
  <line x1="52" y1="200" x2="58" y2="200" stroke="black" stroke-width="1"/>
  <line x1="52" y1="270" x2="58" y2="270" stroke="black" stroke-width="1"/>
  <path d="M 320 300 Q 335 290 330 275" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <circle cx="328" cy="270" r="15" fill="none" stroke="black" stroke-width="2.5"/>
  <line x1="338" y1="280" x2="350" y2="295" stroke="black" stroke-width="3" stroke-linecap="round"/>
  <circle cx="322" cy="265" r="2" fill="none" stroke="black" stroke-width="0.8"/>
  <path d="M 200 300 L 200 340" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <text x="200" y="355" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">dig here!</text>
  <rect x="280" y="280" width="50" height="30" fill="white" stroke="black" stroke-width="1" transform="rotate(5 305 295)"/>
  <text x="305" y="292" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black" transform="rotate(5 305 292)">note: smells</text>
  <text x="305" y="300" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black" transform="rotate(5 305 300)">TERRIBLE</text>
'''+F.format(c="MUD SCIENCE"))

# Ch10: Salami Sub
open(D+"/ch10_sub_salami.svg","w").write(H+'''
  <ellipse cx="200" cy="200" rx="100" ry="50" fill="none" stroke="black" stroke-width="3"/>
  <rect x="175" y="120" width="50" height="35" fill="none" stroke="black" stroke-width="2.5"/>
  <rect x="185" y="105" width="30" height="15" fill="none" stroke="black" stroke-width="2"/>
  <line x1="200" y1="105" x2="200" y2="70" stroke="black" stroke-width="2.5"/>
  <rect x="195" y="60" width="10" height="8" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="200" cy="58" r="3" fill="none" stroke="black" stroke-width="1.5"/>
  <ellipse cx="310" cy="200" rx="15" ry="25" fill="none" stroke="black" stroke-width="2"/>
  <line x1="310" y1="175" x2="310" y2="225" stroke="black" stroke-width="1.5"/>
  <line x1="298" y1="200" x2="322" y2="200" stroke="black" stroke-width="1.5"/>
  <circle cx="100" cy="190" r="20" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="100" cy="190" r="12" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 80 180 L 40 160" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 80 190 L 35 180" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 80 200 L 40 200" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <rect x="160" y="210" width="40" height="25" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="180" cy="200" r="15" fill="none" stroke="black" stroke-width="2"/>
  <rect x="170" y="193" width="20" height="8" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="175" cy="197" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="185" cy="197" r="3" fill="none" stroke="black" stroke-width="1"/>
  <path d="M 175 207 Q 180 212 185 207" stroke="black" stroke-width="1.5"/>
  <path d="M 168 210 Q 155 220 148 215" stroke="black" stroke-width="2"/>
  <path d="M 192 210 Q 205 220 212 215" stroke="black" stroke-width="2"/>
  <rect x="140" y="230" width="80" height="15" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="155" cy="237" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="170" cy="237" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="185" cy="237" r="3" fill="none" stroke="black" stroke-width="1"/>
  <rect x="195" y="233" width="10" height="8" fill="none" stroke="black" stroke-width="1"/>
  <text x="200" y="239" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="4" fill="black">GO</text>
  <circle cx="250" cy="170" r="15" fill="none" stroke="black" stroke-width="2"/>
  <text x="250" y="168" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">DEPTH</text>
  <text x="250" y="178" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">42m</text>
  <line x1="250" y1="170" x2="260" y2="160" stroke="black" stroke-width="1.5"/>
  <circle cx="150" cy="100" r="4" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="170" cy="80" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="140" cy="60" r="5" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="185" cy="50" r="2" fill="none" stroke="black" stroke-width="0.8"/>
  <circle cx="155" cy="40" r="3" fill="none" stroke="black" stroke-width="0.8"/>
  <ellipse cx="50" cy="150" rx="15" ry="8" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 35 150 L 25 142 L 25 158 Z" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="55" cy="147" r="1.5" fill="black"/>
  <circle cx="58" cy="152" r="2" fill="none" stroke="black" stroke-width="1"/>
'''+F.format(c="SALAMI SUB"))

# Ch11: Canal Map
open(D+"/ch11_canal_map.svg","w").write(H+'''
  <rect x="50" y="50" width="300" height="300" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Aged paper texture -->
  <line x1="70" y1="70" x2="330" y2="70" stroke="black" stroke-width="0.3" stroke-dasharray="2 4"/>
  <line x1="70" y1="90" x2="330" y2="90" stroke="black" stroke-width="0.3" stroke-dasharray="3 3"/>
  <line x1="70" y1="110" x2="330" y2="110" stroke="black" stroke-width="0.3" stroke-dasharray="2 5"/>
  <line x1="70" y1="130" x2="330" y2="130" stroke="black" stroke-width="0.3" stroke-dasharray="4 2"/>
  <!-- Title -->
  <text x="200" y="80" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="14" fill="black">CANAL MAP</text>
  <text x="200" y="95" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">of Riverstone</text>
  <!-- Winding canal paths -->
  <path d="M 80 150 Q 120 130 160 150 Q 200 170 240 140 Q 280 110 320 130" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <path d="M 80 200 Q 140 180 180 210 Q 220 240 280 200 Q 320 180 340 200" fill="none" stroke="black" stroke-width="2" stroke-linecap="round"/>
  <!-- DUCK POND label -->
  <ellipse cx="280" cy="120" rx="30" ry="20" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="280" y="125" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">DUCK POND</text>
  <!-- Ducks in pond -->
  <ellipse cx="270" cy="115" rx="6" ry="4" fill="none" stroke="black" stroke-width="1"/>
  <ellipse cx="290" cy="118" rx="5" ry="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- MEOW-FIA HQ label -->
  <rect x="140" y="220" width="60" height="30" fill="white" stroke="black" stroke-width="2"/>
  <text x="170" y="235" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="7" fill="black">MEOW-FIA</text>
  <text x="170" y="245" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="7" fill="black">HQ</text>
  <!-- X marks the spot -->
  <path d="M 165 260 L 175 270 M 175 260 L 165 270" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <text x="170" y="280" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">CLUE HERE</text>
  <!-- Dotted path from pond to HQ -->
  <path d="M 280 140 Q 260 180 240 200 Q 220 220 200 230" fill="none" stroke="black" stroke-width="1.5" stroke-dasharray="4 3"/>
  <!-- Compass rose -->
  <circle cx="310" cy="280" r="20" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="310" y1="258" x2="310" y2="268" stroke="black" stroke-width="2"/>
  <line x1="310" y1="292" x2="310" y2="302" stroke="black" stroke-width="1.5"/>
  <line x1="288" y1="280" x2="298" y2="280" stroke="black" stroke-width="2"/>
  <line x1="322" y1="280" x2="332" y2="280" stroke="black" stroke-width="1.5"/>
  <text x="310" y="255" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="7" fill="black">N</text>
  <text x="310" y="310" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">S</text>
  <text x="283" y="283" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">W</text>
  <text x="337" y="283" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">E</text>
  <!-- Small boat drawing -->
  <path d="M 100 160 L 120 160 L 115 170 Z" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="110" y1="160" x2="110" y2="148" stroke="black" stroke-width="1"/>
  <path d="M 110 148 L 118 155 L 110 155" fill="none" stroke="black" stroke-width="1"/>
  <!-- "HERE LIES CLUE" text -->
  <text x="170" y="310" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">HERE LIES CLUE</text>
  <!-- Stain marks on paper -->
  <ellipse cx="90" cy="250" rx="15" ry="10" fill="none" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
  <ellipse cx="300" cy="180" rx="10" ry="8" fill="none" stroke="black" stroke-width="0.5" stroke-dasharray="2 2"/>
'''+F.format(c="CANAL MAP"))

# Ch12: Simba Grate
open(D+"/ch12_simba_grate.svg","w").write(H+'''
  <!-- Metal grate background -->
  <rect x="60" y="60" width="280" height="280" fill="none" stroke="black" stroke-width="3"/>
  <!-- Vertical bars -->
  <line x1="100" y1="60" x2="100" y2="340" stroke="black" stroke-width="3"/>
  <line x1="140" y1="60" x2="140" y2="340" stroke="black" stroke-width="3"/>
  <line x1="180" y1="60" x2="180" y2="340" stroke="black" stroke-width="3"/>
  <line x1="220" y1="60" x2="220" y2="340" stroke="black" stroke-width="3"/>
  <line x1="260" y1="60" x2="260" y2="340" stroke="black" stroke-width="3"/>
  <line x1="300" y1="60" x2="300" y2="340" stroke="black" stroke-width="3"/>
  <!-- Horizontal bars -->
  <line x1="60" y1="100" x2="340" y2="100" stroke="black" stroke-width="2.5"/>
  <line x1="60" y1="160" x2="340" y2="160" stroke="black" stroke-width="2.5"/>
  <line x1="60" y1="220" x2="340" y2="220" stroke="black" stroke-width="2.5"/>
  <line x1="60" y1="280" x2="340" y2="280" stroke="black" stroke-width="2.5"/>
  <!-- Cat face THROUGH the grate — filling the space -->
  <!-- Cat head outline -->
  <ellipse cx="200" cy="180" rx="90" ry="70" fill="none" stroke="black" stroke-width="3"/>
  <!-- Cat ears poking through bars -->
  <path d="M 120 120 L 100 70 L 140 110" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 280 120 L 300 70 L 260 110" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Inner ears -->
  <path d="M 122 115 L 108 82 L 138 108" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 278 115 L 292 82 L 262 108" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Glowing eyes -->
  <ellipse cx="160" cy="160" rx="20" ry="15" fill="none" stroke="black" stroke-width="2.5"/>
  <ellipse cx="240" cy="160" rx="20" ry="15" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Pupils — vertical slits -->
  <ellipse cx="160" cy="160" rx="5" ry="12" fill="black"/>
  <ellipse cx="240" cy="160" rx="5" ry="12" fill="black"/>
  <!-- Eye glow -->
  <circle cx="155" cy="155" r="2" fill="white" stroke="white" stroke-width="0.5"/>
  <circle cx="235" cy="155" r="2" fill="white" stroke="white" stroke-width="0.5"/>
  <!-- Nose -->
  <path d="M 195 195 L 200 190 L 205 195 Z" fill="black"/>
  <!-- Mouth — sinister grin -->
  <path d="M 170 210 Q 200 235 230 210" fill="none" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Fangs -->
  <path d="M 180 212 L 178 222 L 184 218" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 220 212 L 222 222 L 216 218" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Whiskers poking through bars -->
  <line x1="110" y1="180" x2="60" y2="170" stroke="black" stroke-width="1.5"/>
  <line x1="110" y1="190" x2="55" y2="190" stroke="black" stroke-width="1.5"/>
  <line x1="110" y1="200" x2="60" y2="210" stroke="black" stroke-width="1.5"/>
  <line x1="290" y1="180" x2="340" y2="170" stroke="black" stroke-width="1.5"/>
  <line x1="290" y1="190" x2="345" y2="190" stroke="black" stroke-width="1.5"/>
  <line x1="290" y1="200" x2="340" y2="210" stroke="black" stroke-width="1.5"/>
  <!-- Paws reaching through bars -->
  <path d="M 70 250 Q 60 240 70 230 Q 80 225 75 240" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 330 250 Q 340 240 330 230 Q 320 225 325 240" fill="none" stroke="black" stroke-width="2"/>
  <!-- Claw marks -->
  <line x1="72" y1="255" x2="68" y2="265" stroke="black" stroke-width="1"/>
  <line x1="76" y1="253" x2="74" y2="263" stroke="black" stroke-width="1"/>
  <line x1="328" y1="255" x2="332" y2="265" stroke="black" stroke-width="1"/>
  <line x1="324" y1="253" x2="326" y2="263" stroke="black" stroke-width="1"/>
  <!-- "PEEK-A-BOO" text -->
  <text x="200" y="320" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="14" fill="black">PEEK-A-BOO</text>
  <!-- Small mouse running away -->
  <ellipse cx="50" cy="300" rx="10" ry="6" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="42" cy="297" r="1.5" fill="black"/>
  <path d="M 38 292 L 32 285" stroke="black" stroke-width="1"/>
  <path d="M 40 292 L 36 284" stroke="black" stroke-width="1"/>
  <!-- Mouse sweat -->
  <ellipse cx="58" cy="290" rx="2" ry="3" fill="none" stroke="black" stroke-width="0.8"/>
'''+F.format(c="THE GINGER NINJA"))

# Ch13: Mission Impossible
open(D+"/ch13_mission_impossible.svg","w").write(H+'''
  <!-- Tactical diagram background -->
  <rect x="40" y="40" width="320" height="300" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Grid lines -->
  <line x1="120" y1="40" x2="120" y2="340" stroke="black" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="200" y1="40" x2="200" y2="340" stroke="black" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="280" y1="40" x2="280" y2="340" stroke="black" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="40" y1="120" x2="360" y2="120" stroke="black" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="40" y1="200" x2="360" y2="200" stroke="black" stroke-width="0.5" stroke-dasharray="3 3"/>
  <line x1="40" y1="280" x2="360" y2="280" stroke="black" stroke-width="0.5" stroke-dasharray="3 3"/>
  <!-- Title -->
  <text x="200" y="65" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12" fill="black">OPERATION: MAT</text>
  <text x="200" y="80" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">TOP SECRET</text>
  <!-- STEP 1 -->
  <circle cx="80" cy="110" r="12" fill="none" stroke="black" stroke-width="2"/>
  <text x="80" y="114" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">1</text>
  <text x="80" y="140" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">Henry pulls</text>
  <text x="80" y="150" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">the mat</text>
  <!-- Henry the Horse pulling -->
  <ellipse cx="80" cy="175" rx="20" ry="12" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 60 175 L 40 170" stroke="black" stroke-width="2"/>
  <rect x="35" y="160" width="15" height="20" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Arrow to step 2 -->
  <path d="M 100 175 L 150 175" stroke="black" stroke-width="1.5" stroke-dasharray="3 2"/>
  <polygon points="150,175 143,171 143,179" fill="black"/>
  <!-- STEP 2 -->
  <circle cx="180" cy="175" r="12" fill="none" stroke="black" stroke-width="2"/>
  <text x="180" y="179" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">2</text>
  <text x="180" y="205" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">Salami on</text>
  <text x="180" y="215" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">rope</text>
  <!-- Salami on rope -->
  <ellipse cx="180" cy="240" rx="15" ry="10" fill="none" stroke="black" stroke-width="2"/>
  <line x1="180" y1="230" x2="180" y2="200" stroke="black" stroke-width="1.5"/>
  <circle cx="180" cy="195" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Arrow to step 3 -->
  <path d="M 200 240 L 250 240" stroke="black" stroke-width="1.5" stroke-dasharray="3 2"/>
  <polygon points="250,240 243,236 243,244" fill="black"/>
  <!-- STEP 3 -->
  <circle cx="280" cy="240" r="12" fill="none" stroke="black" stroke-width="2"/>
  <text x="280" y="244" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">3</text>
  <text x="280" y="270" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">Barnaby</text>
  <text x="280" y="280" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">holds tail</text>
  <!-- Barnaby holding tail -->
  <circle cx="280" cy="305" r="10" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 272 310 L 260 315" stroke="black" stroke-width="2"/>
  <path d="M 288 310 L 300 305" stroke="black" stroke-width="2"/>
  <!-- Checkmarks -->
  <path d="M 75 105 L 78 108 L 85 101" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 175 170 L 178 173 L 185 166" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M 275 235 L 278 238 L 285 231" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <!-- Small explosion doodle -->
  <path d="M 320 100 Q 325 90 330 100 Q 335 85 340 100 Q 345 90 350 100" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="335" y="115" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">KABOOM</text>
  <!-- Notes in margins -->
  <text x="50" y="300" font-family="Comic Sans MS, cursive" font-size="5" fill="black">note: don't</text>
  <text x="50" y="308" font-family="Comic Sans MS, cursive" font-size="5" fill="black">let go!!</text>
'''+F.format(c="OPERATION MAT"))

# Ch14: Cat-Dar
open(D+"/ch14_cat_dar.svg","w").write(H+'''
  <!-- Science fair table -->
  <rect x="40" y="200" width="320" height="15" fill="none" stroke="black" stroke-width="2.5"/>
  <rect x="50" y="215" width="10" height="50" fill="none" stroke="black" stroke-width="2"/>
  <rect x="340" y="215" width="10" height="50" fill="none" stroke="black" stroke-width="2"/>
  <!-- "SCIENCE FAIR" banner -->
  <rect x="120" y="50" width="160" height="25" fill="white" stroke="black" stroke-width="2"/>
  <text x="200" y="67" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12" fill="black">SCIENCE FAIR</text>
  <!-- Cat-Dar device on table -->
  <rect x="150" y="120" width="100" height="80" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Antenna -->
  <line x1="200" y1="120" x2="200" y2="70" stroke="black" stroke-width="2.5"/>
  <circle cx="200" cy="65" r="5" fill="none" stroke="black" stroke-width="2"/>
  <!-- Dish -->
  <path d="M 170 85 Q 200 60 230 85" fill="none" stroke="black" stroke-width="2"/>
  <!-- Dials and buttons -->
  <circle cx="175" cy="150" r="8" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="175" y1="150" x2="175" y2="142" stroke="black" stroke-width="1.5"/>
  <circle cx="225" cy="150" r="8" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="225" y1="150" x2="230" y2="145" stroke="black" stroke-width="1.5"/>
  <rect x="185" y="170" width="30" height="15" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="200" y="181" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">CAT-DAR</text>
  <!-- Screen -->
  <rect x="165" y="130" width="70" height="25" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="200" y="147" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">BEEP BEEP</text>
  <!-- Blinking light -->
  <circle cx="240" cy="135" r="3" fill="black"/>
  <!-- Maya standing behind device -->
  <circle cx="200" cy="100" r="15" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Safety goggles -->
  <rect x="190" y="93" width="20" height="10" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="195" cy="98" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="205" cy="98" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Maya's intense expression -->
  <circle cx="194" cy="97" r="2" fill="black"/>
  <circle cx="206" cy="97" r="2" fill="black"/>
  <path d="M 195 108 Q 200 112 205 108" stroke="black" stroke-width="2"/>
  <!-- Maya's body -->
  <ellipse cx="200" cy="130" rx="12" ry="18" fill="none" stroke="black" stroke-width="2"/>
  <!-- Mr. Hendricks looking confused -->
  <circle cx="300" cy="140" r="12" fill="none" stroke="black" stroke-width="2"/>
  <!-- Confused eyes -->
  <circle cx="295" cy="136" r="2" fill="black"/>
  <circle cx="305" cy="136" r="2" fill="black"/>
  <!-- Confused mouth -->
  <path d="M 295 148 Q 300 145 305 148" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Question marks -->
  <text x="315" y="130" font-family="Comic Sans MS, cursive" font-size="10" fill="black">???</text>
  <!-- Other science projects in background -->
  <rect x="60" y="150" width="40" height="50" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="80" y="170" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">volcano</text>
  <rect x="300" y="150" width="40" height="50" fill="none" stroke="black" stroke-width="1.5"/>
  <text x="320" y="170" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">plants</text>
  <!-- Arrow pointing to Cat-Dar -->
  <path d="M 280 100 L 230 130" stroke="black" stroke-width="1.5" stroke-linecap="round"/>
  <text x="285" y="95" font-family="Comic Sans MS, cursive" font-size="7" fill="black">my project!</text>
'''+F.format(c="CAT-DAR 3000"))

# Ch15: Boathouse
open(D+"/ch15_boathouse.svg","w").write(H+'''
  <!-- Wooden walls with peeling paint -->
  <rect x="40" y="40" width="320" height="280" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Wood planks -->
  <line x1="40" y1="80" x2="360" y2="80" stroke="black" stroke-width="0.5"/>
  <line x1="40" y1="120" x2="360" y2="120" stroke="black" stroke-width="0.5"/>
  <line x1="40" y1="160" x2="360" y2="160" stroke="black" stroke-width="0.5"/>
  <line x1="40" y1="200" x2="360" y2="200" stroke="black" stroke-width="0.5"/>
  <line x1="40" y1="240" x2="360" y2="240" stroke="black" stroke-width="0.5"/>
  <line x1="40" y1="280" x2="360" y2="280" stroke="black" stroke-width="0.5"/>
  <!-- Peeling paint -->
  <path d="M 100 100 Q 105 95 102 105" fill="none" stroke="black" stroke-width="0.8"/>
  <path d="M 250 180 Q 255 175 252 185" fill="none" stroke="black" stroke-width="0.8"/>
  <!-- Porthole window -->
  <circle cx="300" cy="100" r="25" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="300" cy="100" r="20" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="300" y1="80" x2="300" y2="120" stroke="black" stroke-width="1.5"/>
  <line x1="280" y1="100" x2="320" y2="100" stroke="black" stroke-width="1.5"/>
  <!-- Water visible through porthole -->
  <path d="M 285 110 Q 300 105 315 110" stroke="black" stroke-width="1"/>
  <!-- Monitors on wall -->
  <rect x="60" y="70" width="60" height="40" fill="none" stroke="black" stroke-width="2"/>
  <rect x="65" y="75" width="50" height="30" fill="none" stroke="black" stroke-width="1"/>
  <!-- Screen content — map -->
  <path d="M 75 85 Q 90 80 105 90" stroke="black" stroke-width="0.8"/>
  <circle cx="90" cy="85" r="2" fill="black"/>
  <text x="90" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="4" fill="black">SURVEILLANCE</text>
  <rect x="130" y="70" width="60" height="40" fill="none" stroke="black" stroke-width="2"/>
  <rect x="135" y="75" width="50" height="30" fill="none" stroke="black" stroke-width="1"/>
  <!-- Screen content — cat face -->
  <circle cx="160" cy="88" r="8" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="157" cy="86" r="1.5" fill="black"/>
  <circle cx="163" cy="86" r="1.5" fill="black"/>
  <text x="160" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="4" fill="black">TARGET</text>
  <!-- "MEOW-FIA HQ" sign -->
  <rect x="140" y="130" width="120" height="20" fill="white" stroke="black" stroke-width="2"/>
  <text x="200" y="144" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">MEOW-FIA HQ</text>
  <!-- Plush Cat Throne -->
  <rect x="150" y="180" width="100" height="60" fill="none" stroke="black" stroke-width="2.5"/>
  <rect x="155" y="185" width="90" height="30" fill="none" stroke="black" stroke-width="2"/>
  <!-- Throne cushion texture -->
  <line x1="165" y1="195" x2="235" y2="195" stroke="black" stroke-width="0.5"/>
  <line x1="165" y1="200" x2="235" y2="200" stroke="black" stroke-width="0.5"/>
  <line x1="165" y1="205" x2="235" y2="205" stroke="black" stroke-width="0.5"/>
  <!-- Throne arms -->
  <path d="M 150 180 L 140 170 L 140 200" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 250 180 L 260 170 L 260 200" fill="none" stroke="black" stroke-width="2"/>
  <!-- Ginger cat on throne -->
  <ellipse cx="200" cy="175" rx="20" ry="15" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="200" cy="158" r="12" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 190 148 L 185 135 L 195 145" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 210 148 L 215 135 L 205 145" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="195" cy="155" r="2" fill="black"/>
  <circle cx="205" cy="155" r="2" fill="black"/>
  <path d="M 196 163 Q 200 168 204 163" stroke="black" stroke-width="1.5"/>
  <!-- Cat's smug expression -->
  <path d="M 193 160 L 190 158" stroke="black" stroke-width="1"/>
  <path d="M 207 160 L 210 158" stroke="black" stroke-width="1"/>
  <!-- Tiny cat soldiers -->
  <circle cx="100" cy="260" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="100" y1="266" x2="100" y2="280" stroke="black" stroke-width="1.5"/>
  <line x1="95" y1="270" x2="105" y2="270" stroke="black" stroke-width="1"/>
  <circle cx="120" cy="260" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="120" y1="266" x2="120" y2="280" stroke="black" stroke-width="1.5"/>
  <line x1="115" y1="270" x2="125" y2="270" stroke="black" stroke-width="1"/>
  <circle cx="280" cy="260" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="280" y1="266" x2="280" y2="280" stroke="black" stroke-width="1.5"/>
  <line x1="275" y1="270" x2="285" y2="270" stroke="black" stroke-width="1"/>
  <circle cx="300" cy="260" r="6" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="300" y1="266" x2="300" y2="280" stroke="black" stroke-width="1.5"/>
  <line x1="295" y1="270" x2="305" y2="270" stroke="black" stroke-width="1"/>
  <!-- Soldier spears -->
  <line x1="100" y1="255" x2="100" y2="240" stroke="black" stroke-width="1"/>
  <line x1="120" y1="255" x2="120" y2="240" stroke="black" stroke-width="1"/>
  <line x1="280" y1="255" x2="280" y2="240" stroke="black" stroke-width="1"/>
  <line x1="300" y1="255" x2="300" y2="240" stroke="black" stroke-width="1"/>
'''+F.format(c="CAT HQ"))

print("Generated ch09-15")
