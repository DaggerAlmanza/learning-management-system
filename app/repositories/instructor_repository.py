from app.helpers import GeneralHelpers
from app.models.instructor_model import InstructorModel
from app.models.course_model import CourseModel
from app.queries import Queries
from app.serializers.instructor_serializers import InstructorSerializer


class InstructorRepository(Queries):

    def __init__(self):
        self.conn = InstructorModel
        self.seria = InstructorSerializer

    def __get_by_id(self, id: str) -> dict:
        instructor = self.conn.objects.filter(id=id).first()
        if instructor:
            return instructor.to_json()
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
            instructor.to_json()
            for instructor in self.conn.objects.all()
        ]

    def get_all_courses(self, id: int) -> list:
        return [
            course.to_json()
            for course in CourseModel.objects.filter(instructor=id)
        ]

    def save_instructor(self, data: dict) -> dict:
        instructor = self.conn(**data)
        try:
            instructor.save()
        except Exception as error:
            return {"error": str(error)}
        return instructor.to_json()

    def update_instructor(self, params: dict, id: int) -> bool:
        data = self.conn.objects.filter(id=id).first()
        if not data:
            return False
        self.__update(data, params)
        return True
