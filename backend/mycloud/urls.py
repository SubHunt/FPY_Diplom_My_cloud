"""
URL configuration for mycloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import index
from api.models import UserResource, FilesResource
from tastypie.api import Api

api = Api(api_name='v1')  # Добавляем версию api
user_resource = UserResource()
files_resource = FilesResource()
api.register(user_resource)
api.register(files_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    # path('api/', include(user_resource.urls)),
    path('api/', include(api.urls))
]

# handler404 = "users.views.error_view"
