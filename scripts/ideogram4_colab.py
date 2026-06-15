#!/usr/bin/env python3
"""Colab entrypoint for Ideogram 4 cover generation."""

from ideogram4_colab_cells import (
    cover_definitions,
    download_zip,
    generate,
    install_dependencies,
    load_pipe,
    login_huggingface,
)

if __name__ == "__main__":
    install_dependencies()
    login_huggingface()
    pipe = load_pipe()
    generate(pipe, cover_definitions())
    try:
        download_zip()
    except ImportError:
        print("google.colab.files is unavailable outside Colab; skip download step.")
