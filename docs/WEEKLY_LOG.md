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
- Vướng mắc: không có.
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
- Vướng mắc: cần xóa khoảng trắng thừa trước khi commit.
- Bước tiếp theo: ôn điều kiện, vòng lặp và function qua project nhỏ.
