from app.processes.course_process import CourseProcess
from app.serializers.course_serializers import CourseSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

course_process = CourseProcess()


class CourseView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    @extend_schema(
        tags=['course'],
        request=CourseSerializer,
        description="""Crear Curso:\n
        ◦ Permite la creación de un nuevo curso en el sistema, asegurando que el usuario asociado no sea un estudiante.
        """
    )
    def post(self, request):
        return course_process.save_data(request.data, request._user.to_json())

    @extend_schema(
        tags=['course'],
        description="""Obtener Todos los Cursos: \n
        ◦ Este endpoint proporciona una lista completa de todos los cursos registrados en la base de datos del sistema.
        """
    )
    def get(self, request):
        return course_process.get_all()


class CoursePkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = CourseSerializer

    @extend_schema(
        tags=['course'],
        description="""Obtener Curso por ID: \n
        ◦ Este endpoint recupera la información detallada de un curso específico según el identificador proporcionado.
        """
    )
    def get(self, request, pk, *args, **kwargs):
        return course_process.get_by_id(pk)

    @extend_schema(
        tags=['course'],
        request=CourseSerializer,
        description="""Actualizar Curso por ID:\n
        ◦ Permite la modificación de la información de un curso existente utilizando su identificador único, con la restricción de que solo el mismo instructor del curso puede realizar la actualización.
        """
    )
    def put(self, request, pk, *args, **kwargs):
        return course_process.update_data(request.data, pk, request._user.to_json())

    @extend_schema(
        tags=['course'],
        description="""Eliminar Curso por ID: \n
        ◦ Elimina de forma permanente la información de un curso específico, exigiendo que la acción sea realizada por el mismo instructor que creó el curso.
        """
    )
    def delete(self, request, pk, *args, **kwargs):
        return course_process.delete_data(pk, request._user.to_json())
