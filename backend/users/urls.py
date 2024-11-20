from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:files_id>', views.single_file, name='single_file')
]
