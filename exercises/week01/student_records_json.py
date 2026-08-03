import json

file_path = "exercises/week01/students.json"
students = []

for i in range(3):
    n = i+1
    name = input(f"Nhập tên sinh viên thứ {n}: ")
    gpa = float(input(f"Nhập điểm hệ 4 của sinh viên thứ {n}: "))

    student = {
        "name": name,
        "gpa": gpa
    }

    students.append(student)

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2, ensure_ascii=False)

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

for student in data:
    print(f"Học sinh: {student["name"]}, Điểm: {student["gpa"]}")
