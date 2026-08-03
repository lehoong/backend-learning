import csv

fieldnames = ["name", "gpa"]
file_path = "exercises/week01/students.csv"
students = []

for i in range(3):
    n = i+ 1
    name = input(f"Nhập tên sinh viên thứ {n}: ")
    gpa = float(input(f"Nhập điểm hệ 4 của sinh viên thứ {n}: "))

    student = {
        "name": name,
        "gpa": gpa
    }

    students.append(student)
with open(file_path, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)

with open(file_path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['name']}, GPA: {float(row['gpa'])}")