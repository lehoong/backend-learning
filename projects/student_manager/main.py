def add_student() -> dict:
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
    return {"name": name, "gpa": gpa}

def list_student(students) -> None:
    if not students:
        print("Danh sách sinh viên trống!")
        return
    for index, student in enumerate(students, start=1):
        print(f"STT: {index}, Tên: {student['name']}, GPA: {student['gpa']}")


def main():
    students = []
    while True:
        print("========Quản lý sinh viên========")
        print("1. Thêm sinh viên")
        print("2. Xem danh sách sinh viên")
        print("0. Thoát")
        choice = input("Nhập lựa chọn: ").strip()
        if choice not in ("0", "1", "2"):
            print("Vui lòng nhập lựa chọn 1, 2 hoặc 0!")
        elif choice == "1":
            students.append(add_student())
        elif choice == "2":
            list_student(students)
        elif choice == "0":
            print("Thoát chương trình.....")
            break

if __name__ == "__main__":
    main()