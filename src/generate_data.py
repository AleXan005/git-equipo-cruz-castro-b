cat > src/generate_data.py << 'EOF'
import csv
import random
from pathlib import Path

def make_students_csv(path: Path, n: int = 20, seed: int = 7):
    random.seed(seed)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["student_id", "studytime", "failures", "absences", "avg_grade"])
        for i in range(1, n + 1):
            studytime = random.randint(1, 4)
            failures = random.randint(0, 3)
            absences = random.randint(0, 20)
            avg_grade = round(random.uniform(6.0, 10.0), 2)
            w.writerow([i, studytime, failures, absences, avg_grade])

def make_sales_csv(path: Path, n: int = 30, seed: int = 11):
    random.seed(seed)
    path.parent.mkdir(parents=True, exist_ok=True)
    products = ["A", "B", "C", "D"]
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sale_id", "product", "units", "price"])
        for i in range(1, n + 1):
            product = random.choice(products)
            units = random.randint(1, 8)
            price = round(random.uniform(10.0, 150.0), 2)
            w.writerow([i, product, units, price])

if __name__ == "__main__":
    make_students_csv(Path("data/students.csv"))
    make_sales_csv(Path("data/sales.csv"))
    print("Generated: data/students.csv, data/sales.csv")
EOF
