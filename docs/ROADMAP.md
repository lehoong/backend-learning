---

title: Backend Learning Roadmap
duration_weeks: 24
hours_per_week: 8
primary_language: Python
main_project: Prompt/SQL-to-CSV
last_updated: 2026-07-31
------------------------

# Backend Learning Roadmap

## Mục tiêu cuối

Hoàn thành một REST API Backend bằng Python và một đồ án Prompt/SQL-to-CSV có:

* REST API.
* PostgreSQL.
* SQLAlchemy và migration.
* Core data generator.
* SQL parser.
* CSV validation.
* Automated tests.
* Docker Compose.
* Tài liệu kiến trúc và hướng dẫn chạy.

---

## Giai đoạn 1 — Python và Git

**Thời gian:** Tuần 1–4

### Kiến thức

* Biến, kiểu dữ liệu và toán tử.
* Điều kiện và vòng lặp.
* Function.
* List, dictionary, tuple và set.
* Exception.
* Module và package.
* File JSON và CSV.
* OOP cơ bản.
* Type hint.
* Virtual environment.
* Git và GitHub workflow.

### Sản phẩm

* Bộ bài tập Python.
* CLI quản lý sinh viên.
* Project JSON-to-CSV.
* Repository có README và lịch sử commit rõ ràng.

### Điều kiện hoàn thành

* Tự viết được chương trình nhiều file.
* Đọc và ghi được JSON, CSV.
* Xử lý được input không hợp lệ.
* Sử dụng được branch, commit, push và merge.

---

## Giai đoạn 2 — SQL và PostgreSQL

**Thời gian:** Tuần 5–7

### Kiến thức

* Database quan hệ.
* DDL và DML.
* Primary key và foreign key.
* Constraint.
* JOIN.
* GROUP BY và HAVING.
* Aggregate function.
* Transaction.
* Index cơ bản.
* Thiết kế quan hệ dữ liệu.

### Sản phẩm

* Database quản lý công việc.
* File schema SQL.
* File seed SQL.
* Ít nhất 20 truy vấn thực hành.

### Điều kiện hoàn thành

* Tự thiết kế được database nhiều bảng.
* Viết được JOIN và truy vấn tổng hợp.
* Hiểu vai trò của constraint và transaction.

---

## Giai đoạn 3 — HTTP và FastAPI

**Thời gian:** Tuần 8–10

### Kiến thức

* Client và server.
* HTTP request và response.
* HTTP method.
* Status code.
* Header.
* Path, query và body parameter.
* REST API.
* FastAPI router.
* Pydantic request và response model.
* Validation.
* Exception handling.
* OpenAPI và Swagger.

### Sản phẩm

* Todo REST API lưu dữ liệu trong memory.

### Điều kiện hoàn thành

* Có đầy đủ endpoint CRUD.
* Status code hợp lý.
* Request validation hoạt động.
* Router và service được tách riêng.

---

## Giai đoạn 4 — PostgreSQL, SQLAlchemy và kiến trúc

**Thời gian:** Tuần 11–14

### Kiến thức

* SQLAlchemy Engine và Session.
* ORM model.
* Relationship.
* Transaction.
* Repository pattern.
* Alembic migration.
* Environment variable.
* Layered architecture.

### Sản phẩm

* Todo API kết nối PostgreSQL.
* Migration tạo database.
* Filter, search và pagination cơ bản.

### Điều kiện hoàn thành

* Router không chứa business logic.
* Service không phụ thuộc trực tiếp vào HTTP.
* Repository quản lý thao tác database.
* Có commit và rollback phù hợp.

---

## Giai đoạn 5 — Testing và chất lượng code

**Thời gian:** Tuần 15–17

### Kiến thức

* Unit test.
* Integration test.
* API test.
* Fixture.
* Parametrize.
* Mock.
* Test database.
* Ruff.
* Type checking cơ bản.

### Sản phẩm

* Test suite cho Todo API.
* Test cho service, repository và endpoint.
* Báo cáo coverage.

### Điều kiện hoàn thành

* Business logic chính có test.
* API lỗi và API thành công đều được kiểm thử.
* Test có thể chạy bằng một command.

---

## Giai đoạn 6 — Docker và bảo mật

**Thời gian:** Tuần 18–20

### Kiến thức

* Docker image và container.
* Dockerfile.
* Docker Compose.
* Volume và network.
* Environment variable.
* Health check.
* Logging.
* Authentication cơ bản.
* Password hashing.
* Input validation.
* SQL injection.

### Sản phẩm

* FastAPI và PostgreSQL chạy bằng Docker Compose.

### Điều kiện hoàn thành

Ứng dụng chạy được bằng:

```bash
docker compose up --build
```

---

## Giai đoạn 7 — Đồ án Prompt/SQL-to-CSV

**Thời gian:** Tuần 21–24

### Phần 1: Core generator

* GenerationPlan.
* Pydantic validation.
* Faker.
* Sequence.
* Integer, float, string, boolean và date.
* Choice.
* Min/max.
* Unique.
* Nullable.
* Seed.
* CSV export.

### Phần 2: Job API

* Tạo generation job.
* Lưu metadata vào PostgreSQL.
* Preview dữ liệu.
* Download CSV.
* Validation report.

### Phần 3: SQL parser

* Parse SQL bằng SQLGlot.
* Phân tích SELECT.
* WHERE.
* AND và OR.
* Toán tử so sánh.
* IN.
* BETWEEN.
* INNER JOIN.
* LIMIT.

### Phần 4: Validation

* Load CSV vào DuckDB.
* Chạy lại truy vấn.
* Sinh expected result.
* Báo cáo kết quả.

### Phần 5: LLM

* Chuyển prompt thành GenerationPlan.
* Validate output bằng Pydantic.
* Không để LLM sinh trực tiếp toàn bộ CSV.

### Điều kiện hoàn thành MVP

* Nhập prompt hoặc SQL + DDL.
* Sinh được một hoặc nhiều CSV.
* Constraint cơ bản hợp lệ.
* Query kiểm thử chạy được.
* Có validation report.
* Có API documentation.
* Có automated tests.
* Chạy được bằng Docker Compose.
