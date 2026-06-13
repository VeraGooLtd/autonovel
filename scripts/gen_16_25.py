#!/usr/bin/env python3
"""Generate SVG doodles ch16-25 for MDIM Book 1."""
import os
D=os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg")
H='''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
'''
F='''
  <text x="200" y="385" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black" font-weight="bold">{c}</text>
</svg>'''

# Ch16: Simba Throne
open(D+"/ch16_simba_throne.svg","w").write(H+'''
  <rect x="40" y="40" width="320" height="300" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Velvet cushion on pedestal -->
  <rect x="120" y="200" width="160" height="40" fill="none" stroke="black" stroke-width="2.5"/>
  <rect x="130" y="205" width="140" height="30" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="150" y1="210" x2="250" y2="210" stroke="black" stroke-width="0.5"/>
  <line x1="150" y1="220" x2="250" y2="220" stroke="black" stroke-width="0.5"/>
  <!-- Simba on throne — military pose -->
  <ellipse cx="200" cy="175" rx="35" ry="30" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="200" cy="140" r="22" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 182 125 L 175 108 L 190 120" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 218 125 L 225 108 L 210 120" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="192" cy="135" r="4" fill="black"/>
  <circle cx="208" cy="135" r="4" fill="black"/>
  <path d="M 193 150 Q 200 155 207 150" stroke="black" stroke-width="2"/>
  <!-- Military medals -->
  <circle cx="185" cy="170" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="200" cy="175" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="215" cy="170" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Tiny sword -->
  <line x1="240" y1="165" x2="265" y2="150" stroke="black" stroke-width="2"/>
  <line x1="238" y1="168" x2="242" y2="162" stroke="black" stroke-width="1.5"/>
  <!-- Cape -->
  <path d="M 165 190 Q 150 210 160 230" stroke="black" stroke-width="2"/>
  <path d="M 235 190 Q 250 210 240 230" stroke="black" stroke-width="2"/>
  <!-- Bea and Barnaby looking up -->
  <circle cx="100" cy="260" r="12" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="140" cy="265" r="10" fill="none" stroke="black" stroke-width="2"/>
  <text x="100" y="255" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">Bea</text>
  <text x="140" y="260" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">Barnaby</text>
  <!-- Cat soldiers with spears -->
  <circle cx="80" cy="180" r="8" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="80" y1="165" x2="80" y2="145" stroke="black" stroke-width="1"/>
  <circle cx="320" cy="180" r="8" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="320" y1="165" x2="320" y2="145" stroke="black" stroke-width="1"/>
  <circle cx="60" cy="220" r="6" fill="none" stroke="black" stroke-width="1.2"/>
  <line x1="60" y1="208" x2="60" y2="195" stroke="black" stroke-width="0.8"/>
  <circle cx="340" cy="220" r="6" fill="none" stroke="black" stroke-width="1.2"/>
  <line x1="340" y1="208" x2="340" y2="195" stroke="black" stroke-width="0.8"/>
  <!-- "SURRENDER" flag -->
  <rect x="180" y="50" width="40" height="25" fill="white" stroke="black" stroke-width="1.5"/>
  <text x="200" y="60" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="6" fill="black">SURRENDER</text>
  <line x1="200" y1="50" x2="200" y2="75" stroke="black" stroke-width="1"/>
  <!-- Dramatic lighting lines -->
  <line x1="200" y1="40" x2="200" y2="30" stroke="black" stroke-width="1"/>
  <line x1="185" y1="42" x2="180" y2="32" stroke="black" stroke-width="1"/>
  <line x1="215" y1="42" x2="220" y2="32" stroke="black" stroke-width="1"/>
'''+F.format(c="GENERAL SIMBA"))

