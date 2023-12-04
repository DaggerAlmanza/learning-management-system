from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(
        self,
        username,
        email,
        name,
        last_name,
        password,
        is_staff,
        is_superuser,
        **extra_fields
    ):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(
        self,
        username,
        email,
        name,
        last_name,
        password=None,
        **extra_fields
    ):
        return self._create_user(
            username,
            email,
            name,
            last_name,
            password,
            False,
            False,
            **extra_fields
        )

    def create_superuser(
        self,
        username,
        email,
        name,
        last_name,
        password=None,
        **extra_fields
    ):
        return self._create_user(
            username,
            email,
            name,
            last_name,
            password,
            True,
            True,
            **extra_fields
        )


class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(
        primary_key=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    username = models.CharField(
        max_length=40,
        unique=True
    )
    email = models.EmailField(
        'Correo Electrónico',
        max_length=40,
        unique=True,
    )
    name = models.CharField(
        'Nombres',
        max_length=40,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=40,
        blank=True,
        null=True
    )
    is_instructor = models.BooleanField(
        '¿Profesor?',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'name',
        'last_name',
        'is_instructor',
    ]

    class Meta:
        db_table = 'user'

    def to_json(self, *args, **kwargs):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            'is_instructor': self.is_instructor,
        }
