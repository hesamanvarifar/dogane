from django.urls import path
from . views import CarList, CarDetail, PartList

urlpatterns = [
    path('car_list/', CarList.as_view(),name='car-list'),
    path('car_detail/', CarDetail.as_view(),name='car-detail'),
    path('part_list/', PartList.as_view(),name='part-list'),

]
