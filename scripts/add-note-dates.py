#!/usr/bin/env python3
"""
Script to automatically add dates to notes in content/notes/index.md
Designed to be run as a git pre-commit hook.
"""

import re
import sys
from datetime import datetime
from pathlib import Path


def get_current_date():
    """Get current date in YYYY.MM.DD format"""
    return datetime.now().strftime("%Y.%m.%d")


def has_date_suffix(line):
    """Check if a line ends with a date in format - YYYY-MM-DD or - YYYY.MM.DD"""
    # Match date patterns like "- 2025-12-03" or "- 2025.12.01"
    pattern = r"-\s*\d{4}\.?\d{2}\.?\d{2}\s*$"
    return bool(re.search(pattern, line))


def process_notes_file(file_path):
    """
    Process the notes file and add dates to blockquotes that don't have them.
    Since new notes are added at the top, we only process until we find a note
    with a date, then copy the rest of the file as-is for better performance.
    Returns True if file was modified, False otherwise.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    modified = False
    i = 0
    new_lines = []
    found_dated_note = False

    while i < len(lines):
        line = lines[i]

        # Check if this is the start of a blockquote
        if line.strip().startswith(">"):
            # Collect all consecutive lines that are part of this blockquote
            blockquote_lines = [line]
            j = i + 1

            # Continue reading lines that are part of the same blockquote
            # In markdown, a blockquote continues until an empty line
            while j < len(lines):
                next_line = lines[j]

                # Empty line marks the end of the blockquote
                if next_line.strip() == "":
                    break

                # Continue the blockquote (can be > line or continuation line)
                blockquote_lines.append(next_line)
                j += 1

            # Check the last line of the blockquote for a date
            last_line = blockquote_lines[-1].rstrip()

            if not has_date_suffix(last_line):
                # Add date to the last line
                current_date = get_current_date()
                # Remove trailing newline, add date, then add newline back
                blockquote_lines[-1] = last_line + f"  - {current_date}\n"
                modified = True
                print(f"✓ Added date to blockquote: {last_line[:50]}...")
            else:
                # Found a note with a date - all notes below should have dates
                found_dated_note = True

            # Add all blockquote lines to new_lines
            new_lines.extend(blockquote_lines)
            i = j

            # If we found a dated note, copy the rest of the file as-is
            if found_dated_note:
                new_lines.extend(lines[i:])
                break
        else:
            # Not a blockquote, just add the line as-is
            new_lines.append(line)
            i += 1

    # Write back to file if modified
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"\n✓ Updated {file_path}")
        return True
    else:
        print(f"✓ No changes needed in {file_path}")
        return False


def main():
    """Main function"""
    # Get the repository root (assuming script is in scripts/ directory)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    notes_file = repo_root / "content" / "notes" / "index.md"

    if not notes_file.exists():
        print(f"✗ Notes file not found: {notes_file}")
        sys.exit(1)

    print(f"Checking notes file: {notes_file}")
    modified = process_notes_file(notes_file)

    if modified:
        print("\n✓ Dates added successfully!")
        sys.exit(0)
    else:
        print("\n✓ All notes already have dates.")
        sys.exit(0)


if __name__ == "__main__":
    main()
