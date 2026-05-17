# Activity 5 – File Handling in Python
## Complete Python Solution
### Student Name: Vaughn Axel Salanio Villaluna
### Student ID: 2025-0850

```python
# =========================================
# ACTIVITY 5 - FILE HANDLING IN PYTHON
# Student Name: Vaughn Axel Salanio Villaluna
# Student ID: 2025-0850
# =========================================

from pathlib import Path
import shutil
import json
import csv
import time
from datetime import datetime

# Personal Information
student_id = "2025-0850"
student_name = "Vaughn Axel Salanio Villaluna"

# Create Main Directory
documents_path = Path.home() / "Documents" / "Activity_5_Files"
documents_path.mkdir(parents=True, exist_ok=True)

print("\n===== ACTIVITY 5 START =====\n")

# =====================================================
# 1. CREATE AND WRITE TO A FILE
# =====================================================
print("1. CREATE AND WRITE TO A FILE")

file_path = documents_path / f"intro_{student_id}.txt"
file_path.write_text(
    f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!"
)

print(f"File created and text written at: {file_path}\n")

# =====================================================
# 2. READ FILE CONTENT
# =====================================================
print("2. READ FILE CONTENT")

content = file_path.read_text()
print(content)
print()

# =====================================================
# 3. APPEND TO A FILE
# =====================================================
print("3. APPEND TO A FILE")

with file_path.open("a") as f:
    f.write("\nThis is a new line.")

print(f"Line appended to: {file_path}\n")

# =====================================================
# 4. WRITE MULTIPLE LINES
# =====================================================
print("4. WRITE MULTIPLE LINES")

lines_file = documents_path / f"lines_{student_id}.txt"

lines = ["Line 1", "Line 2", "Line 3"]

with lines_file.open("w") as f:
    f.write("\n".join(lines))

print(f"Multiple lines written to: {lines_file}\n")

# =====================================================
# 5. READ FILE LINE BY LINE
# =====================================================
print("5. READ FILE LINE BY LINE")

with lines_file.open("r") as f:
    for line in f:
        print(line.strip())

print()

# =====================================================
# 6. COUNT WORDS IN FILE
# =====================================================
print("6. COUNT WORDS IN FILE")

text = lines_file.read_text()
word_count = len(text.split())

print(
    f"{student_name} (ID: {student_id}) - Word count in file '{lines_file.name}': {word_count}"
)
print()

# =====================================================
# 7. COPY FILE
# =====================================================
print("7. COPY FILE")

src = file_path
dst = documents_path / f"intro_copy_{student_id}.txt"

shutil.copy(src, dst)

print(f"File copied successfully from {src.name} to {dst.name}.\n")

# =====================================================
# 8. RENAME FILE
# =====================================================
print("8. RENAME FILE")

old_file = documents_path / f"intro_copy_{student_id}.txt"
new_file = documents_path / f"intro_renamed_{student_id}.txt"

old_file.rename(new_file)

print(
    f"File renamed successfully from {old_file.name} to {new_file.name}."
)
print()

# =====================================================
# 9. DELETE FILE
# =====================================================
print("9. DELETE FILE")

if new_file.exists():
    new_file.unlink()
    print(f"File deleted successfully from: {new_file}")
else:
    print(f"No file found to delete at: {new_file}")

print()

# =====================================================
# 10. CREATE DIRECTORY
# =====================================================
print("10. CREATE DIRECTORY")

new_dir = documents_path / f"data_{student_id}"
new_dir.mkdir(parents=True, exist_ok=True)

print(f"Subdirectory created at: {new_dir}\n")

# =====================================================
# 11. WRITE JSON FILE
# =====================================================
print("11. WRITE JSON FILE")

json_data = {
    "name": student_name,
    "age": 21,
    "course": "Python Programming"
}

json_file = new_dir / f"student_{student_id}.json"

with json_file.open("w") as f:
    json.dump(json_data, f, indent=4)

print(f"JSON file written at: {json_file}\n")

# =====================================================
# 12. READ JSON FILE
# =====================================================
print("12. READ JSON FILE")

with json_file.open("r") as f:
    data = json.load(f)

print(data)
print()

# =====================================================
# 13. WRITE CSV FILE
# =====================================================
print("13. WRITE CSV FILE")

csv_file = documents_path / f"students_{student_id}.csv"

rows = [
    ["Name", "Student ID", "Score"],
    ["Anna", "2025-1001", 90],
    ["Ben", "2025-1002", 85],
    [student_name, student_id, 95]
]

with csv_file.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"CSV file created at: {csv_file}\n")

# =====================================================
# 14. READ CSV FILE
# =====================================================
print("14. READ CSV FILE")

with csv_file.open("r") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

print()

# =====================================================
# 15. FILE NOT FOUND HANDLING
# =====================================================
print("15. FILE NOT FOUND HANDLING")

missing_file = documents_path / f"missing_file_{student_id}.txt"

try:
    print(missing_file.read_text())
except FileNotFoundError:
    print(f"File not found for Student ID: {student_id}")

print()

# =====================================================
# 16. COUNT .TXT FILES
# =====================================================
print("16. COUNT .TXT FILES")

txt_files = list(documents_path.glob("*.txt"))

print(f"Student ID: {student_id}")
print(f"Found {len(txt_files)} .txt files in {documents_path}")

for file in txt_files:
    print(file.name)

print()

# =====================================================
# 17. FILE METADATA
# =====================================================
print("17. FILE METADATA")

if file_path.exists():
    stat = file_path.stat()

    print(f"Student ID: {student_id}")
    print(f"File: {file_path.name}")
    print(f"Size: {stat.st_size} bytes")
    print(f"Last Modified: {time.ctime(stat.st_mtime)}")
else:
    print(f"File {file_path.name} not found.")

print()

# =====================================================
# 18. UPPERCASE AND NUMBER LINES
# =====================================================
print("18. UPPERCASE AND NUMBER LINES")

lines = lines_file.read_text().splitlines()

with lines_file.open("w") as f:
    for i, line in enumerate(lines, 1):
        f.write(f"{i}: {line.upper()}\n")

print(f"Lines formatted and updated in file: {lines_file}\n")

# =====================================================
# 19. REVERSE FILE CONTENT
# =====================================================
print("19. REVERSE FILE CONTENT")

lines = lines_file.read_text().splitlines()
lines.reverse()

with lines_file.open("w") as f:
    f.write("\n".join(lines))

print(f"File lines reversed for Student ID: {student_id}\n")

# =====================================================
# 20. MERGE TWO FILES
# =====================================================
print("20. MERGE TWO FILES")

merged = documents_path / f"merged_{student_id}.txt"

with merged.open("w") as mf:
    mf.write(file_path.read_text())
    mf.write("\n")
    mf.write(lines_file.read_text())

print(f"Files merged successfully for Student ID: {student_id}")

print("\n===== ACTIVITY 5 COMPLETED =====")
```

---

# Recommended GitHub File Type

Use a `.py` file.

Example filename:

```text
activity5_file_handling.py
```

---

# Suggested GitHub Repository Name

```text
ComProg1-Activity5-FileHandling
```

---

# Suggested README Description

```text
This repository contains the Python solution for Activity 5: File Handling.
The program demonstrates reading, writing, appending, copying, renaming,
deleting, and processing files using Python.
```