# Ch17: Soy Sauce Explosion
open(D+"/ch17_soy_sauce.svg","w").write(H+'''
  <!-- Mushroom cloud -->
  <path d="M 120 200 Q 100 150 130 100 Q 160 60 200 40 Q 240 60 270 100 Q 300 150 280 200" fill="none" stroke="black" stroke-width="3"/>
  <path d="M 140 200 Q 130 170 150 140 Q 170 110 200 100 Q 230 110 250 140 Q 270 170 260 200" fill="none" stroke="black" stroke-width="2"/>
  <!-- Cloud puffs -->
  <ellipse cx="160" cy="80" rx="25" ry="15" fill="none" stroke="black" stroke-width="2"/>
  <ellipse cx="200" cy="60" rx="30" ry="18" fill="none" stroke="black" stroke-width="2"/>
  <ellipse cx="240" cy="80" ry="15" rx="25" fill="none" stroke="black" stroke-width="2"/>
  <ellipse cx="180" cy="45" rx="20" ry="12" fill="none" stroke="black" stroke-width="1.5"/>
  <ellipse cx="220" cy="45" rx="20" ry="12" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- "BOOM" text -->
  <text x="200" y="90" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="20" fill="black">BOOM</text>
  <!-- Flying soy sauce bottles -->
  <rect x="80" y="60" width="15" height="30" fill="none" stroke="black" stroke-width="2" transform="rotate(-20 87 75)"/>
  <rect x="300" y="70" width="15" height="30" fill="none" stroke="black" stroke-width="2" transform="rotate(30 307 85)"/>
  <rect x="50" y="120" width="12" height="25" fill="none" stroke="black" stroke-width="1.5" transform="rotate(-45 56 132)"/>
  <rect x="330" y="110" width="12" height="25" fill="none" stroke="black" stroke-width="1.5" transform="rotate(60 336 122)"/>
  <!-- Simba — shocked -->
  <circle cx="100" cy="250" r="20" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="92" cy="245" r="4" fill="black"/>
  <circle cx="108" cy="245" r="4" fill="black"/>
  <ellipse cx="100" cy="260" rx="8" ry="5" fill="none" stroke="black" stroke-width="2"/>
  <!-- Sweat drops -->
  <ellipse cx="80" cy="238" rx="4" ry="6" fill="none" stroke="black" stroke-width="1"/>
  <ellipse cx="120" cy="235" rx="3" ry="5" fill="none" stroke="black" stroke-width="1"/>
  <!-- Duke — shocked -->
  <ellipse cx="300" cy="250" rx="25" ry="20" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="300" cy="230" r="15" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="294" cy="226" r="3" fill="black"/>
  <circle cx="306" cy="226" r="3" fill="black"/>
  <path d="M 295 240 Q 300 245 305 240" stroke="black" stroke-width="2"/>
  <!-- Dukeears -->
  <path d="M 288 218 L 280 205 L 292 215" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 312 218 L 320 205 L 308 215" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Broken containers on ground -->
  <path d="M 60 300 L 80 290 L 70 310" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 140 310 L 160 295 L 155 315" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 250 305 L 270 290 L 265 312" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Motion lines -->
  <path d="M 40 200 L 20 190" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 360 200 L 380 190" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
  <path d="M 200 30 L 200 10" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
'''+F.format(c="SOY SAUCE EXPLOSION"))

