from django.conf.urls import url, include
from . import views

app_name = 'carx_web'

urlpatterns = [
    url(r'^home/', views.dashboard, name='dashboard'),
    url(r'^create/vehicle', views.create_vehicle, name='createVehicle'),
    url(r'^carx/login/', views.login, name="login"),
    url(r'^logout/', views.logout,name="logout"),
]