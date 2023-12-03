from app.queries import Queries
from app.serializers.course_serializers import CourseSerializer
from app.models.course_model import CourseModel
from app.helpers import GeneralHelpers


class CourseRepository(Queries):

    def __init__(self):
        self.conn = CourseModel
        self.seria = CourseSerializer

    def __get_by_id(self, id: str) -> dict:
        course = self.conn.objects.filter(id=id).first()
        if course:
            return course.to_json()
        return {}

    def __update(
        self,
        data,
        params: dict,
    ) -> None:
        keys = [
            "name",
            "description",
        ]
        GeneralHelpers.update_object_attrs(data, keys, params)
        data.save()

    def get_by_id(self, id: str) -> dict:
        response = self.__get_by_id(id)
        return response

    def get_all(self) -> list:
        return [
            course.to_json()
            for course in self.conn.objects.all()
        ]

    def save_course(self, data: dict) -> dict:
        course = self.conn(**data)
        try:
            course.save()
        except Exception as error:
            return {"error": str(error)}
        return course.to_json()

    def update_course(self, params: dict, id: int) -> bool:
        data = self.conn.objects.filter(id=id).first()
        if not data:
            return False
        self.__update(data, params)
        return True

    def delete_course(self, id: int) -> bool:
        data = self.conn.objects.filter(id=id).first()
        if not data:
            return False
        data.delete()
        return True
