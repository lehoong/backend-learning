## 2026-08-03 — Student score CLI

- Mục tiêu: hoàn thiện bài phân loại GPA bằng Python.
- Đã làm:
  - Viết `classify_gpa`.
  - Viết `main` để nhận tên và GPA.
  - Xử lý tên rỗng, GPA không phải số và GPA ngoài khoảng `0–4`.
  - Thêm type hint và định dạng GPA hai chữ số.
- Kiểm tra: các mốc GPA từ `0` đến `4` và các input không hợp lệ đều cho kết quả đúng.
- Vướng mắc: không có.
- Bước tiếp theo: tạo commit đầu tiên cho bài tập.
## 2026-08-03 — List và dictionary

- Mục tiêu: thực hành list, dictionary và vòng lặp `for`.
- Đã làm:
  - Tạo list `students`.
  - Tạo dictionary gồm `name` và `gpa`.
  - Dùng `append()` để lưu 3 sinh viên.
  - Duyệt list và in kết quả.
- Kiểm tra: nhập `a/2`, `b/3`, `c/4`; kết quả đúng.
- Vướng mắc: không có.
- Bước tiếp theo: học đọc và ghi JSON.
## 2026-08-03 — Đọc và ghi JSON

- Mục tiêu: thực hành lưu dữ liệu Python vào JSON và đọc lại.
- Đã làm:
  - Dùng list các dictionary cho dữ liệu sinh viên.
  - Ghi dữ liệu bằng `json.dump()`.
  - Đọc dữ liệu bằng `json.load()`.
- Kiểm tra: dữ liệu `a/2`, `b/3`, `c/4` được ghi và đọc đúng.
- Vướng mắc: dùng nhầm chuỗi `"file_path"` thay vì biến `file_path`, đã sửa.
- Bước tiếp theo: học đọc và ghi CSV.
## 2026-08-03 — Đọc và ghi CSV

- Mục tiêu: thực hành ghi và đọc dữ liệu CSV.
- Đã làm:
  - Dùng `csv.DictWriter` để ghi header và các dòng dữ liệu.
  - Dùng `csv.DictReader` để đọc lại CSV.
  - Sử dụng `newline=""` và UTF-8.
- Kiểm tra: nhập `a/4`, `b/3`, `c/2`; kết quả đọc lại đúng.
- Vướng mắc: `git diff --cached --check` phát hiện một dòng trống thừa ở cuối `student_service.py`; đã sửa và kiểm tra lại trước commit `a5a63e0`.
- Bước tiếp theo: học exception.

## 2026-08-04 — Exception và nhập lại dữ liệu

- Mục tiêu: áp dụng `try`, `except`, `raise` và vòng lặp để xử lý input không hợp lệ.
- Đã làm:
  - Kiểm tra tên rỗng, GPA không phải số và GPA ngoài khoảng `0–4`.
  - Hiển thị thông báo lỗi tiếng Việt.
  - Giữ nguyên sinh viên hiện tại để người dùng nhập lại.
- Kiểm tra: thử tên rỗng, `abc`, `10`, sau đó nhập `a/2`, `b/3`, `c/4`; chương trình in đủ 3 sinh viên.
- Vướng mắc: không có.
- Bước tiếp theo: xây project JSON-to-CSV.

## 2026-08-04 — Project JSON-to-CSV

- Mục tiêu: kết hợp list/dictionary, JSON và CSV trong một project nhỏ.
- Đã làm:
  - Đọc danh sách sinh viên từ `students.json`.
  - Ghi header và dữ liệu sang `students.csv` bằng `csv.DictWriter`.
  - In số sinh viên đã chuyển.
- Kiểm tra: script chuyển 3 sinh viên; JSON và CSV có cùng tên tiếng Việt và GPA.
- Vướng mắc: đường dẫn hiện tại yêu cầu chạy script từ repository root.
- Bước tiếp theo: củng cố CLI quản lý sinh viên.

## 2026-08-04 — CLI quản lý sinh viên

- Mục tiêu: kết hợp function, menu, list/dictionary và exception trong một CLI chạy trong bộ nhớ.
- Đã làm:
  - Tạo menu thêm sinh viên, xem danh sách và thoát.
  - Tách `add_student`, `list_student` và `main`.
  - Xử lý lựa chọn menu sai và input sinh viên không hợp lệ.
- Kiểm tra: danh sách rỗng an toàn; thêm nhiều sinh viên hợp lệ; menu sai, tên rỗng, GPA `abc` và GPA `10` đều được xử lý.
- Vướng mắc: không có; đã kiểm tra khoảng trắng trước khi commit.
- Bước tiếp theo: ôn điều kiện, vòng lặp và function qua project nhỏ.

## 2026-08-04 — Tách CLI thành module

- Mục tiêu: hiểu module và `import` bằng cách tách code của CLI hiện có.
- Đã làm:
  - Tạo `projects/student_manager/student_service.py`.
  - Chuyển `add_student` và `list_student` sang module mới.
  - Import hai hàm đó trong `main.py`; menu và danh sách `students` vẫn ở `main.py`.
- Kiểm tra: thêm `a/2` và xem danh sách hoạt động; danh sách rỗng in thông báo an toàn; chương trình thoát bình thường.
- Vướng mắc: không có.
- Bước tiếp theo: học package bằng cách tổ chức lại `student_manager`.

## 2026-08-04 — Package và relative import

- Mục tiêu: tổ chức CLI thành package và hiểu cách chạy module bằng `-m`.
- Đã làm:
  - Tạo `projects/__init__.py` và `projects/student_manager/__init__.py`.
  - Đổi import trong `main.py` thành relative import từ `.student_service`.
  - Chạy CLI bằng `python -m projects.student_manager.main`.
- Kiểm tra: danh sách rỗng, thêm `a/2`, xem danh sách và thoát đều hoạt động.
- Git evidence: `5d86529 Turn student manager into a package`.
- Vướng mắc: import cũ `from student_service ...` gây `ModuleNotFoundError`; đã sửa thành relative import.
- Bước tiếp theo: ôn OOP cơ bản.

## 2026-08-04 — Class Student

- Mục tiêu: luyện class, object, constructor và thuộc tính bằng CLI hiện có.
- Đã làm:
  - Tạo `projects/student_manager/student.py` với class `Student`.
  - Lưu `name` và `gpa` trong `self.name` và `self.gpa`.
  - Đổi `add_student()` để trả về object `Student` thay vì dictionary.
  - Đổi `list_student()` sang đọc thuộc tính object.
- Kiểm tra: thêm `a/2`, in đúng `STT: 1, Tên: a, GPA: 2.0`; danh sách rỗng và thoát đều hoạt động.
- Git evidence: `2185fa8 Introduce Student class`.
- Vướng mắc: gõ nhầm `project.student_manager.main`; đã sửa thành `projects.student_manager.main`.
- Bước tiếp theo: củng cố method và type hint bằng class `Student`.

## 2026-08-04 — Method và type hint cho Student

- Mục tiêu: luyện method instance và type hint trong class.
- Đã làm:
  - Thêm `Student.display(index: int) -> str`.
  - Để method tạo chuỗi hiển thị từ `self.name` và `self.gpa`.
  - Đổi `list_student` thành `list[Student]` và gọi `student.display(index)`.
- Kiểm tra: thêm `a/2`, xem danh sách in đúng `STT: 1, Tên: a, GPA: 2.0`, rồi thoát.
- Git evidence: `deb830f Add Student display method and type hints`.
- Vướng mắc: không có.
- Bước tiếp theo: ôn tuple và set.
