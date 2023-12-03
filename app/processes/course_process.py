from app.repositories.course_repository import CourseRepository
from rest_framework.response import Response
from rest_framework import (
    status,
)
from app.models.instructor_model import InstructorModel


repository = CourseRepository()


# def internal_update_or_delete_process():


def get_all_process():
    response = repository.get_all()
    return Response({
        "data": response,
        "message": "Estos son todos los datos de cursos en la base de datos",
    })


def save_data_process(data: dict, user: dict) -> dict:
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


def get_by_id_process(id: int):
    response = repository.get_by_id(id)
    return Response({
        "data": response,
        "message": f"El curso con el id: {id}"
    })


def update_data_process(data: dict, id: int, user: dict):
    if user["is_instructor"]:
        course = repository.get_by_id(id)
        if course["instructor"]["id"] == user["id"]:
            response = repository.update_course(data, id)
            return Response({
                "data": response,
                "message":
                    f"El curso con id {id} fue actualizado"
                    if response else
                    f"El curso con id {id} no fue actualizado"
            })
        response = {
            "data": "",
            "message": "El curso no fue actualizado, " +
            "las actualizaciones están a cargo solo del tutor."
        }
    else:
        response = {
            "data": "",
            "message": "El curso no fue actualizado, " +
            "el usuario es un Estudiante",
        }
    return Response(response, status=status.HTTP_403_FORBIDDEN)


def delete_data_process(id: int, user: dict):
    if user["is_instructor"]:
        course = repository.get_by_id(id)
        if course["instructor"]["id"] == user["id"]:
            response = repository.delete_course(id)
            return Response({
                "data": response,
                "message":
                    f"El curso con id {id} fue eliminado"
                    if response else
                    f"El curso con id {id} no fue eliminado"
            })
        response = {
            "data": "",
            "message": (
                "El curso no fue eliminado, "
                "las eliminaciones están a cargo solo del tutor."
            )
        }
    else:
        response = {
            "data": "",
            "message": (
                "El curso no fue eliminado, "
                "el usuario es un Estudiante",
            )
        }
    return Response(response, status=status.HTTP_403_FORBIDDEN)
