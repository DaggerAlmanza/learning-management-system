from app.processes.student_process import StudentProcess
from app.serializers.student_serializers import StudentSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


student_process = StudentProcess()


class StudentView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    @extend_schema(
        tags=['student'],
        request=StudentSerializer,
        description="""Crear Estudiante: \n
        ◦ Permite la creación de un nuevo estudiante en el sistema, asegurando que el usuario asociado no sea un instructor.
        """
    )
    def post(self, request):
        return student_process.save_data(request.data, request._user.to_json())

    @extend_schema(
        tags=['student'],
        description="""Obtener Todos los Estudiantes: \n
        ◦ Este endpoint proporciona una lista completa de todos los estudiantes registrados en la base de datos del sistema.
        """
    )
    def get(self, request):
        return student_process.get_all()


class StudentPkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer

    @extend_schema(
        tags=['student'],
        description="""Obtener Estudiante por ID: \n
        ◦ Este endpoint recupera la información detallada de un estudiante específico según el identificador proporcionado.
        """
    )
    def get(self, request, pk, *args, **kwargs):
        return student_process.get_by_id(pk)

    @extend_schema(
        tags=['student'],
        request=StudentSerializer,
        description="""Actualizar Estudiante por ID: \n
        ◦ Permite la modificación de la información de un estudiante existente utilizando su identificador único, con la restricción de que solo el mismo estudiante puede realizar la actualización.
        """
    )
    def put(self, request, pk, *args, **kwargs):
        return student_process.update_data(
            request.data,
            pk,
            request._user.to_json()
        )

    @extend_schema(
        tags=['student'],
        description="""Eliminar Estudiante por ID: \n
        ◦ Elimina de forma permanente la cuenta de un estudiante específico, exigiendo que la acción sea realizada por un instructor.
        """
    )
    def delete(self, request, pk, *args, **kwargs):
        return student_process.delete_data(pk, request._user.to_json())
