from app.processes.instructor_process import InstructorProcess
from app.serializers.instructor_serializers import InstructorSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


instructor_process = InstructorProcess()


class InstructorView(
    APIView
):
    permission_classes = [IsAuthenticated]
    serializer_class = InstructorSerializer

    @extend_schema(
        tags=['instructor'],
        request=InstructorSerializer,
        description="""Crear Instructor: \n
        ◦ Permite la creación de un nuevo instructor en el sistema, asegurando que el usuario asociado no sea un estudiante.
        """
    )
    def post(self, request):
        return instructor_process.save_data(request.data, request._user.to_json())

    @extend_schema(
        tags=['instructor'],
        description="""Obtener Todos los Instructores: \n
        ◦ Este endpoint proporciona una lista completa de todos los instructores registrados en la base de datos del sistema.
        """
    )
    def get(self, request):
        return instructor_process.get_all()


class InstructorPkView(
    APIView,
):
    permission_classes = [IsAuthenticated]
    serializer_class = InstructorSerializer

    @extend_schema(
        tags=['instructor'],
        description="""Obtener Instructor por ID: \n
        ◦ Este endpoint recupera la información detallada de un instructor específico según el identificador proporcionado.
        """
    )
    def get(self, request, pk, *args, **kwargs):
        return instructor_process.get_by_id(pk)

    @extend_schema(
        tags=['instructor'],
        request=InstructorSerializer,
        description="""Actualizar Instructor por ID:\n
        ◦ Permite la modificación de la información de un instructor existente utilizando su identificador único, con la restricción de que solo el mismo instructor puede realizar la actualización.
        """
    )
    def put(self, request, pk, *args, **kwargs):
        return instructor_process.update_data(request.data, pk, request._user.to_json())

    @extend_schema(
        tags=['instructor'],
        description=""" Eliminar Instructor por ID:\n
        ◦ Elimina de forma permanente la cuenta de un instructor específico, exigiendo que la acción sea realizada por el mismo instructor.
        """
    )
    def delete(self, request, pk, *args, **kwargs):
        return instructor_process.delete_data(pk, request._user.to_json())
