import PyPDF2
import sys
import os

SOURCE_FOLDER = "./files"
TARGET_FOLDER = "./target"
MERGED_FILE = f"{TARGET_FOLDER}/merged.pdf"

merger = PyPDF2.PdfMerger()

for file in os.listdir(SOURCE_FOLDER):
    if file.endswith(".pdf"):
        merger.append(f"{SOURCE_FOLDER}/{file}")
merger.write(MERGED_FILE)
print(f"Merged PDF file was created: {MERGED_FILE}")
