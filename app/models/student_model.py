from django.db import models
from app.models.user_model import UserModel
from app.models.course_model import CourseModel


class StudentModel(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    address = models.CharField(
        'Dirección',
        max_length=100,
        null=False,
        blank=False,
    )
    identification = models.IntegerField(
        'Cédula',
        unique=True,
        null=False,
        blank=False,
    )
    cell_phone = models.IntegerField(
        'Celular',
        null=False,
        blank=False,
    )
    guardians_name = models.CharField(
        'Nombre del Acudiente',
        max_length=100,
        null=False,
        blank=False,
    )
    guardians_phone = models.IntegerField(
        'Celular del Acudiente',
        null=False,
        blank=False,
    )
    courses = models.ManyToManyField(
        CourseModel,
        related_name='students',
    )

    class Meta:
        db_table = 'student'

    def to_json(self, *args, **kwargs):
        return {
            "id": self.id,
            "user": {
                    "id": self.user.id,
                    "username": self.user.username,
                    "email": self.user.email,
                    "name": self.user.name,
                    "last_name": self.user.last_name,
                    "is_instructor": self.user.is_instructor,
                },
            "address": self.address,
            "identification": self.identification,
            "cell_phone": self.cell_phone,
            "guardians_name": self.guardians_name,
            "guardians_phone": self.guardians_phone,
        }
