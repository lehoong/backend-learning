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

Củng cố CLI quản lý sinh viên bằng cách tổ chức lại các kỹ năng Python đã học.

## Đã hoàn thành

* [x] Luyện tập list và dictionary bằng `student_records.py`.
* [x] Đọc và ghi JSON bằng `student_records_json.py`.
* [x] Đọc và ghi CSV bằng `student_records_csv.py`.
* [x] Áp dụng exception và nhập lại dữ liệu không hợp lệ trong `student_records.py`.
* [x] Xây project JSON-to-CSV bằng `projects/json_to_csv/convert_students.py`.

## Đang thực hiện

* Củng cố CLI quản lý sinh viên.

## Kiến thức đã có

### Python

* Biến và kiểu dữ liệu: đã thực hành cơ bản trong các bài Week 1.
* Điều kiện: đã thực hành cơ bản trong `student_score.py`.
* Vòng lặp: đã thực hành cơ bản trong các bài `student_records*`.
* Function: đã thực hành cơ bản với `classify_gpa` và `main`.
* File JSON/CSV: đã thực hành đọc, ghi và chuyển đổi JSON sang CSV.
* OOP: đã từng học nhưng cần ôn lại.
* Type hint: đã thực hành cơ bản trong `classify_gpa`.
* List và dictionary: đã thực hành cơ bản qua `student_records.py`.
* Exception: đã áp dụng `try`, `except`, `raise` và vòng lặp nhập lại trong `student_records.py`.

### SQL

* Đã có kiến thức SQL cơ bản.
* Cần đánh giá lại JOIN, GROUP BY, constraint và transaction.

### Git

* Đã thực hành `add`, `commit` và `push`; chưa học branch và merge.

### Backend

* Chưa học theo một lộ trình có hệ thống.

## Task ưu tiên

1. Củng cố CLI quản lý sinh viên.
2. Ôn điều kiện, vòng lặp và function qua project nhỏ.
3. Chuẩn bị học module và package.

## Task kế tiếp

* Củng cố CLI quản lý sinh viên.
* Chuẩn bị học module và package.

## Vấn đề đang gặp

Chưa có.

## Bằng chứng tiến độ

* Repository: 'backend-learning'
* Commit kiểm chứng bài gần nhất: `253f99d Build JSON to CSV converter`.
* Bài gần nhất: `projects/json_to_csv/convert_students.py`
* Test đã chạy: `convert_students.py` báo đã chuyển 3 sinh viên; JSON và CSV có cùng 3 bản ghi, gồm đúng tên tiếng Việt và GPA.
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
