from app.repositories.user_repository import UserRepository
from rest_framework.response import Response


repository = UserRepository()


class UserProcess:
    def get_all(self):
        response = repository.get_all()
        return Response({
            "data": response,
            "message": "Estos son todos los datos de usarios en la base de datos"
        })

    def save_data(self, data: dict) -> dict:
        response = repository.save_user(data)
        return Response({
            "data": response,
            "message":
                "El usuario fue creado exitosamente"
                if len(response) == 1 else
                "El usuario no fue creado exitosamente"
        })

    def get_by_id(self, id: int):
        response = repository.get_by_id(id)
        return Response({
            "data": response,
            "message": f"El usuario con el id: {id}"
        })

    def update_data(self, data: dict, id):
        response = repository.update_user(data, id)
        return Response({
            "data": response,
            "message":
                f"El usuario con id {id} fue actualizado"
                if len(response) == 1 else
                f"El usuario con id {id} no fue actualizado"
        })

    def delete_data(self, id: int):
        response = repository.delete_one(id)
        return Response({
            "data": response,
            "message":
                f"El usuario con id {id} fue eliminado"
                if response else
                f"El usuario con id {id} no fue eliminado"
        })
