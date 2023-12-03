from app.processes.instructor_process import (
    delete_data_process,
    get_all_process,
    get_by_id_process,
    save_data_process,
    update_data_process,
)
from app.serializers.instructor_serializers import InstructorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


class InstructorView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = InstructorSerializer

    @extend_schema(
        tags=['instructor'],
        request=InstructorSerializer
    )
    def post(self, request):
        return save_data_process(request.data, request._user.to_json())

    @extend_schema(tags=['instructor'])
    def get(self, request):
        return get_all_process()


class InstructorPkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = InstructorSerializer

    @extend_schema(tags=['instructor'])
    def get(self, request, pk, *args, **kwargs):
        return get_by_id_process(pk)

    @extend_schema(
        tags=['instructor'],
        request=InstructorSerializer
    )
    def put(self, request, pk, *args, **kwargs):
        return update_data_process(request.data, pk, request._user.to_json())

    @extend_schema(tags=['instructor'])
    def delete(self, request, pk, *args, **kwargs):
        return delete_data_process(pk, request._user.to_json())
