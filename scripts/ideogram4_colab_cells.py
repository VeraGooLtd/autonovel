#!/usr/bin/env python3
"""
Ideogram 4 cover generation helper for Google Colab.

Copy the whole script into one Colab cell, or split at the section comments if you
prefer the cell-by-cell workflow. The install function must run before model load.
Critical order: install bitsandbytes first, then diffusers from GitHub.
Do not use DiffusionPipeline. Do not call pipe.to('cuda') for this model.
"""

from __future__ import annotations

import csv
import os
import subprocess
import sys
import time
from pathlib import Path

OUTPUT = "/content/covers"
WIDTH = 1600
HEIGHT = 2400
STEPS = 30
GUIDANCE = 7.5


def pip_install(*packages: str) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *packages])


def install_dependencies() -> None:
    # CRITICAL: bitsandbytes must be installed first for nf4 quantization.
    pip_install("bitsandbytes>=0.46.1")
    pip_install("git+https://github.com/huggingface/diffusers.git")
    pip_install(
        "transformers",
        "accelerate",
        "safetensors",
        "huggingface_hub",
        "peft",
        "omegaconf",
        "pillow",
    )
    print("Dependencies installed.")


def login_huggingface() -> None:
    from huggingface_hub import login

    login()
    print("HuggingFace login complete.")


def load_pipe():
    import torch
    from diffusers import Ideogram4Pipeline

    print("Downloading/loading ideogram-ai/ideogram-4-nf4 ...")
    print("First load can take 10-20 minutes on Colab.")

    pipe = Ideogram4Pipeline.from_pretrained(
        "ideogram-ai/ideogram-4-nf4",
        torch_dtype=torch.float16,
        trust_remote_code=True,
        device_map="balanced",
        low_cpu_mem_usage=True,
    )

    print("Ideogram 4 loaded.")
    print("Pipeline device:", getattr(pipe, "device", "balanced/meta-device-managed"))
    print("CUDA available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
        print("VRAM GB:", round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2))
    return pipe


def cover_definitions() -> list[tuple[str, str, str]]:
    return [
        (
            "the-genesis-engine",
            "The Genesis Engine",
            "Middle grade science fiction book cover, 1600x2400. Title 'The Genesis Engine' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: a massive engineered fungal spore pod on the red Martian surface, with a pale blue Earth visible in an orange-tinted Martian sky. The pod has glowing bioluminescent veins. Rocky Martian terrain surrounds it. Clean, bold lines, slightly cartoonish, appealing to ages 8-12. Reds, oranges, blues, whites. Professional book cover layout. No spelling errors in text.",
        ),
        (
            "the-martian-spore",
            "The Martian Spore",
            "Middle grade science fiction book cover, 1600x2400. Title 'The Martian Spore' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Cracked Martian soil with bright green fungal mycelium spreading across the surface like a network of veins. Small orange warning signs planted in the ground. A white habitat dome sits in the background. Clean, bold lines, slightly cartoonish. Reds, greens, whites, oranges. Professional book cover layout. No spelling errors in text.",
        ),
        (
            "the-crimson-bloom",
            "The Crimson Bloom",
            "Middle grade science fiction book cover, 1600x2400. Title 'The Crimson Bloom' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. View from space showing Mars with a massive crimson-red fungal bloom spreading across the surface in a spiral pattern. A tiny white colony dome sits at the edge of the bloom. Stars in the black space background. Clean, bold lines, slightly cartoonish. Deep reds, blacks, whites, golds. Professional book cover layout. No spelling errors in text.",
        ),
        (
            "sporefall",
            "Sporefall",
            "Young adult science fiction horror book cover, 1600x2400. Title 'Sporefall' in large distressed grunge font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration: a massive terrifying fungal fruiting body emerging from a dark rainforest canopy, releasing thick clouds of yellow-green spores. Tiny human figures with flashlights flee through the undergrowth below. Dark atmospheric lighting, moonlight filtering through trees. Dramatic, stylized, dark fantasy horror. Deep greens, blacks, sickly yellows, hints of red. No spelling errors in text.",
        ),
        (
            "mycelial-tide",
            "Mycelial Tide",
            "Young adult science fiction horror book cover, 1600x2400. Title 'Mycelial Tide' in large distressed grunge font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration: a massive wall of white and gray mycelium consuming a modern city street, rising like a tidal wave. Cars and streetlights being overtaken and swallowed by the fungal mass. Dramatic low-angle perspective from street level looking up at the approaching wall of fungus. Cinematic horror. Grays, whites, blacks, touches of red from brake lights. No spelling errors in text.",
        ),
        (
            "mycelial-earth",
            "Mycelial Earth",
            "Young adult science fiction horror book cover, 1600x2400. Title 'Mycelial Earth' in large distressed grunge font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Planet Earth viewed from space, continents covered in a glowing web of fungal mycelium with bioluminescent nodes connected by glowing threads. A small spaceship with lights on approaches from the foreground. The mycelium pulses with light. Epic scale. Dramatic, stylized cinematic space art. Blues, greens, blacks, glowing bioluminescent highlights. No spelling errors in text.",
        ),
        (
            "the-salami-saboteur",
            "The Salami Saboteur",
            "Middle grade mystery humor book cover, 1600x2400. Title 'The Salami Saboteur' in large playful handwritten-style font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration in hand-drawn doodle/sketch style like Diary of a Wimpy Kid: an orange ginger cat wearing a tiny black domino mask sneaking away with an enormous salami sausage over its shoulder. Behind it, a 9-year-old girl with round glasses and a brown bulldog look shocked. The bulldog has X-eyes. Thin pencil-line art with light shading. White background. Fun and kid-friendly. No spelling errors in text.",
        ),
        (
            "the-glass-vaults-gambit",
            "The Glass Vaults Gambit",
            "Middle grade mystery humor book cover, 1600x2400. Title 'The Glass Vaults Gambit' in large playful handwritten-style font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration in hand-drawn doodle/sketch style like Diary of a Wimpy Kid: a nighttime shopping mall interior with a glass skylight showing red laser security beams criss-crossing. An orange ginger cat in a black turtleneck spy outfit crawls through an air duct. A girl with glasses and a bulldog peek from behind a large potted plant. Question marks and exclamation marks floating. Thin pencil-line art. White background. No spelling errors in text.",
        ),
        (
            "station-zero",
            "Station Zero",
            "Young adult science fiction book cover, 1600x2400. Title 'Station Zero' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: a derelict space station floating against a field of distant stars. One single light still blinks on the station exterior. A small shuttle with approach lights on comes toward the station in the foreground. The station has visible damage: missing solar panels, dented hull. Cold, vast, lonely feeling. Clean science fiction, hard edges, realistic proportions. Deep blacks, dark blues, whites, warm orange shuttle lights. No spelling errors in text.",
        ),
        (
            "the-echo-chamber",
            "The Echo Chamber",
            "Young adult science fiction thriller book cover, 1600x2400. Title 'The Echo Chamber' in large bold tech-thriller font at the top. Author name 'Daniel Ryan' in smaller font at the bottom. Central illustration: a young person's face reflected in a smartphone screen, but their reflection is a slightly uncanny AI avatar with glowing eyes and too-perfect features. Digital glitch effects around the edges. Floating social media notification icons and streams of binary data surround the phone. Dark moody lighting. Modern tech-thriller, slightly cyberpunk. Dark blues, blacks, electric blues, neon pink accents. No spelling errors in text.",
        ),
        (
            "the-silent-strata",
            "The Silent Strata",
            "Young adult science fiction book cover, 1600x2400. Title 'The Silent Strata' in large bold futuristic font at the top. Author name 'Daniel Ryan' in smaller clean font at the bottom. Central illustration: a cross-section diagram of the Earth's crust showing geological layers, brown soil on top, then sandstone and granite getting progressively darker, then the deep mantle in near-black. In the deepest darkest layer, an ancient alien geometric structure glows with blue-white light. A tiny drilling machine approaches from far above. Clean science fiction meets scientific illustration. Browns, grays, blacks, glowing blue-white alien light. No spelling errors in text.",
        ),
    ]


