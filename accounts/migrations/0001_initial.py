# Generated by Django 4.0.4 on 2022-04-20 15:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=80, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_login', models.DateField(auto_now=True, verbose_name='Последняя авторизация')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pics/',
                                            validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])],
                                            verbose_name='Фото')),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
