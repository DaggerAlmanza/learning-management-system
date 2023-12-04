from app.models.instructor_model import InstructorModel
from django.db import models


class CourseModel(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
    )
    description = models.CharField(
        'Descripción del curso',
        max_length=200,
        null=False,
        blank=False,
    )
    instructor = models.ForeignKey(
        InstructorModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='courses'
    )

    class Meta:
        db_table = 'course'

    def to_json(self, *args, **kwargs):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "instructor": {
                    "id": self.instructor.id,
                    "user": {
                        "id": self.instructor.user.id,
                        "created_at": self.instructor.user.created_at,
                        "username": self.instructor.user.username,
                        "email": self.instructor.user.email,
                        "name": self.instructor.user.name,
                        "last_name": self.instructor.user.last_name,
                        'is_instructor': self.instructor.user.is_instructor,
                    },
                    "address": self.instructor.address,
                    "identification": self.instructor.identification,
                    "cell_phone": self.instructor.cell_phone,
                }
        }
