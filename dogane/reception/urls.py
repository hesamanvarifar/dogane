from django.urls import path
from .views import Reception, UpdateReception

urlpatterns = [
    path('create_car/', Reception.as_view(),name='create-car'),
    path('update-car/', UpdateReception.as_view(),name='update-car'),
]
