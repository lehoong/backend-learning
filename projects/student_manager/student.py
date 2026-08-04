class Student:
    def __init__(self, name: str, gpa: float) -> None:
        self.name = name
        self.gpa = gpa

    def display(self, index: int) -> str:
        return f"STT: {index}, Tên: {self.name}, GPA: {self.gpa}"
