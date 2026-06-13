#!/usr/bin/env python3
"""
Ideogram 4 Cover Generation for D2D Publishing
Run this in Google Colab: https://colab.research.google.com
Runtime: Python 3, GPU (T4 or better)

Requirements:
- HuggingFace account (free)
- Colab GPU runtime (free tier)
- ~16GB VRAM needed (T4 works)

After generation, download covers and place in book directories.
"""

# ============================================================
# CELL 1: Install Dependencies
# ============================================================
# Run this cell first in Colab

!pip install -q diffusers transformers accelerate huggingface_hub
!pip install -q omegaconf peft

print("✅ Dependencies installed!")

# ============================================================
# CELL 2: Login to HuggingFace
# ============================================================

from huggingface_hub import login
login()  # Paste your HF token when prompted
# Get free token at: https://huggingface.co/settings/tokens

# ============================================================
# CELL 3: Load Ideogram 4 Model
# ============================================================

import torch
import os
import time
from diffusers import DiffusionPipeline

print("Downloading Ideogram 4 (nf4) model...")
print("This may take 10-20 minutes on first run...")

pipe = DiffusionPipeline.from_pretrained(
    "ideogram-ai/ideogram-4-nf4",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
)
pipe.to("cuda")

print("✅ Ideogram 4 loaded!")
print(f"GPU: {torch.cuda.get_device_name(0)}")
print(f"VRAM: {round(torch.cuda.get_device_properties(0).total_mem / 1e9, 1)} GB")

# ============================================================
# CELL 4: Generate All 11 Ebook Covers
# ============================================================

OUTPUT = "/content/covers"
os.makedirs(OUTPUT, exist_ok=True)

# Cover definitions: (filename_slug, title, prompt)
COVERS = [
    # === Mycoformed Mars Saga ===
    (
        "the-genesis-engine",
        "The Genesis Engine",
        "Middle grade science fiction book cover, 1600x2400 pixels. Title 'The Genesis Engine' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: a massive engineered fungal spore pod sitting on the red Martian surface, with a pale blue Earth visible in the orange-tinted Martian sky. The pod has glowing bioluminescent veins. Rocky Martian terrain surrounds it. Art style: clean, bold lines, slightly cartoonish — appealing to middle grade readers ages 8-12. Colors: reds, oranges, blues, whites. Professional book cover layout with clear title placement. No spelling errors in text.",
    ),
    (
        "the-martian-spore",
        "The Martian Spore",
        "Middle grade science fiction book cover, 1600x2400 pixels. Title 'The Martian Spore' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: cracked Martian soil glowing with bright green fungal mycelium spreading across the surface like a network of veins. Small orange warning signs planted in the ground. A white habitat dome sits in the background. Art style: clean, bold lines, slightly cartoonish. Colors: reds, greens, whites, oranges. Professional book cover layout. No spelling errors in text.",
    ),
    (
        "the-crimson-bloom",
        "The Crimson Bloom",
        "Middle grade science fiction book cover, 1600x2400 pixels. Title 'The Crimson Bloom' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: view from space showing Mars with a massive crimson-red fungal bloom spreading across the surface in an intricate spiral pattern. A tiny white colony dome sits at the edge of the bloom. Stars in the black space background. Art style: clean, bold lines, slightly cartoonish. Colors: deep reds, blacks, whites, golds. Professional book cover layout. No spelling errors in text.",
    ),
    # === Sporefall Cycle ===
    (
        "sporefall",
        "Sporefall",
        "Young adult science fiction horror book cover, 1600x2400 pixels. Title 'Sporefall' in large distressed grunge font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration: a massive terrifying fungal fruiting body emerging from a dark rainforest canopy, releasing thick clouds of yellow-green spores. Tiny human figures with flashlights flee through the undergrowth below. Dark atmospheric lighting, moonlight filtering through trees. Art style: dramatic, stylized, dark fantasy meets horror. Colors: deep greens, blacks, sickly yellows, hints of red. No spelling errors in text.",
    ),
    (
        "mycelial-tide",
        "Mycelial Tide",
        "Young adult science fiction horror book cover, 1600x2400 pixels. Title 'Mycelial Tide' in large distressed grunge font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration: a massive wall of white and gray mycelium consuming a modern city street, rising like a tidal wave. Cars and streetlights being overtaken and swallowed by the fungal mass. Dramatic low-angle perspective from street level looking up at the approaching wall of fungus. Art style: dramatic, stylized, cinematic horror. Colors: grays, whites, blacks, touches of red from brake lights. No spelling errors in text.",
    ),
    (
        "mycelial-earth",
        "Mycelial Earth",
        "Young adult science fiction horror book cover, 1600x2400 pixels. Title 'Mycelial Earth' in large distressed grunge font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration: planet Earth viewed from space, but the continents are covered in a glowing web of fungal mycelium with bioluminescent nodes connected by glowing threads. A small spaceship with lights on approaches from the foreground. The mycelium pulses with light. Epic scale. Art style: dramatic, stylized, cinematic space art. Colors: blues, greens, blacks, glowing bioluminescent highlights. No spelling errors in text.",
    ),
    # === My Dog Is Judging Me ===
    (
        "the-salami-saboteur",
        "The Salami Saboteur",
        "Middle grade mystery humor book cover, 1600x2400 pixels. Title 'The Salami Saboteur' in large playful handwritten-style font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration in hand-drawn doodle/sketch style like Diary of a Wimpy Kid: An orange ginger cat wearing a tiny black domino mask sneaking away with an enormous salami sausage over its shoulder. Behind it, a 9-year-old girl with round glasses and a brown bulldog are looking shocked. The bulldog has X-eyes (knocked out cold). Sketchy pencil-line art with light shading. White background. Fun and kid-friendly. No spelling errors in text.",
    ),
    (
        "the-glass-vaults-gambit",
        "The Glass Vaults Gambit",
        "Middle grade mystery humor book cover, 1600x2400 pixels. Title 'The Glass Vaults Gambit' in large playful handwritten-style font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration in hand-drawn doodle/sketch style like Diary of a Wimpy Kid: A nighttime shopping mall interior with a glass skylight showing red laser security beams criss-crossing. An orange ginger cat in a black turtleneck spy outfit crawls through an air duct. A girl with glasses and a bulldog peek from behind a large potted plant. Question marks and exclamation marks floating. Sketchy pencil-line art. White background. No spelling errors in text.",
    ),
    # === Standalone Books ===
    (
        "station-zero",
        "Station Zero",
        "Young adult science fiction book cover, 1600x2400 pixels. Title 'Station Zero' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: a derelict space station floating against a field of distant stars. One single light still blinks on the station exterior. A small shuttle with its approach lights on comes toward the station in the foreground. The station has visible damage — missing solar panels, dented hull. Cold, vast, lonely feeling. Art style: clean science fiction, hard edges, realistic proportions. Colors: deep blacks, dark blues, whites, warm orange shuttle lights. No spelling errors in text.",
    ),
    (
        "the-echo-chamber",
        "The Echo Chamber",
        "Young adult science fiction thriller book cover, 1600x2400 pixels. Title 'The Echo Chamber' in large bold tech-thriller font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration: a young person's face reflected in a smartphone screen, but their reflection is a slightly uncanny AI avatar with glowing eyes and too-perfect features. Digital glitch effects around the edges. Floating social media notification icons and streams of binary data surround the phone. Dark moody lighting. Art style: modern, tech-thriller, slightly cyberpunk. Colors: dark blues, blacks, electric blues, neon pink accents. No spelling errors in text.",
    ),
    (
        "the-silent-strata",
        "The Silent Strata",
        "Young adult science fiction book cover, 1600x2400 pixels. Title 'The Silent Strata' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: a cross-section diagram of the Earth's crust showing geological layers — brown soil on top, then layers of sandstone and granite getting progressively darker, then the deep mantle in near-black. In the deepest darkest layer, an ancient alien geometric structure glows with blue-white light. A tiny drilling machine approaches from far above. Art style: clean science fiction, meets scientific illustration. Colors: browns, grays, blacks, glowing blue-white alien light. No spelling errors in text.",
    ),
]

