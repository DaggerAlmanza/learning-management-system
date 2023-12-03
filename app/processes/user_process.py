from app.repositories.user_repository import UserRepository
from rest_framework.response import Response


repository = UserRepository()


def get_all_process():
    response = repository.get_all()
    return Response({
        "data": response,
        "message": "Estos son todos los datos de usarios en la base de datos"
    })


def save_data_process(data: dict) -> dict:
    response = repository.save_user(data)
    return Response({
        "data": response,
        "message":
            "El usuario fue creado exitosamente"
            if type(response) is dict else
            "El usuario no fue creado exitosamente"
    })


def get_by_id_process(id: int):
    response = repository.get_by_id(id)
    return Response({
        "data": response,
        "message": f"El usuario con el id: {id}"
    })


def update_data_process(data: dict, id):
    response = repository.update_user(data, id)
    return Response({
        "data": response,
        "message": f"El usuario con id {id} fue actualizado"
    })


def delete_data_process(id: int):
    response = repository.delete_one(id)
    return Response({
        "data": response,
        "message": f"El usuario con id {id} fue eliminado"
    })
