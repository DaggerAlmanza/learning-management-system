from app.processes.student_process import (
    delete_data_process,
    get_all_process,
    get_by_id_process,
    save_data_process,
    update_data_process,
)
from app.serializers.student_serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


class StudentView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    @extend_schema(
        tags=['student'],
        request=StudentSerializer
    )
    def post(self, request):
        return save_data_process(request.data, request._user.to_json())

    @extend_schema(tags=['student'])
    def get(self, request):
        return get_all_process()


class StudentPkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    @extend_schema(tags=['student'])
    def get(self, request, pk, *args, **kwargs):
        return get_by_id_process(pk)

    @extend_schema(
        tags=['student'],
        request=StudentSerializer
    )
    def put(self, request, pk, *args, **kwargs):
        return update_data_process(request.data, pk, request._user.to_json())

    @extend_schema(tags=['student'])
    def delete(self, request, pk, *args, **kwargs):
        return delete_data_process(pk, request._user.to_json())
