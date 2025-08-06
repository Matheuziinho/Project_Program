from bisect import insort
from functools import reduce

class GradeSchool:
    def __init__(self) -> None:
        self.students = {}

    def add_student(self, name: str, grade: int) -> None:
        if grade not in self.students:
            self.students[grade] = []
        insort(self.students[grade], name)

    def get_roster(self) -> list[str]:
        return reduce(lambda acc, grade: acc + self.students[grade], sorted(self.students), [])