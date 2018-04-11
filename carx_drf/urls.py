from django.conf.urls import url, include
import rest_auth.urls
from django.conf.urls.static import static
import carx_drf.urls
import carx_web.urls
import rest_framework.urls
from carx_drf.models import Customer

from rest_framework import routers, serializers, viewsets
from carx_drf import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
# router.register(r'customer/login/', views.HelloWorldView.as_view(), base_name='HelloWorldView')


urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'user/login/', views.LoginView.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='api-docs', description='RESTful API for CarX'), name='api-docs'),

]