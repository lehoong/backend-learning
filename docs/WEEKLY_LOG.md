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
