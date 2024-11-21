from django.urls import path, include
from api.models import UserResource, FilesResource
from tastypie.api import Api

api = Api(api_name='v1')  # Добавляем версию api
user_resource = UserResource()
files_resource = FilesResource()
api.register(user_resource)
api.register(files_resource)


# api/v1/files/  GET, POST
# api/v1/files/1 GET, DELETE
# api/v1/users/  GET
# api/v1/users/1 GET

# Для POST, DELETE нужно добавить header
# Key: Authorization
# Value: ApiKey admin:apikeyforpostrequests

urlpatterns = [
    path('', include(api.urls), name='index')
]
