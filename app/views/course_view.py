from app.processes.course_process import (
    delete_data_process,
    get_all_process,
    get_by_id_process,
    save_data_process,
    update_data_process,
)
from app.serializers.course_serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


class CourseView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    @extend_schema(
        tags=['course'],
        request=CourseSerializer
    )
    def post(self, request):
        return save_data_process(request.data, request._user.to_json())

    @extend_schema(tags=['course'])
    def get(self, request):
        return get_all_process()


class CoursePkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    @extend_schema(tags=['course'])
    def get(self, request, pk, *args, **kwargs):
        return get_by_id_process(pk)

    @extend_schema(
        tags=['course'],
        request=CourseSerializer
    )
    def put(self, request, pk, *args, **kwargs):
        return update_data_process(request.data, pk, request._user.to_json())

    @extend_schema(tags=['course'])
    def delete(self, request, pk, *args, **kwargs):
        return delete_data_process(pk, request._user.to_json())
