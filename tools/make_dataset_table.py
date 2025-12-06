"""Helper script to generate Markdown tables of datasets and data files.

Run this from the root of the repository (where the `datasets/` and
`textbook_data/` folders live):

    python tools/make_dataset_table.py

It will:
- scan the `datasets/` folder and print a Markdown table with data file + codebook links
  (you can paste this into index.md or README.md if you like)
- recursively scan ALL subfolders of `textbook_data/` and update their README.md:
  * it will REPLACE any existing '## Dataset Index' section
  * or APPEND a new '## Dataset Index' section if none exists
"""

from pathlib import Path
import re
import sys

# ----------------------------------------------------------
# File types to index
# ----------------------------------------------------------

# Case-insensitive suffixes we treat as "data files"
INDEXED_SUFFIXES = {
    ".csv",
    ".xlsx",
    ".xpt",
    ".sav",
    ".txt",
    ".rdata",
    ".rds",
    ".json",
    ".tsv",
}

# Filenames we want to skip (temp/junk files etc.)
IGNORE_PREFIXES = (".", "~")  # e.g. .DS_Store, .gitignore, ~$foo.xlsx
IGNORE_SUFFIXES = ("~", ".bak", ".tmp")


def is_indexed(p: Path) -> bool:
    """Return True if the file should be included in the index."""
    if not p.is_file():
        return False
    name = p.name
    # ignore obvious junk
    if name.startswith(IGNORE_PREFIXES) or name.endswith(IGNORE_SUFFIXES):
        return False
    return p.suffix.lower() in INDEXED_SUFFIXES


# ----------------------------------------------------------
# Root dataset table
# ----------------------------------------------------------
def make_table_for_root_datasets(datasets_dir: Path) -> str:
    rows = []
    for p in sorted(datasets_dir.iterdir(), key=lambda x: x.name.lower()):
        if is_indexed(p):
            stem = p.stem
            data_link = f"datasets/{p.name}"

            # Codebook logic: only .md with matching stem
            md_name = f"{stem}.md"
            md_path = datasets_dir / md_name
            if md_path.exists():
                md_link = f"datasets/{md_name}"
            else:
                md_link = f"{md_name} (not yet created)"

            desc = f"{stem} file"
            rows.append(
                f"| {desc} | [`{p.name}`]({data_link}) | [`{md_name}`]({md_link}) |"
            )

    if not rows:
        return "_No dataset files found in datasets/._"

    header = "| File | Data | Codebook |\n|------|------|----------|"
    return header + "\n" + "\n".join(rows)


# ----------------------------------------------------------
# Subdirectory tables (textbook_data and deeper)
# ----------------------------------------------------------
def make_table_for_subdir(subdir: Path) -> str:
    rows = []
    for p in sorted(subdir.iterdir(), key=lambda x: x.name.lower()):
        if is_indexed(p):
            stem = p.stem
            data_link = p.name          # local relative link

            md_name = f"{stem}.md"
            md_path = subdir / md_name
            if md_path.exists():
                md_link = md_name       # local relative
            else:
                md_link = f"{md_name} (not yet created)"

            desc = f"{stem} file"
            rows.append(
                f"| {desc} | [`{p.name}`]({data_link}) | [`{md_name}`]({md_link}) |"
            )

    if not rows:
        return "_No dataset files found in this folder._"

    header = "| File | Data | Codebook |\n|------|------|----------|"
    return header + "\n" + "\n".join(rows)


# ----------------------------------------------------------
# README updater (Option B logic)
# ----------------------------------------------------------
def update_readme_with_index(readme_text: str, table: str) -> str:
    """Replace or append a '## Dataset Index' section in README.md.

    - If '## Dataset Index' exists, everything from that heading up to the next
      top-level or second-level heading ('# ' or '## ') is replaced with the new section.
    - If it does not exist, the section is appended at the end.
    """
    section = "\n## Dataset Index\n\n" + table + "\n"

    heading_re = re.compile(r"^## Dataset Index.*$", re.M)
    m = heading_re.search(readme_text)

    if not m:
        # Append at the end
        text = readme_text
        if not text.endswith("\n"):
            text += "\n"
        return text + section

    # Replace existing section
    start = m.start()
    after_heading_pos = m.end()
    rest = readme_text[after_heading_pos:]

    # Find next heading after this one
    next_heading_re = re.compile(r"^# ", re.M)
    m2 = next_heading_re.search(rest)
    if m2:
        end = after_heading_pos + m2.start()
    else:
        end = len(readme_text)

    before = readme_text[:start].rstrip()
    after = readme_text[end:]
    if not before.endswith("\n"):
        before += "\n"

    return before + section + after


# ----------------------------------------------------------
# Main script
# ----------------------------------------------------------
if __name__ == "__main__":
    repo_root = Path(".")

    # ---- 1. Datasets root table (stdout) ----
    datasets_dir = repo_root / "datasets"
    print("# Datasets (datasets/)\n")
    if not datasets_dir.exists():
        print("_No datasets/ folder found._")
    else:
        print(make_table_for_root_datasets(datasets_dir))
    print()

    # ---- 2. Traverse textbook_data/ recursively ----
    textbook_root = repo_root / "textbook_data"
    if not textbook_root.exists():
        print("No textbook_data/ folder found – skipping textbook READMEs.", file=sys.stderr)
        sys.exit(0)

    for subdir in sorted(textbook_root.rglob("*"), key=lambda x: str(x).lower()):
        if not subdir.is_dir():
            continue
        if subdir == textbook_root:
            continue

        readme_path = subdir / "README.md"
        if readme_path.exists():
            readme_text = readme_path.read_text(encoding="utf-8")
        else:
            title = subdir.name.replace("_", " ")
            readme_text = f"# {title} datasets\n\n"

        table = make_table_for_subdir(subdir)
        updated = update_readme_with_index(readme_text, table)
        readme_path.write_text(updated, encoding="utf-8")

        print(f"Updated dataset index in {readme_path}", file=sys.stderr)
