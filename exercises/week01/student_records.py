students = []

for i in range(3):
    name = input(f"Nhập tên học sinh thứ {i+1}: ")
    gpa = float(input(f"Nhập điểm hệ 4 của học sinh thứ {i+1}: "))

    student = {
        "name": name,
        "gpa": gpa
    }

    students.append(student)

for student in students:
    print(student)