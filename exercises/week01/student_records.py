students = []

for i in range(3):
    n = i + 1
    while True:
        try:
            name = input(f"Nhập tên sinh viên thứ {n}: ").strip()
            if not name:
                raise ValueError("Tên sinh viên không được để trống!")
            try:
                gpa = float(input(f"Nhập điểm sinh viên thứ {n}: "))
            except ValueError:
                raise ValueError("GPA phải là điểm số")
            if not 0 <= gpa <=4:
                raise ValueError("GPA nằm trong khoảng từ 0 đến 4")

            break

        except ValueError as e:
            print(f"Dữ liệu nhập vào không hợp lệ: {e}")

    student = {
        "name": name,
        "gpa": gpa
    }
    students.append(student)



for student in students:
    print(f"Name: {student['name']}, GPA: {student['gpa']}")