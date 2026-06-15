#!/usr/bin/env python3
"""Generate all 25 SVG doodles using LLM delegation."""

import os
import json

output_dir = os.path.expanduser("~/autonovel/books/mdim-book3/doodles/book1_svg")

# All 25 doodle descriptions
doodles = [
    ("ch01_sticky_sadness.svg", "STICKY SADNESS", "A bowl of lumpy oatmeal with a frowny face drawn on the side. Steam rising as tiny fists. Simple childlike doodle."),
    ("ch02_column_of_shame.svg", "COLUMN OF SHAME", "A tall ancient Roman stone column with a child's juice box balanced on top. A tiny ginger cat sitting on the juice box looking proud."),
    ("ch03_mud_trail.svg", "THE EVIDENCE", "A trail of messy paw-shaped mud blobs leading into a dark stone archway. Different sizes of paw prints."),
    ("ch04_cat_salami_jetpack.svg", "SALAMI JETPACK", "A tiny ginger cat with a jetpack made of a giant salami strapped to its back, flying over a picnic scene."),
    ("ch05_ledger.svg", "FELINE LEDGER", "A close-up of a secret ledger page with columns for FAT CONTENT % and DIGNITY INDEX. Tiny handwriting."),
    ("ch06_pigeon_spy.svg", "FEATHERED FRANK", "A disheveled pigeon perched on a rusted park fence, staring intensely with one eye. Wearing a tiny spy hat."),
    ("ch07_lulu_chaos.svg", "LULU CHAOS", "A 5-year-old girl spinning in circles with ice-cream on her face, toys flying everywhere."),
    ("ch08_henry_ride.svg", "SIR HENRY", "A very majestic horse with a tiny girl and bulldog on its back. The horse has a superhero cape."),
    ("ch09_mud_crosssection.svg", "MUD SCIENCE", "A cross-section diagram of mud layers. Top layer: SLIME. Middle layer: MYSTERY GOOP. Bottom layer: CLUE."),
    ("ch10_sub_salami.svg", "SALAMI SUB", "A cross-section of a tiny submarine. The Salami is in the pilot seat wearing goggles."),
    ("ch11_canal_map.svg", "CANAL MAP", "A treasure map showing canal tunnels. One branch leads to DUCK POND, the other to MEOW-FIA HQ."),
    ("ch12_simba_grate.svg", "THE GINGER NINJA", "A ginger cat's face seen through a metal grate. The cat looks like a fuzzy ginger monster with glowing eyes."),
    ("ch13_mission_impossible.svg", "OPERATION MAT", "A Mission Impossible style diagram. Henry the Horse pulling a mat, a salami on a rope, a bulldog holding the tail."),
    ("ch14_cat_dar.svg", "CAT-DAR 3000", "Maya standing behind her Cat-Dar science project. She looks very intense. Mr. Hendricks looks confused."),
    ("ch15_boathouse.svg", "CAT HQ", "The interior of a boathouse. Tiny monitors on the wall, a plush Cat Throne, a ginger cat looking smug."),
    ("ch16_simba_throne.svg", "GENERAL SIMBA", "Simba standing on his velvet cushion looking down at Bea and Barnaby. Surrounded by tiny cat soldiers."),
    ("ch17_soy_sauce.svg", "SOY SAUCE EXPLOSION", "A dark cloud of soy sauce shaped like a mushroom cloud. Simba and Duke looking shocked."),
    ("ch18_sinkhole.svg", "THE SINKHOLE", "A sinkhole entrance with rusted iron arches and dangling glass. A sign that says DANGER."),
    ("ch19_salami_rescue.svg", "SALAMI RESCUE", "The giant salami hanging over a crack on a rope. Barnaby holding the tail. Bea pulling a rope."),
    ("ch20_salami_bobsled.svg", "SALAMI BOBSLED", "Bea, Maya, and Barnaby on the Salami Bobsled going down a pipe. Barnaby looks terrified."),
    ("ch21_simba_entrance.svg", "THE GRAND ENTRANCE", "Simba standing at the entrance to the museum. He looks very professional. Two cat guards flanking him."),
    ("ch22_salami_sensors.svg", "SALAMI SABOTAGE", "The giant salami in the middle of the museum sensors. Barnaby sitting on it like a king. Cats running around in panic."),
    ("ch23_pipe_slide.svg", "PIPE SLIDE", "Bea, Maya, and Barnaby falling down a metal pipe filled with towels. Barnaby looks terrified."),
    ("ch24_henry_hero.svg", "HENRY THE HERO", "Henry the Horse nudging the giant salami onto a silver platter while humans cheer in the background."),
    ("ch25_shadow_cat.svg", "TO BE CONTINUED...", "Bea and Barnaby looking out over the park. In the shadows of the ferns, a ginger cat watches them."),
]

# Save as JSON for processing
with open(os.path.join(output_dir, 'doodles.json'), 'w') as f:
    json.dump(doodles, f, indent=2)

print(f'Saved {len(doodles)} doodle descriptions to doodles.json')
