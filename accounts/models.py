from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import FileExtensionValidator
from django.db import models


class Profile(AbstractBaseUser):
    email = models.EmailField('Email', max_length=80, unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField('Дата создания', auto_now_add=True)
    last_login = models.DateField('Последняя авторизация', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image = models.ImageField(
        'Фото',
        null=True,
        upload_to='pics/',
        blank=True,
        validators=[
            FileExtensionValidator(['jpg', 'png'])
        ]
    )
    hide_email = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
