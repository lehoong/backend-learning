from .student import Student
def add_student() -> Student:
    while True:
        try:
            name = input("Nhập tên sinh viên cần thêm: ").strip()
            if not name:
                raise ValueError("Tên không được rỗng!")
            try:
                gpa = float(input("Nhập điểm sinh viên cần thêm: "))
            except ValueError:
                raise ValueError("GPA phải là một số!")
            if not 0 <= gpa <= 4.0:
                raise ValueError("GPA nằm trong khoảng 0 đến 4")
            break
        except ValueError as e:
            print(f"Lỗi: {e}")
    return Student(name, gpa)

def list_student(students: list[Student]) -> None:
    if not students:
        print("Danh sách sinh viên trống!")
        return
    for index, student in enumerate(students, start=1):
        print(student.display(index))