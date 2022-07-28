from urllib.parse import urlparse
from django.urls import URLPattern, path
from django.views import View
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
]