# Ch18: Sinkhole
open(D+"/ch18_sinkhole.svg","w").write(H+'''
  <path d="M 60 350 L 60 100 Q 200 20 340 100 L 340 350" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 80 350 L 80 110 Q 200 35 320 110 L 320 350" fill="none" stroke="black" stroke-width="1.5" stroke-dasharray="3 3"/>
  <!-- Dangling glass shards -->
  <path d="M 100 120 L 95 140 L 105 145 L 100 120" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 150 100 L 145 125 L 155 130" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 250 95 L 245 120 L 255 125" fill="none" stroke="black" stroke-width="1.5"/>
  <path d="M 300 115 L 295 135 L 305 140 L 300 115" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- DANGER sign -->
  <rect x="160" y="150" width="80" height="40" fill="white" stroke="black" stroke-width="2"/>
  <text x="200" y="168" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">DANGER</text>
  <text x="200" y="182" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="7" fill="black">DO NOT ENTER</text>
  <!-- Skull and crossbones -->
  <circle cx="200" cy="220" r="12" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="195" cy="217" r="2" fill="black"/>
  <circle cx="205" cy="217" r="2" fill="black"/>
  <path d="M 195 227 L 205 227" stroke="black" stroke-width="2"/>
  <line x1="200" y1="232" x2="195" y2="245" stroke="black" stroke-width="2"/>
  <line x1="200" y1="232" x2="205" y2="245" stroke="black" stroke-width="2"/>
  <line x1="195" y1="245" x2="205" y2="245" stroke="black" stroke-width="2"/>
  <!-- Cobwebs -->
  <path d="M 60 100 Q 70 90 80 100 Q 90 90 100 100" stroke="black" stroke-width="1"/>
  <path d="M 300 100 Q 310 90 320 100 Q 330 90 340 100" stroke="black" stroke-width="1"/>
  <line x1="70" y1="90" x2="70" y2="70" stroke="black" stroke-width="0.5"/>
  <line x1="310" y1="90" x2="310" y2="70" stroke="black" stroke-width="0.5"/>
  <!-- Rocks falling -->
  <rect x="180" y="280" width="15" height="10" fill="none" stroke="black" stroke-width="1.5"/>
  <rect x="210" y="300" width="12" height="8" fill="none" stroke="black" stroke-width="1.5"/>
  <rect x="195" y="320" width="10" height="7" fill="none" stroke="black" stroke-width="1"/>
  <!-- Flashlight beam from above -->
  <path d="M 200 0 L 170 100 L 230 100 Z" fill="none" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <!-- Darkness inside -->
  <text x="200" y="270" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="8" fill="black">it's dark...</text>
'''+F.format(c="THE SINKHOLE"))

# Ch19: Salami Rescue
open(D+"/ch19_salami_rescue.svg","w").write(H+'''
  <!-- Giant salami on rope -->
  <ellipse cx="200" cy="150" rx="60" ry="35" fill="none" stroke="black" stroke-width="3"/>
  <circle cx="170" cy="140" r="5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="200" cy="135" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="230" cy="145" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Rope going up -->
  <path d="M 200 115 L 200 40" stroke="black" stroke-width="2.5"/>
  <circle cx="200" cy="35" r="5" fill="none" stroke="black" stroke-width="2"/>
  <!-- Crack in ground below -->
  <path d="M 100 200 Q 150 220 200 210 Q 250 200 300 220" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 120 220 Q 160 240 200 230 Q 240 220 280 240" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Barnaby holding tail — strained expression -->
  <circle cx="280" cy="200" r="18" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="274" cy="195" r="3" fill="black"/>
  <circle cx="286" cy="195" r="3" fill="black"/>
  <path d="M 272 210 Q 280 218 288 210" stroke="black" stroke-width="2"/>
  <!-- Strain lines -->
  <line x1="265" y1="190" x2="260" y2="185" stroke="black" stroke-width="1"/>
  <line x1="295" y1="190" x2="300" y2="185" stroke="black" stroke-width="1"/>
  <!-- Barnaby's arms pulling -->
  <path d="M 265 210 Q 250 220 240 215" stroke="black" stroke-width="2.5"/>
  <path d="M 295 210 Q 310 220 320 215" stroke="black" stroke-width="2.5"/>
  <!-- Bea pulling rope -->
  <circle cx="200" cy="250" r="15" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="194" cy="245" r="2.5" fill="black"/>
  <circle cx="206" cy="245" r="2.5" fill="black"/>
  <path d="M 195 260 Q 200 265 205 260" stroke="black" stroke-width="2"/>
  <!-- Bea's arms pulling rope -->
  <path d="M 190 260 Q 185 275 190 285" stroke="black" stroke-width="2"/>
  <path d="M 210 260 Q 215 275 210 285" stroke="black" stroke-width="2"/>
  <!-- "ALMOST THERE" text -->
  <text x="200" y="310" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12" fill="black">ALMOST THERE!</text>
  <!-- Motion lines -->
  <path d="M 195 100 L 190 90" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <path d="M 205 100 L 210 90" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
'''+F.format(c="SALAMI RESCUE"))

