from django.urls import path
from . import views

urlpatterns = [
    path('', views.init, name='index'),
    path('nosotros', views.about, name='nosotros'),
]
