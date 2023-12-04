from app.helpers import GeneralHelpers
from app.models.student_model import StudentModel
from app.queries import Queries
from app.serializers.student_serializers import StudentSerializer


class StudentRepository(Queries):

    def __init__(self):
        self.conn = StudentModel
        self.seria = StudentSerializer

    def __get_by_id(self, id: str) -> dict:
        student = self.conn.objects.filter(id=id).first()
        if student:
            student_current = student.to_json()
            student_current.update({
                "courses": [
                    course.to_json()
                    for course in student.courses.all()
                    ]
            })
            return student_current
        return {}

    def __update(
        self,
        data,
        params: dict,
    ) -> None:
        keys = [
            "address",
            "identification",
            "cell_phone",
            "guardians_name",
            "guardians_phone",
            "courses",
        ]
        GeneralHelpers.update_object_attrs(data, keys, params)
        data.save()

    def get_by_id(self, id: str) -> dict:
        response = self.__get_by_id(id)
        return response

    def get_all(self) -> list:
        students: list = []
        for student in self.conn.objects.all():
            student_current: dict = student.to_json()
            student_current.update({
                "courses": [
                    course.to_json()
                    for course in student.courses.all()
                ]
            })
            students.append(student_current)
        return students

    def save_student(self, data: dict, courses: list) -> dict:
        try:
            student = self.conn.objects.create(**data)
            student.courses.set(courses)
            student.save()
        except Exception as error:
            return {"error": str(error)}
        return student.to_json()

    def update_student(self, params: dict, id: int, courses: list) -> bool:
        data = self.conn.objects.filter(id=id).first()
        if not data:
            return False
        data.courses.set(courses)
        self.__update(data, params)
        return True