# Ch20: Salami Bobsled
open(D+"/ch20_salami_bobsled.svg","w").write(H+'''
  <!-- Salami as bobsled -->
  <ellipse cx="200" cy="200" rx="80" ry="30" fill="none" stroke="black" stroke-width="3"/>
  <path d="M 120 200 Q 120 220 200 230 Q 280 220 280 200" fill="none" stroke="black" stroke-width="2"/>
  <!-- Runners -->
  <path d="M 140 230 L 140 245" stroke="black" stroke-width="2.5"/>
  <path d="M 260 230 L 260 245" stroke="black" stroke-width="2.5"/>
  <!-- Bea at front -->
  <circle cx="160" cy="180" r="12" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="155" cy="176" r="2" fill="black"/>
  <circle cx="165" cy="176" r="2" fill="black"/>
  <path d="M 155 188 Q 160 193 165 188" stroke="black" stroke-width="2"/>
  <!-- Maya in middle -->
  <circle cx="200" cy="175" r="11" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="196" cy="171" r="2" fill="black"/>
  <circle cx="204" cy="171" r="2" fill="black"/>
  <path d="M 196 183 Q 200 188 204 183" stroke="black" stroke-width="2"/>
  <!-- Barnaby at back — terrified -->
  <circle cx="240" cy="178" r="13" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="234" cy="173" r="3" fill="black"/>
  <circle cx="246" cy="173" r="3" fill="black"/>
  <ellipse cx="240" cy="188" rx="6" ry="4" fill="none" stroke="black" stroke-width="2"/>
  <!-- Sweat on Barnaby -->
  <ellipse cx="255" cy="170" rx="3" ry="5" fill="none" stroke="black" stroke-width="1"/>
  <!-- Speed lines -->
  <line x1="100" y1="190" x2="60" y2="185" stroke="black" stroke-width="1.5"/>
  <line x1="100" y1="200" x2="55" y2="200" stroke="black" stroke-width="1.5"/>
  <line x1="100" y1="210" x2="60" y2="215" stroke="black" stroke-width="1.5"/>
  <!-- Pipe they're sliding through -->
  <path d="M 40 150 Q 200 120 360 150" stroke="black" stroke-width="2" stroke-dasharray="5 3"/>
  <path d="M 40 250 Q 200 280 360 250" stroke="black" stroke-width="2" stroke-dasharray="5 3"/>
  <!-- "WHEEE" text -->
  <text x="160" y="155" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">WHEEE!</text>
  <!-- Motion blur -->
  <path d="M 280 190 Q 320 185 350 190" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
'''+F.format(c="SALAMI BOBSLED"))

