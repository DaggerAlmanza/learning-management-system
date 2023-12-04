from app.models.user_model import UserModel
from app.queries import Queries
from app.serializers.user_serializers import UserSerializer


class UserRepository(Queries):

    def __init__(self):
        self.conn = UserModel
        self.seria = UserSerializer

    def get_by_id(self, id: str) -> dict:
        response = self.find_one(
            id
        )
        return response

    def get_all(self) -> list:
        response = self.find_many()
        return response

    def save_user(self, data: dict) -> dict:
        user = self.conn(**data)
        user.set_password(data.get("password"))
        try:
            user.save()
        except Exception as error:
            return str(error)
        return user.to_json()

    def update_user(self, params: dict, id: int) -> dict:
        data = self.conn.objects.filter(id=id).first()
        if data:
            data.set_password(params.get("password"))
            params.update({
                "password": data.password
            })
            response = self.seria(data, data=params)
            if response.is_valid():
                response.save()
                return response.data
            return response.errors
        return {}
