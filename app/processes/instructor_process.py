from app.models.user_model import UserModel
from app.repositories.instructor_repository import InstructorRepository
from rest_framework import (
    status,
)
from rest_framework.response import Response


repository = InstructorRepository()


class InstructorProcess:
    def get_all_courses(self, user: dict):
        instructor = repository.get_by_id(user["id"])
        if not instructor:
            return Response(
                {
                    "data": "",
                    "message": f"El instructor con id {id} no existe"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        response = repository.get_all_courses(instructor["id"])
        return Response({
            "data": response,
            "message": "Estos son todos los datos de cursos del instructor en la base de datos",
        })

    def get_all(self):
        response = repository.get_all()
        return Response({
            "data": response,
            "message": "Estos son todos los datos de instructors en la base de datos",
        })

    def save_data(self, data: dict, user: dict) -> dict:
        if user["is_instructor"]:
            data.update({
                "user": UserModel.objects.get(id=user["id"])
            })
            response = repository.save_instructor(data)
            return Response({
                "data": response,
                "message":
                    "El instructor fue creado exitosamente"
                    if len(response) == 1 else
                    "El instructor no fue creado exitosamente"
            })
        response = {
            "data": "",
            "message": "El instructor no fue creado, el usuario es un Estudiante",
        }
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def get_by_id(self, id: int):
        response = repository.get_by_id(id)
        return Response({
            "data": response,
            "message": f"El instructor con el id: {id}"
        })

    def update_data(self, data: dict, id: int, user: dict):
        if user["is_instructor"]:
            instructor = repository.get_by_id(id)
            if not instructor:
                return Response(
                    {
                        "data": "",
                        "message": f"El instructor con id {id} no existe"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif instructor["user"]["id"] == user["id"]:
                response = repository.update_instructor(data, id)
                return Response({
                    "data": response,
                    "message":
                        f"El instructor con id {id} fue actualizado"
                        if response else
                        f"El instructor con id {id} no fue actualizado"
                })
            return Response(
                {
                    "data": "",
                    "message": "El instructor no fue actualizado, " +
                    "las actualizaciones están a cargo solo del tutor."
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(
            {
                "data": "",
                "message": "El instructor no fue actualizado, " +
                "el usuario es un Estudiante",
            },
            status=status.HTTP_403_FORBIDDEN
        )

    def delete_data(self, id: int, user: dict):
        if user["is_instructor"]:
            instructor = repository.get_by_id(id)
            if not instructor:
                return Response(
                    {
                        "data": "",
                        "message": f"El instructor con id {id} no existe"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif instructor["user"]["id"] == user["id"]:
                response = repository.delete_one(id)
                return Response({
                    "data": response,
                    "message":
                        f"El instructor con id {id} fue eliminado"
                        if response else
                        f"El instructor con id {id} no fue eliminado"
                })
            return Response({
                    "data": "",
                    "message": (
                        "El instructor no fue eliminado, "
                        "las eliminaciones están a cargo solo del tutor."
                    )
                },
                status=status.HTTP_403_FORBIDDEN
            )
        return Response(
            {
                "data": "",
                "message": (
                    "El instructor no fue eliminado, "
                    "el usuario es un Estudiante",
                )
            },
            status=status.HTTP_403_FORBIDDEN
        )