# Ch21: Simba Entrance
open(D+"/ch21_simba_entrance.svg","w").write(H+'''
  <!-- Museum columns -->
  <rect x="80" y="60" width="25" height="200" fill="none" stroke="black" stroke-width="2.5"/>
  <rect x="295" y="60" width="25" height="200" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Column bases -->
  <rect x="75" y="255" width="35" height="15" fill="none" stroke="black" stroke-width="2"/>
  <rect x="290" y="255" width="35" height="15" fill="none" stroke="black" stroke-width="2"/>
  <!-- Column capitals -->
  <path d="M 75 60 L 80 50 L 105 50 L 110 60" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 290 60 L 295 50 L 320 50 L 325 60" fill="none" stroke="black" stroke-width="2"/>
  <!-- Entablature -->
  <rect x="70" y="45" width="260" height="15" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- "MUSEUM" sign -->
  <rect x="150" y="65" width="100" height="25" fill="white" stroke="black" stroke-width="2"/>
  <text x="200" y="82" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12" fill="black">MUSEUM</text>
  <!-- Red carpet -->
  <path d="M 200 280 L 170 350 L 230 350 Z" fill="none" stroke="black" stroke-width="2"/>
  <line x1="185" y1="310" x2="200" y2="280" stroke="black" stroke-width="1"/>
  <line x1="215" y1="310" x2="200" y2="280" stroke="black" stroke-width="1"/>
  <!-- Simba at top of steps — dramatic pose -->
  <ellipse cx="200" cy="240" rx="25" ry="20" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="200" cy="218" r="18" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 186 205 L 180 190 L 192 202" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 214 205 L 220 190 L 208 202" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="194" cy="214" r="3" fill="black"/>
  <circle cx="206" cy="214" r="3" fill="black"/>
  <path d="M 195 228 Q 200 235 205 228" stroke="black" stroke-width="2"/>
  <!-- Cape flowing -->
  <path d="M 175 250 Q 160 270 170 290" stroke="black" stroke-width="2"/>
  <path d="M 225 250 Q 240 270 230 290" stroke="black" stroke-width="2"/>
  <!-- Cat guards with spears -->
  <circle cx="140" cy="260" r="10" fill="none" stroke="black" stroke-width="2"/>
  <line x1="140" y1="245" x2="140" y2="225" stroke="black" stroke-width="1.5"/>
  <circle cx="260" cy="260" r="10" fill="none" stroke="black" stroke-width="2"/>
  <line x1="260" y1="245" x2="260" y2="225" stroke="black" stroke-width="1.5"/>
  <!-- "CLOSED" sign -->
  <rect x="250" y="100" width="50" height="25" fill="white" stroke="black" stroke-width="2"/>
  <text x="275" y="117" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">CLOSED</text>
'''+F.format(c="THE GRAND ENTRANCE"))

# Ch22: Salami Sensors
open(D+"/ch22_salami_sensors.svg","w").write(H+'''
  <!-- Museum room -->
  <rect x="40" y="40" width="320" height="280" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Sensor beams (red lines) -->
  <line x1="60" y1="60" x2="60" y2="320" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="120" y1="60" x2="120" y2="320" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="180" y1="60" x2="180" y2="320" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="240" y1="60" x2="240" y2="320" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="300" y1="60" x2="300" y2="320" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <!-- Horizontal beams -->
  <line x1="40" y1="120" x2="360" y2="120" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="40" y1="200" x2="360" y2="200" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <line x1="40" y1="280" x2="360" y2="280" stroke="black" stroke-width="1" stroke-dasharray="2 2"/>
  <!-- Giant salami blocking beams -->
  <ellipse cx="200" cy="180" rx="70" ry="40" fill="none" stroke="black" stroke-width="3"/>
  <circle cx="170" cy="170" r="5" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="200" cy="165" r="4" fill="none" stroke="black" stroke-width="1.5"/>
  <circle cx="230" cy="175" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Barnaby sitting on salami like a king -->
  <circle cx="200" cy="140" r="15" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="194" cy="135" r="2.5" fill="black"/>
  <circle cx="206" cy="135" r="2.5" fill="black"/>
  <path d="M 195 150 Q 200 158 205 150" stroke="black" stroke-width="2"/>
  <!-- Crown -->
  <path d="M 182 125 L 188 112 L 194 122 L 200 108 L 206 122 L 212 112 L 218 125" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Cats running in panic -->
  <circle cx="80" cy="250" r="8" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="75" y1="240" x2="70" y2="225" stroke="black" stroke-width="1"/>
  <circle cx="320" cy="260" r="8" fill="none" stroke="black" stroke-width="1.5"/>
  <line x1="325" y1="250" x2="330" y2="235" stroke="black" stroke-width="1"/>
  <circle cx="100" cy="300" r="6" fill="none" stroke="black" stroke-width="1.2"/>
  <circle cx="300" cy="290" r="6" fill="none" stroke="black" stroke-width="1.2"/>
  <!-- Sweat drops on cats -->
  <ellipse cx="90" cy="240" rx="2" ry="3" fill="none" stroke="black" stroke-width="0.8"/>
  <ellipse cx="335" y="250" rx="2" ry="3" fill="none" stroke="black" stroke-width="0.8"/>
  <!-- Alarm lights -->
  <circle cx="60" cy="55" r="5" fill="black"/>
  <circle cx="340" cy="55" r="5" fill="black"/>
  <!-- "INTRUDER" text -->
  <text x="200" y="340" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12" fill="black">⚠ INTRUDER ⚠</text>
'''+F.format(c="SALAMI SABOTAGE"))

