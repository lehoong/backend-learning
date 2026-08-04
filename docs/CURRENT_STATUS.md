---

current_week: 1
current_phase: Python and Git
status: in_progress
hours_per_week: 8
last_updated: 2026-08-04
next_review_date: 2026-08-09
----------------------------

# Current Learning Status

## Mục tiêu hiện tại

Ôn OOP cơ bản bằng một bài thực hành nhỏ.

## Đã hoàn thành

* [x] Luyện tập list và dictionary bằng `student_records.py`.
* [x] Đọc và ghi JSON bằng `student_records_json.py`.
* [x] Đọc và ghi CSV bằng `student_records_csv.py`.
* [x] Áp dụng exception và nhập lại dữ liệu không hợp lệ trong `student_records.py`.
* [x] Xây project JSON-to-CSV bằng `projects/json_to_csv/convert_students.py`.
* [x] Xây CLI quản lý sinh viên trong `projects/student_manager/main.py`.
* [x] Tách các thao tác sinh viên sang module `projects/student_manager/student_service.py`.
* [x] Tổ chức `student_manager` thành package và chạy bằng `python -m`.
* [x] Thay dictionary bằng class `Student` trong CLI quản lý sinh viên.

## Đang thực hiện

* Củng cố method và type hint bằng class `Student`.

## Kiến thức đã có

### Python

* Biến và kiểu dữ liệu: đã thực hành cơ bản trong các bài Week 1.
* Điều kiện: đã thực hành cơ bản trong `student_score.py`.
* Vòng lặp: đã thực hành cơ bản trong các bài `student_records*`.
* Function: đã thực hành cơ bản với `classify_gpa`, `main`, `add_student` và `list_student`.
* Module: đã tách `add_student` và `list_student` từ `main.py` sang `student_service.py` và import lại.
* Package: đã tạo `__init__.py`, dùng relative import và chạy `python -m projects.student_manager.main`.
* File JSON/CSV: đã thực hành đọc, ghi và chuyển đổi JSON sang CSV.
* OOP: đã tạo class `Student`, constructor `__init__`, thuộc tính `name` và `gpa`.
* Type hint: đã thực hành cơ bản trong `classify_gpa`.
* List và dictionary: đã thực hành cơ bản qua `student_records.py` và CLI quản lý sinh viên.
* Exception: đã áp dụng `try`, `except`, `raise` và vòng lặp nhập lại trong `student_records.py`.

### SQL

* Đã có kiến thức SQL cơ bản.
* Cần đánh giá lại JOIN, GROUP BY, constraint và transaction.

### Git

* Đã thực hành `add`, `commit` và `push`; chưa học branch và merge.

### Backend

* Chưa học theo một lộ trình có hệ thống.

## Task ưu tiên

1. Củng cố method và type hint bằng class `Student`.
2. Ôn tuple và set.

## Task kế tiếp

* Củng cố method và type hint bằng class `Student`.
* Ôn tuple và set.

## Vấn đề đang gặp

Chưa có.

## Bằng chứng tiến độ

* Repository: 'backend-learning'
* Commit kiểm chứng CLI: `8c9e72b Build student manager CLI`.
* Bài gần nhất: `projects/student_manager/main.py`
* Test đã chạy: menu sai được báo lỗi; tên rỗng, GPA `abc` và GPA `10` yêu cầu nhập lại; danh sách rỗng an toàn và danh sách có `a/2`, `b/3`, `d/1` được in đúng.
* Kiểm chứng module: chạy `projects/student_manager/main.py`; import thành công, danh sách rỗng được xử lý và chương trình thoát bình thường.
* Commit module: `6874a64 Split student manager into a module`; dọn khoảng trắng: `a5a63e0 Remove trailing blank line`.
* Kiểm chứng package: `python -m projects.student_manager.main` chạy thành công; relative import, danh sách rỗng, thêm sinh viên và thoát đều hoạt động. Commit: `5d86529 Turn student manager into a package`.
* Kiểm chứng OOP: `Student` được tạo đúng; CLI thêm `a/2`, in `student.name` và `student.gpa`, danh sách rỗng và thoát đều hoạt động. Commit: `2185fa8 Introduce Student class`.
* Type hint: đã thực hành cơ bản trong `classify_gpa`.

## Quyết định cần giữ nguyên

* Backend chính sử dụng Python và FastAPI.
* PostgreSQL là database ứng dụng.
* Đồ án chính là Prompt/SQL-to-CSV.
* Không thêm RAG hoặc ChromaDB vào MVP.
* Không học nhiều framework Backend cùng lúc.

## Câu hỏi cho buổi học tiếp theo

* Task nhỏ nhất nên làm tiếp theo là gì?
* Cần học lý thuyết nào trước khi làm task đó?
* Definition of Done của task tiếp theo là gì?
