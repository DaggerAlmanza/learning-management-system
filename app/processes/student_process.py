from app.models.user_model import UserModel
from app.repositories.student_repository import StudentRepository
from rest_framework import (
    status,
)
from rest_framework.response import Response


repository = StudentRepository()
NO_UPDATED = "El estudiante no fue actualizado, "
NO_CREATED = "El estudiante no fue creado, "


class StudentProcess:
    def get_all(self):
        response = repository.get_all()
        return Response({
            "data": response,
            "message": "Estos son todos los datos de estudiante en la base de datos",
        })

    def save_data(self, data: dict, user: dict) -> dict:
        if not user["is_instructor"]:
            data.update({
                "user": UserModel.objects.get(id=user["id"])
            })
            response = repository.save_student(data)
            return Response({
                "data": response,
                "message":
                    "El estudiante fue creado exitosamente"
                    if len(response) == 1 else
                    NO_CREATED
            })
        response = {
            "data": "",
            "message": NO_CREATED +
            "La creación esta a cargo del mismo estudiante.",
        }
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    def get_by_id(self, id: int):
        response = repository.get_by_id(id)
        return Response({
            "data": response,
            "message": f"El estudiante con el id: {id}"
        })

    def update_data(self, data: dict, id: int, user: dict):
        if not user["is_instructor"]:
            student = repository.get_by_id(id)
            if student["user"]["id"] == user["id"]:
                response = repository.update_student(data, id)
                return Response({
                    "data": response,
                    "message":
                        f"El estudiante con id {id} fue actualizado"
                        if response else
                        f"El estudiante con id {id} no fue actualizado"
                })
            response = {
                "data": "",
                "message": NO_UPDATED +
                "las actualizaciones están a cargo del estudiante titular."
            }
        else:
            response = {
                "data": "",
                "message": NO_UPDATED +
                "el usuario es un Instructor",
            }
        return Response(response, status=status.HTTP_403_FORBIDDEN)

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
        response = {
            "data": "",
            "message": (
                "El estudiante no fue eliminado, "
                "La eliminado esta a cargo del los instructores.",
            )
        }
        return Response(response, status=status.HTTP_403_FORBIDDEN)
