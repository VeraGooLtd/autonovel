#!/usr/bin/env python3
"""Generate EPUBs for MDIM books, Echo Chamber, and Silent Strata."""
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

# MDIM Book 1 — combine chapters
md_dir = os.path.expanduser("~/MY-DOG-IS-JUDGING-ME-/content/books/salami-saboteur/manuscript")
chapters = sorted([f for f in os.listdir(md_dir) if f.startswith("chapter_")])
md_content = ""
for ch in chapters:
    with open(os.path.join(md_dir, ch), 'r') as f:
        md_content += f.read() + "\n\n"

# Write combined md
combined_md = os.path.expanduser("~/MY-DOG-IS-JUDGING-ME-/content/books/salami-saboteur/combined.md")
with open(combined_md, 'w') as f:
    f.write("# The Salami Saboteur\n\n" + md_content)

md_to_epub(combined_md, os.path.expanduser("~/MY-DOG-IS-JUDGING-ME-/content/books/salami-saboteur/The-Salami-Saboteur.epub"), "The Salami Saboteur")

# MDIM Book 2
md_dir2 = os.path.expanduser("~/MY-DOG-IS-JUDGING-ME-/content/books/the-glass-vaults-gambit/manuscript")
chapters2 = sorted([f for f in os.listdir(md_dir2) if f.startswith("chapter_")])
md_content2 = ""
for ch in chapters2:
    with open(os.path.join(md_dir2, ch), 'r') as f:
        md_content2 += f.read() + "\n\n"

combined_md2 = os.path.expanduser("~/MY-DOG-IS-JUDGING-ME-/content/books/the-glass-vaults-gambit/combined.md")
with open(combined_md2, 'w') as f:
    f.write("# The Glass Vaults Gambit\n\n" + md_content2)

md_to_epub(combined_md2, os.path.expanduser("~/MY-DOG-IS-JUDGING-ME-/content/books/the-glass-vaults-gambit/The-Glass-Vaults-Gambit.epub"), "The Glass Vaults Gambit")

# Echo Chamber
ec_dir = os.path.expanduser("~/TheEchoChamber/content/chapters")
ec_chapters = sorted([f for f in os.listdir(ec_dir) if f.endswith(".md")])
ec_content = ""
for ch in ec_chapters:
    with open(os.path.join(ec_dir, ch), 'r') as f:
        ec_content += f.read() + "\n\n"

combined_ec = os.path.expanduser("~/TheEchoChamber/combined.md")
with open(combined_ec, 'w') as f:
    f.write("# The Echo Chamber\n\n" + ec_content)

md_to_epub(combined_ec, os.path.expanduser("~/TheEchoChamber/The-Echo-Chamber.epub"), "The Echo Chamber")

# Silent Strata
ss_dir = os.path.expanduser("~/The-Silent-Strata/Chapters")
ss_chapters = sorted([f for f in os.listdir(ss_dir) if f.endswith(".md")])
ss_content = ""
for ch in ss_chapters:
    with open(os.path.join(ss_dir, ch), 'r') as f:
        ss_content += f.read() + "\n\n"

combined_ss = os.path.expanduser("~/The-Silent-Strata/combined.md")
with open(combined_ss, 'w') as f:
    f.write("# The Silent Strata\n\n" + ss_content)

md_to_epub(combined_ss, os.path.expanduser("~/The-Silent-Strata/The-Silent-Strata.epub"), "The Silent Strata")

print("\nAll EPUBs generated!")
