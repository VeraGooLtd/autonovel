#!/usr/bin/env python3
"""Convert Markdown manuscripts to EPUB for D2D publishing."""
import os, re, markdown
from ebooklib import epub

def md_to_epub(md_path, epub_path, title, author="Daniel Ryan"):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['extra'])
    book = epub.EpubBook()
    book.set_identifier(f'daniel-ryan-{title.lower().replace(" ", "-")}')
    book.set_title(title)
    book.set_language('en')
    book.add_author(author)
    style = 'body{font-family:Georgia,serif;line-height:1.6;margin:5%}h1{text-align:center;font-size:2em;margin-top:2em}h2{font-size:1.5em;margin-top:1.5em}p{text-indent:1.5em;margin:0}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)
    # Split on h1
    parts = re.split(r'(<h1[^>]*>.*?</h1>)', html_content, flags=re.DOTALL)
    chapters = []
    current_title = "Front Matter"
    current_content = ""
    for part in parts:
        if part.startswith('<h1'):
            if current_content.strip():
                safe = re.sub(r'[^\w]+', '-', current_title.lower()).strip('-') or 'chap'
                c = epub.EpubHtml(title=current_title, file_name=f'{safe}.xhtml', lang='en')
                c.content = f'<h1>{current_title}</h1>{current_content}' if current_title != "Front Matter" else current_content
                c.add_item(nav_css)
                book.add_item(c)
                chapters.append(c)
            current_title = re.sub(r'<[^>]+>', '', part).strip()
            current_content = ""
        else:
            current_content += part
    # Last chapter
    if current_content.strip():
        safe = re.sub(r'[^\w]+', '-', current_title.lower()).strip('-') or 'chap'
        c = epub.EpubHtml(title=current_title, file_name=f'{safe}.xhtml', lang='en')
        c.content = f'<h1>{current_title}</h1>{current_content}'
        c.add_item(nav_css)
        book.add_item(c)
        chapters.append(c)
    book.toc = chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    epub.write_epub(epub_path, book, {})
    print(f'OK: {epub_path} ({os.path.getsize(epub_path)} bytes)')

manuscripts = [
    ("~/Mycoformed Mars Saga/Mycoformed Mars Book 1. The Genesis Engine 5 x 8 in Published.docx.md", "~/Mycoformed Mars Saga/The-Genesis-Engine.epub", "The Genesis Engine"),
    ("~/Mycoformed Mars Saga/Mycoformed Mars Book 2. The Martian Spore 5 x 8 in Published.docx.md", "~/Mycoformed Mars Saga/The-Martian-Spore.epub", "The Martian Spore"),
    ("~/Mycoformed Mars Saga/Mycoformed Mars Book 3. The Crimson Bloom 5 x 8 in NOTPublished.docx.md", "~/Mycoformed Mars Saga/The-Crimson-Bloom.epub", "The Crimson Bloom"),
    ("~/Sporefall/Book 1. Sporefall.md", "~/Sporefall/Sporefall.epub", "Sporefall"),
    ("~/Sporefall/Book 2. Mycelial Tide.md", "~/Sporefall/Mycelial-Tide.epub", "Mycelial Tide"),
    ("~/Sporefall/Book 3. Mycelial Earth.md", "~/Sporefall/Mycelial-Earth.epub", "Mycelial Earth"),
    ("~/StationZero/station_zero_complete.md", "~/StationZero/Station-Zero.epub", "Station Zero"),
]

for md_path, epub_path, title in manuscripts:
    md_path, epub_path = os.path.expanduser(md_path), os.path.expanduser(epub_path)
    if not os.path.exists(md_path):
        print(f'SKIP: {md_path} not found')
        continue
    try:
        md_to_epub(md_path, epub_path, title)
    except Exception as e:
        print(f'ERROR: {title}: {e}')

print('\nDone!')
