import json
import csv

file_path_r = "projects/json_to_csv/students.json"
file_path_w = "projects/json_to_csv/students.csv"

with open(file_path_r, "r", encoding="utf-8") as file:
    students = json.load(file)

with open(file_path_w, "w",newline="" ,encoding="utf-8") as file:
    fieldnames = ["name", "gpa"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)

print(f"Số sinh viên đã chuyển: {len(students)} ")
