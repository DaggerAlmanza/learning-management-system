from app.processes.user_process import (
    delete_data_process,
    get_all_process,
    get_by_id_process,
    save_data_process,
    update_data_process,
)
from app.serializers.user_serializers import UserSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @extend_schema(
        tags=['user'],
        request=UserSerializer
    )
    def post(self, request):
        return save_data_process(request.data)

    @extend_schema(tags=['user'])
    def get(self, request):
        return get_all_process()


class UserPkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @extend_schema(tags=['user'])
    def get(self, request, pk, *args, **kwargs):
        return get_by_id_process(pk)

    @extend_schema(
        tags=['user'],
        request=UserSerializer
    )
    def put(self, request, pk, *args, **kwargs):
        return update_data_process(request.data, pk)

    @extend_schema(tags=['user'])
    def delete(self, request, pk, *args, **kwargs):
        return delete_data_process(pk)


class CurrentUser(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['user'])
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
        return request._user.to_json()
