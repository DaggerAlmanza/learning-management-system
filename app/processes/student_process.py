from app.models.course_model import CourseModel
from app.models.user_model import UserModel
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from rest_framework import (
    status,
)
from rest_framework.response import Response


repository = StudentRepository()
repository_course = CourseRepository()
NO_UPDATED = "El estudiante no fue actualizado, "
NO_CREATED = "El estudiante no fue creado, "


class StudentProcess:
    def __course_verification(self, data: dict):
        data["courses"] = [
            id for id in data["courses"]
            if repository_course.get_by_id(id)
        ]

    def __courses_list(self, courses: list) -> list:
        return [
            CourseModel.objects.get(id=id) for id in courses
        ]

    def get_all(self):
        response = repository.get_all()
        return Response({
            "data": response,
            "message": "Estos son todos los datos de estudiante en la base de datos",
        })

    def save_data(self, data: dict, user: dict) -> dict:
        if not user["is_instructor"]:
            self.__course_verification(data)
            courses = self.__courses_list(data["courses"])
            data.update({
                "user": UserModel.objects.get(id=user["id"])
            })
            print(data.pop("courses"))
            response = repository.save_student(data, courses)
            return Response({
                "data": response,
                "message":
                    "El estudiante fue creado exitosamente"
                    if len(response) > 1 else
                    NO_CREATED
            })
        return Response(
            {
                "data": "",
                "message": NO_CREATED +
                "La creación esta a cargo del mismo estudiante."
            },
            status=status.HTTP_403_FORBIDDEN
        )

    def get_by_id(self, id: int):
        response = repository.get_by_id(id)
        return Response({
            "data": response,
            "message": f"El estudiante con el id: {id}"
        })

    def update_data(self, data: dict, id: int, user: dict):
        student = repository.get_by_id(id)
        if not user["is_instructor"] and student:
            self.__course_verification(data)
            courses = self.__courses_list(data["courses"])
            if student["user"]["id"] == user["id"]:
                print(data.pop("courses"))
                response = repository.update_student(data, id, courses)
                return Response({
                    "data": response,
                    "message":
                        f"El estudiante con id {id} fue actualizado"
                        if response else
                        f"El estudiante con id {id} no fue actualizado"
                })
            return Response(
                {
                    "data": "",
                    "message": NO_UPDATED +
                    "las actualizaciones están a cargo del estudiante titular."
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(
            {
                "data": "",
                "message": NO_UPDATED +
                "el usuario es un Instructor " +
                "O puede que este ingresando un ID no valido",
            },
            status=status.HTTP_403_FORBIDDEN
        )

    def delete_data(self, id: int, user: dict):
        if user["is_instructor"]:
            response = repository.delete_one(id)
            return Response({
                "data": response,
                "message":
                    f"El estudiante con id {id} fue eliminado"
                    if response else
                    f"El estudiante con id {id} no fue eliminado"
            })
        return Response(
            {
                "data": "",
                "message": (
                    "El estudiante no fue eliminado, "
                    "La eliminado esta a cargo del los instructores.",
                )
            },
            status=status.HTTP_403_FORBIDDEN
        )
