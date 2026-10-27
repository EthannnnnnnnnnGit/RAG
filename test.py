from pathlib import Path

folder_path = Path("data/raw")

python_files = list(folder_path.rglob("*.py"))
for f in python_files:
    print(f)