# Generate covers
results = []
total = len(COVERS)

for i, (slug, title, prompt) in enumerate(COVERS, 1):
    print(f"\n[{i}/{total}] Generating: {title}...")
    start = time.time()

    try:
        result = pipe(
            prompt=prompt,
            width=1600,
            height=2400,
            num_inference_steps=30,
            guidance_scale=7.5,
        )
        img = result.images[0]
        path = f"{OUTPUT}/{slug}-ebook-cover.png"
        img.save(path)

        elapsed = time.time() - start
        size_kb = os.path.getsize(path) // 1024
        print(f"  ✅ Saved: {slug}-ebook-cover.png ({size_kb}KB, {elapsed:.0f}s)")
        results.append((title, "success", path))
    except Exception as e:
        print(f"  ❌ Error: {e}")
        results.append((title, "error", str(e)))

# Summary
print("\n" + "=" * 60)
print("GENERATION COMPLETE")
print("=" * 60)
success = sum(1 for r in results if r[1] == "success")
failed = sum(1 for r in results if r[1] == "error")
print(f"Success: {success}/{total}")
print(f"Failed: {failed}/{total}")

for title, status, detail in results:
    icon = "✅" if status == "success" else "❌"
    print(f"  {icon} {title}")

# ============================================================
# CELL 5: Download All Covers as ZIP
# ============================================================

import shutil
from google.colab import files

shutil.make_archive("/content/covers_all", "zip", OUTPUT)
files.download("/content/covers_all.zip")
print("✅ Downloaded: covers_all.zip")

# ============================================================
# CELL 6 (Optional): Upload to GitHub
# ============================================================

# Uncomment this section if you want to upload covers directly to GitHub
# You'll need a GitHub token stored as GH_TOKEN environment variable
#
# import subprocess
# REPO = "VeraGooLtd/Mycoformed-Mars-Saga"  # Change per book
# subprocess.run(["git", "clone", f"https://oauth2:{os.environ['GH_TOKEN']}@github.com/{REPO}.git", "/content/repo"], check=True)
# for f in os.listdir(OUTPUT):
#     shutil.copy(f"{OUTPUT}/{f}", f"/content/repo/{f}")
# subprocess.run(["git", "config", "user.email", "owl@hermes.agent"], cwd="/content/repo")
# subprocess.run(["git", "config", "user.name", "OWL Hermes Agent"], cwd="/content/repo")
# subprocess.run(["git", "add", "."], cwd="/content/repo")
# subprocess.run(["git", "commit", "-m", "add: ebook covers via Ideogram 4"], cwd="/content/repo")
# subprocess.run(["git", "push"], cwd="/content/repo")
# print("✅ Uploaded to GitHub!")

print("\nDone! Place covers in book directories and update metadata.")
