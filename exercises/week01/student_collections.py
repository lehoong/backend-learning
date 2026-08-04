students = [
    {
        "name": "An",
        "gpa": 3.5
    },
    {
        "name": "Binh",
        "gpa": 2.5
    },
    {
        "name": "Chi",
        "gpa": 3.5
    },
    {
        "name": "An",
        "gpa": 3.5
    }
]

student_pairs = []

unique_names = set()

for student in students:
    name = student["name"]
    gpa = student["gpa"]

    student_pair = (name, gpa)
    student_pairs.append(student_pair)
    unique_names.add(name)

print("Danh sách tuple:", student_pairs)
print("Tên không trùng: ", unique_names)
print("Số lượng tên khác nhau:", len(unique_names))