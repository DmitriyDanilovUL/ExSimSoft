from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('health/', views.health),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path("", include("django_prometheus.urls"), name="django-prometheus")
    
]
