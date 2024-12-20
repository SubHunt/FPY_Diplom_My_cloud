# Generated by Django 5.1.2 on 2024-11-20 12:22

import django.db.models.deletion
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('email', models.EmailField(max_length=50, verbose_name='Е-майл')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор?')),
                ('path_to_user', models.CharField(max_length=50, verbose_name='Путь к файлам пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Название файла')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('date_last_load', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата последнего обновления')),
                ('link_download', models.URLField(blank=True, max_length=50, unique=True, verbose_name='Прямая ссылка')),
                ('path', models.FileField(upload_to=users.models.path_to_file, verbose_name='Путь к файлу')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Владелец файла')),
            ],
        ),
    ]
