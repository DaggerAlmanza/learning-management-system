from app.models.user_model import UserModel
from django.db import models


class InstructorModel(models.Model):
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

    class Meta:
        db_table = 'instructor'

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
        }
