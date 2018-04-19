from django.conf.urls import url, include
from . import views

app_name = 'carx_web'

urlpatterns = [
    # url(r'^dashboard', views.Home, name='dashboard'),
    url(r'^create/vehicle', views.create_vehicle, name='createVehicle'),
    url(r'^save/vehicle', views.save_vehicle, name='save_vehicle'),
    url(r'^model/list', views.model_list, name='model_list'),
    url(r'^edit/vehicle/(?P<pk>\d+)/$', views.update_vehicle, name='update_vehicle'),
    url(r'^delete/vehicle/(?P<pk>\d+)/$', views.delete_vehicle, name='delete_vehicle'),
    url(r'^update/vehicle/(?P<pk>\d+)/$', views.update_vehicle_save, name='update_vehicle_save'),
    url(r'^vehicle/list', views.vehicle_list, name='vehicle_list'),
    url(r'^category_list/', views.CategoryList, name="category_list"),
    url(r'^save_category/', views.SaveCategory, name="save_category"),
    url(r'^category_view/(?P<category_id>\d+)', views.ViewCategory, name="category_view"),
    url(r'^category_update/(?P<category_id>\d+)', views.UpdateCategory, name="category_update"),
    url(r'^category_delete/(?P<category_id>\d+)', views.CategoryDelete, name="category_delete"),
    url(r'^save_maker/', views.Maker, name="save_maker"),
    url(r'^logout/', views.Logout, name="logout"),
    url(r'^tyre_list/', views.TyreList, name="tyre_list"),
    url(r'^add_tyre/', views.AddTyre, name="add_tyre"),
    url(r'^save_tyre/', views.SaveTyre, name="save_tyre"),
    url(r'^tyre_delete/(?P<tyre_id>\d+)', views.DeleteTyre, name="tyre_delete"),
    url(r'^tyre_view/(?P<tyre_id>\d+)', views.ViewTyre, name="tyre_view"),
    url(r'^tyre_update/(?P<tyre_id>\d+)', views.UpdateTyre, name="tyre_update"),
    url(r'^tyre_import/', views.TyreImport, name="tyre_import"),
    url(r'^tyre_import_data/', views.TyreImportData, name="tyre_import_data"),
    url(r'^tyre_import_format/', views.TyreImportExcelFormat, name="tyre_import_format"),
    url(r'^home/', views.Home,name='home'),
    url(r'', views.Login,name="login"),

]