# Ch23: Pipe Slide
open(D+"/ch23_pipe_slide.svg","w").write(H+'''
  <!-- Metal pipe interior -->
  <rect x="80" y="60" width="240" height="280" fill="none" stroke="black" stroke-width="3"/>
  <!-- Pipe texture -->
  <line x1="80" y1="100" x2="320" y2="100" stroke="black" stroke-width="0.5"/>
  <line x1="80" y1="140" x2="320" y2="140" stroke="black" stroke-width="0.5"/>
  <line x1="80" y1="180" x2="320" y2="180" stroke="black" stroke-width="0.5"/>
  <line x1="80" y1="220" x2="320" y2="220" stroke="black" stroke-width="0.5"/>
  <line x1="80" y1="260" x2="320" y2="260" stroke="black" stroke-width="0.5"/>
  <line x1="80" y1="300" x2="320" y2="300" stroke="black" stroke-width="0.5"/>
  <!-- Towels flying -->
  <rect x="60" y="40" width="25" height="15" fill="none" stroke="black" stroke-width="1.5" transform="rotate(-10 72 47)"/>
  <rect x="300" y="50" width="20" height="12" fill="none" stroke="black" stroke-width="1.5" transform="rotate(15 310 56)"/>
  <rect x="50" y="100" width="18" height="10" fill="none" stroke="black" stroke-width="1" transform="rotate(-25 59 105)"/>
  <!-- Soap bubbles -->
  <circle cx="120" cy="80" r="5" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="250" cy="90" r="4" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="180" cy="70" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Three characters falling -->
  <!-- Bea — front -->
  <circle cx="200" cy="150" r="14" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="195" cy="146" r="2" fill="black"/>
  <circle cx="205" cy="146" r="2" fill="black"/>
  <path d="M 194 158 Q 200 165 206 158" stroke="black" stroke-width="2.5" stroke-linecap="round"/>
  <!-- Maya — middle -->
  <circle cx="200" cy="210" r="12" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="196" cy="206" r="2" fill="black"/>
  <circle cx="204" cy="206" r="2" fill="black"/>
  <path d="M 195 218 Q 200 223 205 218" stroke="black" stroke-width="2"/>
  <!-- Barnaby — back, terrified -->
  <circle cx="200" cy="270" r="15" fill="none" stroke="black" stroke-width="2.5"/>
  <circle cx="194" cy="264" r="3" fill="black"/>
  <circle cx="206" cy="264" r="3" fill="black"/>
  <ellipse cx="200" cy="280" rx="8" ry="5" fill="none" stroke="black" stroke-width="2"/>
  <!-- Barnaby sweat -->
  <ellipse cx="220" cy="258" rx="4" ry="6" fill="none" stroke="black" stroke-width="1"/>
  <ellipse cx="180" cy="260" rx="3" ry="4" fill="none" stroke="black" stroke-width="1"/>
  <!-- "AAAAH" text -->
  <text x="200" y="320" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="18" fill="black">AAAAAHHH!</text>
  <!-- Falling arms/legs -->
  <path d="M 186 160 Q 170 175 160 170" stroke="black" stroke-width="2"/>
  <path d="M 214 160 Q 230 175 240 170" stroke="black" stroke-width="2"/>
  <!-- Mop flying -->
  <line x="280" y1="120" x2="310" y2="150" stroke="black" stroke-width="2"/>
  <path d="M 305 155 Q 315 160 310 170 Q 320 165 315 175" stroke="black" stroke-width="1.5"/>
'''+F.format(c="PIPE SLIDE"))

