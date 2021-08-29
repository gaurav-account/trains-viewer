from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:station_code>', views.departures, name='departures'),
    path('v1/api/', views.indexapi, name='indexapi'),
    path('v1/api/<str:station_code>', views.departuresapi, name='departuresapi'),
]
