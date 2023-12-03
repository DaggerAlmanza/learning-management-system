from app.models.student_model import StudentModel
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = [
            'id',
            'user',
            'address',
            'identification',
            'cell_phone',
            'guardians_name',
            'guardians_phone',
        ]
        read_only_fields = (
            'id',
            'user',
        )