# Ch24: Henry Hero
open(D+"/ch24_henry_hero.svg","w").write(H+'''
  <!-- Henry in heroic pose -->
  <ellipse cx="200" cy="180" rx="60" ry="35" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 145 165 Q 130 135 140 110" stroke="none" stroke="black" stroke-width="2.5"/>
  <ellipse cx="138" cy="95" rx="22" ry="16" fill="none" stroke="black" stroke-width="2.5"/>
  <path d="M 122 82 L 116 65 L 128 78" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 150 82 L 156 68 L 146 78" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="130" cy="90" r="3" fill="black"/>
  <circle cx="144" cy="90" r="3" fill="black"/>
  <path d="M 130 102 Q 137 108 144 102" stroke="black" stroke-width="2"/>
  <!-- Mane -->
  <path d="M 145 78 Q 158 62 152 50" stroke="black" stroke-width="2"/>
  <path d="M 150 82 Q 162 68 156 55" stroke="black" stroke-width="2"/>
  <!-- Giant salami on silver platter -->
  <ellipse cx="200" cy="250" rx="50" ry="10" fill="none" stroke="black" stroke-width="2"/>
  <ellipse cx="200" cy="245" rx="55" ry="8" fill="none" stroke="black" stroke-width="1.5"/>
  <ellipse cx="200" cy="260" rx="45" ry="25" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="180" cy="255" r="4" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="200" cy="250" r="3" fill="none" stroke="black" stroke-width="1"/>
  <circle cx="220" cy="258" r="3" fill="none" stroke="black" stroke-width="1"/>
  <!-- Henry nudging salami -->
  <path d="M 160 190 Q 180 210 200 220" stroke="black" stroke-width="2"/>
  <!-- Humans cheering -->
  <circle cx="80" cy="280" r="10" fill="none" stroke="black" stroke-width="2"/>
  <line x1="75" y1="270" x2="70" y2="255" stroke="black" stroke-width="1.5"/>
  <line x1="85" y1="270" x2="90" y2="255" stroke="black" stroke-width="1.5"/>
  <circle cx="320" cy="280" r="10" fill="none" stroke="black" stroke-width="2"/>
  <line x1="315" y1="270" x2="310" y2="255" stroke="black" stroke-width="1.5"/>
  <line x1="325" y1="270" x2="330" y2="255" stroke="black" stroke-width="1.5"/>
  <!-- Confetti -->
  <rect x="120" y="60" width="4" height="4" fill="black" transform="rotate(15 122 62)"/>
  <rect x="280" y="50" width="3" height="3" fill="black" transform="rotate(-20 281 51)"/>
  <rect x="150" y="40" width="5" height="3" fill="black" transform="rotate(30 152 41)"/>
  <rect x="250" y="45" width="4" height="4" fill="black" transform="rotate(-10 252 47)"/>
  <!-- Medal around Henry's neck -->
  <circle cx="140" cy="130" r="8" fill="none" stroke="black" stroke-width="2"/>
  <path d="M 140 122 L 140 110" stroke="black" stroke-width="2"/>
  <!-- "HERO" banner -->
  <rect x="140" y="30" width="120" height="25" fill="white" stroke="black" stroke-width="2"/>
  <text x="200" y="47" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="14" fill="black">HERO!</text>
  <!-- Spotlight from above -->
  <path d="M 170 20 Q 180 0 200 0 Q 220 0 230 20" stroke="black" stroke-width="1" stroke-dasharray="3 2"/>
'''+F.format(c="HENRY THE HERO"))

