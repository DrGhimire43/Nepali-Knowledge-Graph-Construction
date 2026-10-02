import os
import glob

INPUT_DIR = r"C:\Users\DELL\Downloads\nepali_wiki_articles"
OUTPUT_FILE = os.path.join(INPUT_DIR, "merged_articles.txt")

txt_files = sorted(glob.glob(os.path.join(INPUT_DIR, "*.txt")))

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
    for i, filepath in enumerate(txt_files, 1):
        with open(filepath, "r", encoding="utf-8") as infile:
            content = infile.read().strip()
        outfile.write(content)
        outfile.write("\n\n")  # separator between articles
        print(f"[{i}/{len(txt_files)}] merged: {os.path.basename(filepath)}")

print(f"\nDone. {len(txt_files)} files merged into {OUTPUT_FILE}")
