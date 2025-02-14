from django.urls import path
from app.views import index, login, computer, register, software


urlpatterns = [
    path('', index, name='index'),
    path('rede_social/', login, name='login'),
    path('aprendizado_de_tecnologia/', computer, name='computer'),
    path('register/', register, name='register'),
    path('software/', software, name='software')
]