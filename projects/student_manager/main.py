from .student_service import add_student, list_student
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