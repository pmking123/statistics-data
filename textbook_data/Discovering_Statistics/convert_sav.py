import os
import pandas as pd
import pyreadstat

# ==== CONFIGURE THIS ====
input_dir = "./"
summary_filename = "_directory_summary.md"
# =========================

summary_entries = []  # will hold info for the global summary

# Ensure absolute path (optional but nice)
input_dir = os.path.abspath(input_dir)

# Get .sav files in a stable order
sav_files = sorted(
    f for f in os.listdir(input_dir) 
    if f.lower().endswith(".sav")
)

if not sav_files:
    print(f"No .sav files found in {input_dir}")
else:
    for filename in sav_files:
        sav_path = os.path.join(input_dir, filename)
        base = os.path.splitext(filename)[0]
        csv_path = os.path.join(input_dir, f"{base}.csv")
        md_path = os.path.join(input_dir, f"{base}.md")

        print(f"Processing {filename}…")

        # Read SPSS file
        df, meta = pyreadstat.read_sav(sav_path)

        # --- Write CSV ---
        df.to_csv(csv_path, index=False)

        # Variable labels: meta.column_names + meta.column_labels (parallel lists)
        var_labels = list(zip(meta.column_names, meta.column_labels))

        # Value labels per variable
        value_labels = meta.variable_value_labels  # dict: var -> {value: label}

        # --- Write per-file Markdown metadata ---
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# Metadata for `{filename}`\n\n")

            # File-level info
            f.write("## File information\n\n")
            f.write(f"- **SPSS file label**: {meta.file_label or ''}\n")
            f.write(f"- **Rows**: {meta.number_rows}\n")
            f.write(f"- **Columns**: {meta.number_columns}\n\n")

            # Variable labels
            f.write("## Variable labels\n\n")
            for var_name, var_label in var_labels:
                label_str = var_label or ""
                f.write(f"- **{var_name}**: {label_str}\n")

            # Value labels
            f.write("\n## Value labels\n")
            if value_labels:
                for var_name, labels_dict in value_labels.items():
                    f.write(f"\n### {var_name}\n")
                    if labels_dict:
                        for val, label in labels_dict.items():
                            f.write(f"- `{val}` → {label}\n")
                    else:
                        f.write("- (No value labels defined)\n")
            else:
                f.write("\n(No value labels present in this file.)\n")

        # Collect info for global summary
        summary_entries.append({
            "filename": filename,
            "base": base,
            "csv": os.path.basename(csv_path),
            "md": os.path.basename(md_path),
            "rows": meta.number_rows,
            "cols": meta.number_columns,
            "file_label": meta.file_label or "",
            "n_variables": len(meta.column_names),
            "n_vars_with_value_labels": sum(
                1 for v in meta.column_names if v in value_labels
            )
        })

        print(f"Created {csv_path} and {md_path}")

    # --- Write directory-level summary Markdown ---
    summary_path = os.path.join(input_dir, summary_filename)
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(f"# SPSS conversion summary\n\n")
        f.write(f"Directory: `{input_dir}`\n\n")
        f.write(f"Total .sav files processed: **{len(summary_entries)}**\n\n")

        # Table of files
        f.write("## Files converted\n\n")
        f.write("| SPSS file | Rows | Columns | SPSS file label | CSV file | Metadata file |\n")
        f.write("|----------|------|---------|-----------------|----------|---------------|\n")
        for entry in summary_entries:
            f.write(
                f"| `{entry['filename']}` "
                f"| {entry['rows']} "
                f"| {entry['cols']} "
                f"| {entry['file_label']} "
                f"| `{entry['csv']}` "
                f"| `{entry['md']}` |\n"
            )

        # Variables summary
        f.write("\n## Variable / value label overview\n\n")
        for entry in summary_entries:
            f.write(f"### {entry['filename']}\n\n")
            f.write(f"- Variables: **{entry['n_variables']}**\n")
            f.write(
                f"- Variables with value labels: "
                f"**{entry['n_vars_with_value_labels']}**\n"
            )
            f.write(f"- Metadata file: `{entry['md']}`\n\n")

    print(f"\nSummary written to {summary_path}")
    print("All done ✅")