def generate(pipe, covers: list[tuple[str, str, str]]) -> list[dict[str, str]]:
    output = Path(OUTPUT)
    output.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, str]] = []
    for i, (slug, title, prompt) in enumerate(covers, 1):
        path = output / f"{slug}-ebook-cover.png"
        if path.exists():
            print(f"[{i}/{len(covers)}] {title}: already exists, skipping")
            results.append(
                {
                    "title": title,
                    "slug": slug,
                    "status": "skipped-existing",
                    "path": str(path),
                    "error": "",
                }
            )
            continue

        print(f"[{i}/{len(covers)}] Generating {title}...")
        start = time.time()
        try:
            img = pipe(
                prompt=prompt,
                width=WIDTH,
                height=HEIGHT,
                num_inference_steps=STEPS,
                guidance_scale=GUIDANCE,
            ).images[0]
            img.save(path)
            elapsed = time.time() - start
            size_kb = path.stat().st_size // 1024
            print(f"  OK: {path} ({size_kb} KB, {elapsed:.0f}s)")
            results.append(
                {
                    "title": title,
                    "slug": slug,
                    "status": "success",
                    "path": str(path),
                    "error": "",
                }
            )
        except Exception as exc:
            elapsed = time.time() - start
            print(f"  FAIL: {title}: {exc}")
            results.append(
                {
                    "title": title,
                    "slug": slug,
                    "status": "error",
                    "path": str(path),
                    "error": str(exc),
                }
            )

    manifest_path = output / "manifest.csv"
    with manifest_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "slug", "status", "path", "error"])
        writer.writeheader()
        writer.writerows(results)

    success = sum(1 for r in results if r["status"] == "success")
    errors = sum(1 for r in results if r["status"] == "error")
    skipped = sum(1 for r in results if r["status"] == "skipped-existing")
    print("\nGENERATION COMPLETE")
    print(f"Success: {success}/{len(covers)}")
    print(f"Errors: {errors}/{len(covers)}")
    print(f"Skipped existing: {skipped}/{len(covers)}")
    print("Manifest:", manifest_path)
    return results


def download_zip() -> None:
    import shutil
    from google.colab import files

    shutil.make_archive("/content/covers_all", "zip", OUTPUT)
    files.download("/content/covers_all.zip")
    print("Downloaded covers_all.zip")


if __name__ == "__main__":
    # In Colab, run each step explicitly. Locally, this block gives a quick syntax/import smoke test.
    install_dependencies()
    login_huggingface()
    pipe = load_pipe()
    generate(pipe, cover_definitions())
    try:
        download_zip()
    except ImportError:
        print("google.colab.files is unavailable outside Colab; skip download step.")
