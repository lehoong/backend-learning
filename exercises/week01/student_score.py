def classify_gpa(gpa: float) -> str:
    if 4.0 >= gpa >= 3.6:
        return "Xuất sắc"

    elif 3.6 > gpa >= 3.2:
        return "Giỏi"

    elif 3.2 > gpa >= 2.5:
        return "Khá"

    elif 2.5 > gpa >= 2.0:
        return "Trung Bình"

    elif 2.0 > gpa >= 0:
        return("Cần cải thiện")

    else:
        raise ValueError("Giá trị không hợp lệ")

def main() -> None:

    try:

        name = input("Nhập tên sinh viên: ").strip()
        if not name:
            raise ValueError("Tên sinh viên không được để trống")

        gpa_text = input("Nhập GPA hệ 4: ")

        try:
            gpa = float(gpa_text)
        except ValueError:
            raise ValueError("GPA phải là điểm số!")

        if gpa < 0 or gpa > 4:
            raise ValueError("GPA phải nằm trong khoảng từ 0 đến 4.")
        result = classify_gpa(gpa)

        print(f"Sinh viên: {name}")
        print(f"Điểm: {gpa:.2f}")
        print(f"Phân loại: {result}")

    except ValueError as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
