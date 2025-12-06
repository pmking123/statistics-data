"""Helper script to generate a Markdown table of datasets.

Run this from the root of the repository (where the `datasets/` folder lives):

    python tools/make_dataset_table.py

It will scan the `datasets/` folder and print a Markdown table with CSV and
codebook links, which you can paste into `index.md` or `README.md`.
"""

from pathlib import Path

def make_table(datasets_dir: Path) -> str:
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
            rows.append(f"| {desc} | [`{p.name}`]({csv_link}) | [`{md_name}`]({md_link}) |")
    header = "| Dataset | CSV | Codebook |\n|---------|-----|----------|"
    return header + "\n" + "\n".join(rows)

if __name__ == "__main__":
    datasets_dir = Path("datasets")
    if not datasets_dir.exists():
        raise SystemExit("datasets/ folder not found. Run from the repo root.")
    print(make_table(datasets_dir))
