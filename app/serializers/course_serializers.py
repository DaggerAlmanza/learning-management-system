from app.models.course_model import CourseModel
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = [
            'id',
            'name',
            'description',
        ]
        read_only_fields = (
            'id',
            'instructor',
        )
