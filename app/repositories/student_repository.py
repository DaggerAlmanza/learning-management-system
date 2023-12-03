from app.queries import Queries
from app.serializers.student_serializers import StudentSerializer
from app.models.student_model import StudentModel
from app.helpers import GeneralHelpers


class StudentRepository(Queries):

    def __init__(self):
        self.conn = StudentModel
        self.seria = StudentSerializer

    def __get_by_id(self, id: str) -> dict:
        student = self.conn.objects.filter(id=id).first()
        if student:
            return student.to_json()
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
        ]
        GeneralHelpers.update_object_attrs(data, keys, params)
        data.save()

    def get_by_id(self, id: str) -> dict:
        response = self.__get_by_id(id)
        return response

    def get_all(self) -> list:
        return [
            student.to_json()
            for student in self.conn.objects.all()
        ]

    def save_student(self, data: dict) -> dict:
        student = self.conn(**data)
        try:
            student.save()
        except Exception as error:
            return {"error": str(error)}
        return student.to_json()

    def update_student(self, params: dict, id: int) -> bool:
        data = self.conn.objects.filter(id=id).first()
        if not data:
            return False
        self.__update(data, params)
        return True
