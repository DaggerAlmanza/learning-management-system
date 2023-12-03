from app.models.instructor_model import InstructorModel
from rest_framework import serializers


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorModel
        fields = [
            'id',
            'user',
            'address',
            'identification',
            'cell_phone',
        ]
        read_only_fields = (
            'id',
            'user',
        )
