cat > src/analyze.py << 'EOF'
import csv
from pathlib import Path

def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else float("nan")

def read_grades(path: Path):
    grades = []
    with path.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            grades.append(float(row["avg_grade"]))
    return grades

if __name__ == "__main__":
    grades = read_grades(Path("data/students.csv"))
    print("Mean avg_grade:", round(mean(grades), 3))
EOF
