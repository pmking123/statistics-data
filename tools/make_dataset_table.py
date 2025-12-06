"""Helper script to generate Markdown tables of datasets.

Run this from the root of the repository (where the `datasets/` and
`textbook_data/` folders live):

    python tools/make_dataset_table.py

It will:
- scan the `datasets/` folder and print a Markdown table with CSV + codebook links
  (you can paste this into index.md or README.md if you like)
- scan each subfolder of `textbook_data/` and update its README.md:
  * it will REPLACE any existing '## Dataset Index' section
  * or APPEND a new '## Dataset Index' section at the end if none exists
"""

from pathlib import Path
import re
import sys


def make_table_for_root_datasets(datasets_dir: Path) -> str:
    """Make a Markdown table for all .csv files in datasets/ (for the main index)."""
    rows = []
    for p in sorted(datasets_dir.iterdir()):
        if p.suffix.lower() == ".csv":
            stem = p.stem
            csv_link = f"datasets/{p.name}"
            md_name = f"{stem}.md"
            md_path = datasets_dir / md_name
            if md_path.exists():
                md_link = f"datasets/{md_name}"
            else:
                md_link = md_name + " (not yet created)"
            desc = f"{stem} dataset"
            rows.append(
                f"| {desc} | [`{p.name}`]({csv_link}) | [`{md_name}`]({md_link}) |"
            )

    if not rows:
        return "_No .csv files found in datasets/._"

    header = "| Dataset | CSV | Codebook |\n|---------|-----|----------|"
    return header + "\n" + "\n".join(rows)


def make_table_for_subdir(subdir: Path) -> str:
    """Make a Markdown table for .csv files in a textbook subfolder.

    Links are relative to that folder (e.g. `asthma.csv`, `asthma.md`).
    """
    rows = []
    for p in sorted(subdir.iterdir()):
        if p.suffix.lower() == ".csv":
            stem = p.stem
            csv_link = p.name
            md_name = f"{stem}.md"
            md_path = subdir / md_name
            if md_path.exists():
                md_link = md_name
            else:
                md_link = md_name + " (not yet created)"
            desc = f"{stem} dataset"
            rows.append(
                f"| {desc} | [`{p.name}`]({csv_link}) | [`{md_name}`]({md_link}) |"
            )

    if not rows:
        return "_No .csv files found in this folder._"

    header = "| Dataset | CSV | Codebook |\n|---------|-----|----------|"
    return header + "\n" + "\n".join(rows)


def update_readme_with_index(readme_text: str, table: str) -> str:
    """Replace or append a '## Dataset Index' section in a README.md (Option B).

    - If '## Dataset Index' exists, everything from that heading up to the next
      heading ('# ' or '## ') is replaced with the new section.
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

    # Find next heading (level 1 or 2) after '## Dataset Index'
    next_heading_re = re.compile(r"^# ", re.M)  # matches '# ' OR '## ' etc.
    m2 = next_heading_re.search(rest)
    if m2:
        end = after_heading_pos + m2.start()
    else:
        end = len(readme_text)

    before = readme_text[:start].rstrip()
    after = readme_text[end:]
    if not before.endswith("\n"):
        before += "\n"
    # Keep a blank line between the previous content and the new section
    return before + section + after


if __name__ == "__main__":
    repo_root = Path(".")

    # ---- 1. Print table for datasets/ (stdout, for use in index.md etc.) ----
    datasets_dir = repo_root / "datasets"
    if not datasets_dir.exists():
        raise SystemExit("datasets/ folder not found. Run from the repo root.")

    table_root = make_table_for_root_datasets(datasets_dir)
    print("# Datasets (datasets/)\n")
    print(table_root)
    print()

    # ---- 2. Update textbook_data/*/README.md files in-place ----
    textbook_root = repo_root / "textbook_data"
    if not textbook_root.exists():
        print("No textbook_data/ folder found – skipping textbook READMEs.", file=sys.stderr)
        raise SystemExit(0)

    for subdir in sorted(textbook_root.iterdir()):
        if not subdir.is_dir():
            continue

        readme_path = subdir / "README.md"
        if not readme_path.exists():
            # If you prefer to skip folders without README, uncomment next line:
            # print(f"Skipping {subdir} (no README.md found)", file=sys.stderr)
            # continue
            # Or create a basic README:
            base_title = f"# {subdir.name} datasets\n\n"
            readme_text = base_title
        else:
            readme_text = readme_path.read_text(encoding="utf-8")

        table = make_table_for_subdir(subdir)
        updated = update_readme_with_index(readme_text, table)
        readme_path.write_text(updated, encoding="utf-8")
        print(f"Updated dataset index in {readme_path}", file=sys.stderr)
