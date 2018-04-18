from django.conf.urls import url, include
from . import views

app_name = 'carx_web'

urlpatterns = [
    url(r'^home/', views.dashboard, name='dashboard'),
    url(r'^create/vehicle', views.create_vehicle, name='createVehicle'),
    url(r'^save/vehicle', views.save_vehicle, name='save_vehicle'),
    url(r'^model/list', views.model_list, name='model_list'),
    url(r'^edit/vehicle/(?P<pk>\d+)/$', views.update_vehicle, name='update_vehicle'),
    url(r'^delete/vehicle/(?P<pk>\d+)/$', views.delete_vehicle, name='delete_vehicle'),
    url(r'^update/vehicle/(?P<pk>\d+)/$', views.update_vehicle_save, name='update_vehicle_save'),
    url(r'^vehicle/list', views.vehicle_list, name='vehicle_list'),
    url(r'^', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
]