from app.models.instructor_model import InstructorModel
from app.repositories.course_repository import CourseRepository
from rest_framework import (
    status,
)
from rest_framework.response import Response


repository = CourseRepository()


class CourseProcess:
    def get_all(self):
        response = repository.get_all()
        return Response({
            "data": response,
            "message": "Estos son todos los datos de cursos en la base de datos",
        })

    def save_data(self, data: dict, user: dict) -> dict:
        if user["is_instructor"]:
            try:
                instructor = InstructorModel.objects.get(user=user["id"])
                data.update({
                    "instructor": instructor
                })
                response = repository.save_course(data)
                return Response({
                    "data": response,
                    "message":
                        "El curso fue creado exitosamente"
                        if len(response) == 1 else
                        "El curso no fue creado exitosamente"
                })
            except Exception as error:
                response = {
                    "data": {"error": str(error)},
                    "message": "El instructor no ha creado la cuenta de instructor",
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                "data": "",
                "message": "El curso no fue creado, el usuario es un Estudiante",
            }
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def get_by_id(self, id: int):
        response = repository.get_by_id(id)
        return Response({
            "data": response,
            "message": f"El curso con el id: {id}"
        })

    def update_data(self, data: dict, id: int, user: dict):
        if user["is_instructor"]:
            course = repository.get_by_id(id)
            if not course:
                return Response(
                    {
                        "data": "",
                        "message": f"El curso con id {id} no existe"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif course["instructor"]["id"] == user["id"]:
                response = repository.update_course(data, id)
                return Response({
                    "data": response,
                    "message":
                        f"El curso con id {id} fue actualizado"
                        if response else
                        f"El curso con id {id} no fue actualizado"
                })
            return Response(
                {
                    "data": "",
                    "message": "El curso no fue actualizado, " +
                    "las actualizaciones están a cargo solo del tutor."
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(
            {
                "data": "",
                "message": "El curso no fue actualizado, " +
                "el usuario es un Estudiante",
            },
            status=status.HTTP_403_FORBIDDEN
        )

    def delete_data(self, id: int, user: dict):
        if user["is_instructor"]:
            course = repository.get_by_id(id)
            if not course:
                return Response(
                    {
                        "data": "",
                        "message": f"El curso con id {id} no existe"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif course["instructor"]["id"] == user["id"]:
                response = repository.delete_course(id)
                return Response({
                    "data": response,
                    "message":
                        f"El curso con id {id} fue eliminado"
                        if response else
                        f"El curso con id {id} no fue eliminado"
                })
            return Response(
                {
                    "data": "",
                    "message": (
                        "El curso no fue eliminado, "
                        "las eliminaciones están a cargo solo del tutor."
                    )
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(
            {
                "data": "",
                "message": (
                    "El curso no fue eliminado, "
                    "el usuario es un Estudiante",
                )
            },
            status=status.HTTP_403_FORBIDDEN
        )
