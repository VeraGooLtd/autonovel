"""
Shared book-path configuration for Autonovel scripts.

All scripts accept an optional --book-dir argument pointing to an external
book directory. When provided, chapter and plan-file paths are resolved
relative to that directory instead of the autonovel repo root.

Expected external book layout (MY-DOG-IS-JUDGING-ME- style):
  <book-dir>/
    manuscript/chapter_01.md ... chapter_NN.md
    plans/
      seed.md
      world.md
      characters.md
      outline.md
      voice.md
      canon.md

Legacy autonovel layout (default when --book-dir is not set):
  <autonovel-root>/
    chapters/ch_01.md ... ch_NN.md
    voice.md
    world.md
    characters.md
    outline.md
    canon.md
"""

from pathlib import Path
import os
import re
import glob
import sys


def resolve_book_dir(book_dir_arg: str | None = None) -> tuple[Path, str]:
    """Return (chapters_dir, layout) for the given book-dir argument.

    layout is 'external' for the MY-DOG-IS-JUDGING-ME- style or 'legacy'
    for the autonovel default.
    """
    if book_dir_arg:
        bd = Path(book_dir_arg).resolve()
        if not bd.is_dir():
            print(f"ERROR: --book-dir '{bd}' is not a directory", file=sys.stderr)
            sys.exit(1)
        return (bd / "manuscript", "external")

    return (Path(__file__).parent / "chapters", "legacy")


def load_layers(book_dir_arg: str | None = None) -> dict:
    """Load all planning layer files (voice, world, characters, outline, canon)."""
    if book_dir_arg:
        bd = Path(book_dir_arg).resolve()
        plans = bd / "plans"
        return {
            "voice": _read(plans / "voice.md"),
            "world": _read(plans / "world.md"),
            "characters": _read(plans / "characters.md"),
            "outline": _read(plans / "outline.md"),
            "canon": _read(plans / "canon.md"),
        }
    # legacy: files sit in autonovel root
    root = Path(__file__).parent
    return {
        "voice": _read(root / "voice.md"),
        "world": _read(root / "world.md"),
        "characters": _read(root / "characters.md"),
        "outline": _read(root / "outline.md"),
        "canon": _read(root / "canon.md"),
    }


def _read(path: Path) -> str:
    try:
        return path.read_text()
    except FileNotFoundError:
        return ""


def load_all_chapter_paths(chapters_dir: Path, layout: str) -> dict:
    """Return {chapter_number: Path} for all chapters found."""
    chapters: dict[int, Path] = {}
    if layout == "external":
        # MDIM style: chapter_01.md, chapter_02.md ...
        pattern = str(chapters_dir / "chapter_*.md")
        for f in sorted(glob.glob(pattern)):
            m = re.search(r'chapter_(\d+)', f)
            if m:
                chapters[int(m.group(1))] = Path(f)
    else:
        # Autonovel legacy: ch_01.md, ch_02.md ...
        pattern = str(chapters_dir / "ch_*.md")
        for f in sorted(glob.glob(pattern)):
            m = re.search(r'ch_(\d+)', f)
            if m:
                chapters[int(m.group(1))] = Path(f)
    return chapters


def load_all_chapters(chapters_dir: Path, layout: str) -> dict:
    """Return {chapter_number: text} for all chapters found."""
    paths = load_all_chapter_paths(chapters_dir, layout)
    return {n: p.read_text() for n, p in paths.items()}
