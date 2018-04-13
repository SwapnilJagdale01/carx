from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^home/', views.Home),
    url(r'^', views.Login,name="login"),
    url(r'^logout/', views.Logout,name="logout"),
]