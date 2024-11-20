# from django.db import models
from tastypie.resources import ModelResource
from users.models import User, Files
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        allowed_methods = ['get']


class FilesResource(ModelResource):
    class Meta:
        queryset = Files.objects.all()
        resource_name = 'files'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    # Для POST запроса создания файла нужно добавить id пользователя, к которому данный файл будет привязан,
    # но в модели Files нет поля user_id, чтобы обойти данную проблему нужно использовать следующие методы
    # hydrate - записываем в б.д. информацию полученную от пользователя (POST-запрос)
    # dehydrate - добавляет в JSON файл при выводе id пользователя к которому привязан конкретный файл (GET-запрос)

    def hydrate(self, bundle):
        bundle.obj.user_id = bundle.data['user_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['user'] = bundle.obj.user
        bundle.data['user_id'] = bundle.obj.user.id
        return bundle
