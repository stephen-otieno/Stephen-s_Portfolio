from . import views
from django.urls import path
from portfolio import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homepage'),
    path('contacts/', views.contacts, name='contacts'),
]