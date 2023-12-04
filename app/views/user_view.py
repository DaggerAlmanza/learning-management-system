from app.processes.user_process import UserProcess
from app.serializers.user_serializers import UserSerializer
from drf_spectacular.utils import (
    extend_schema,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


user_process = UserProcess()


class UserView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @extend_schema(
        tags=['user'],
        request=UserSerializer,
        description="""Crear Usuario : \n
        • Permite la creación de un nuevo usuario en el sistema.""",
    )
    def post(self, request):
        return user_process.save_data(request.data)

    @extend_schema(
        tags=['user'],
        description="""Obtener Todos los Usuarios: \n
        • Este endpoint proporciona una lista completa de todos los usuarios registrados en la base de datos del sistema.
        """
    )
    def get(self, request):
        return user_process.get_all()


class UserPkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @extend_schema(
        tags=['user'],
        description="""Obtener Usuario por ID: \n
        • Este endpoint recupera la información detallada de un usuario específico según el identificador proporcionado.
        """
    )
    def get(self, request, pk, *args, **kwargs):
        return user_process.get_by_id(pk)

    @extend_schema(
        tags=['user'],
        request=UserSerializer,
        description="""Actualizar Usuario por ID: \n
        • Permite la modificación de la información de un usuario existente utilizando su identificador único.
        """
    )
    def put(self, request, pk, *args, **kwargs):
        return user_process.update_data(request.data, pk)

    @extend_schema(
        tags=['user'],
        description="""Eliminar Usuario por ID: \n
        • Elimina de forma permanente la cuenta de un usuario específico según el identificador proporcionado.
        """
    )
    def delete(self, request, pk, *args, **kwargs):
        return user_process.delete_data(pk)


class CurrentUser(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['user'],
        description="""Obtener Usuario Actual: \n
        • Este endpoint permite consultar la información del usuario actualmente autenticado en el sistema.
        """
    )
    def get(self, request, format=None):
        content = {
            "user": request._user.to_json(),
            "auth": request.auth.payload
        }
        return Response({
            "data": content,
            "message": "Usuario actual"
        })

    def current_user_int(self, request, format=None):
        return user_process.request._user.to_json()