# Ch25: Shadow Cat (To Be Continued)
open(D+"/ch25_shadow_cat.svg","w").write(H+'''
  <!-- Park scene with trees -->
  <rect x="40" y="40" width="320" height="280" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Trees -->
  <rect x="60" y="150" width="10" height="100" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="65" cy="140" r="25" fill="none" stroke="black" stroke-width="2"/>
  <rect x="320" y="160" width="10" height="90" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="325" cy="150" r="20" fill="none" stroke="black" stroke-width="2"/>
  <!-- Park bench -->
  <rect x="150" y="200" width="60" height="5" fill="none" stroke="black" stroke-width="2"/>
  <rect x="155" y="205" width="5" height="15" fill="none" stroke="black" stroke-width="1.5"/>
  <rect x="200" y="205" width="5" height="15" fill="none" stroke="black" stroke-width="1.5"/>
  <!-- Bea and Barnaby in foreground — looking back -->
  <circle cx="120" cy="250" r="12" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="115" cy="246" r="2" fill="black"/>
  <circle cx="125" cy="246" r="2" fill="black"/>
  <path d="M 116 258 Q 120 262 124 258" stroke="black" stroke-width="1.5"/>
  <text x="120" y="242" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">Bea</text>
  <circle cx="280" cy="255" r="10" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="276" cy="251" r="2" fill="black"/>
  <circle cx="284" cy="251" r="2" fill="black"/>
  <path d="M 276 262 Q 280 266 284 262" stroke="black" stroke-width="1.5"/>
  <text x="280" y="247" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="5" fill="black">Barnaby</text>
  <!-- They're looking back — worried expressions -->
  <path d="M 118 258 Q 120 260 122 258" stroke="black" stroke-width="1"/>
  <path d="M 278 262 Q 280 264 282 262" stroke="black" stroke-width="1"/>
  <!-- Ginger cat silhouette in shadows — watching -->
  <path d="M 350 280 Q 360 260 370 250 Q 375 245 380 250 Q 385 245 390 250 Q 395 240 400 245" fill="none" stroke="black" stroke-width="2.5"/>
  <!-- Cat eyes glowing in shadow -->
  <circle cx="372" cy="248" r="3" fill="black"/>
  <circle cx="382" cy="246" r="3" fill="black"/>
  <!-- Cat body in shadow -->
  <ellipse cx="380" cy="275" rx="20" ry="15" fill="black" opacity="0.7"/>
  <!-- Tail curling -->
  <path d="M 400 270 Q 415 260 420 270" stroke="black" stroke-width="2"/>
  <!-- Shadows on ground -->
  <ellipse cx="380" cy="295" rx="25" ry="5" fill="black" opacity="0.3"/>
  <!-- "..." text -->
  <text x="200" y="100" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="24" fill="black">. . .</text>
  <!-- Moon in sky -->
  <circle cx="320" cy="60" r="15" fill="none" stroke="black" stroke-width="2"/>
  <circle cx="328" cy="55" r="12" fill="white" stroke="white" stroke-width="2"/>
  <!-- "THE END?" text -->
  <text x="200" y="320" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="10" fill="black">THE END?</text>
  <!-- Small heart doodle -->
  <path d="M 50 50 Q 45 42 38 45 Q 32 48 38 55 Q 44 60 50 65 Q 56 60 62 55 Q 68 48 62 45 Q 55 42 50 50" fill="none" stroke="black" stroke-width="1"/>
'''+F.format(c="TO BE CONTINUED..."))

print("Generated ch16-25")
