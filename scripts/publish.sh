#!/bin/env bash
# D2D Publishing Workflow for Hermes Agent
# Usage: bash publish.sh <book-repo> <epub-file> <metadata-file>

set -e

BOOK_REPO=$1
EPUB_FILE=$2
METADATA_FILE=$3

if [ -z "$BOOK_REPO" ] || [ -z "$EPUB_FILE" ] || [ -z "$METADATA_FILE" ]; then
  echo "Usage: bash publish.sh <book-repo-path> <epub-file> <metadata-file>"
  echo "Example: bash publish.sh ~/Mycoformed-Mars-Saga The-Genesis-Engine.epub metadata.json"
  exit 1
fi

cd "$BOOK_REPO"

# Read metadata
TITLE=$(python3 -c "import json; print(json.load(open('$METADATA_FILE'))['title'])")
AUTHOR=$(python3 -c "import json; print(json.load(open('$METADATA_FILE'))['author'])")
DESCRIPTION=$(python3 -c "import json; print(json.load(open('$METADATA_FILE'))['description'])")
WORD_COUNT=$(python3 -c "import json; print(json.load(open('$METADATA_FILE')).get('word_count', 'N/A'))")

echo "============================================"
echo "D2D Publishing Workflow"
echo "============================================"
echo "Title: $TITLE"
echo "Author: $AUTHOR"
echo "Word Count: $WORD_COUNT"
echo "EPUB: $EPUB_FILE"
echo "============================================"
echo ""
echo "Steps:"
echo "1. Open https://www.draft2digital.com in browser"
echo "2. Login to D2D account"
echo "3. Click 'Add New Book'"
echo "4. Fill in metadata (see metadata.json)"
echo "5. Upload EPUB file: $EPUB_FILE"
echo "6. Upload cover image (if available)"
echo "7. Set pricing and distribution"
echo "8. Review and publish"
echo ""
echo "Metadata ready in: $METADATA_FILE"
echo "EPUB ready in: $EPUB_FILE"
echo "============================================"
