from . import views
from django.urls import path
from portfolio import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homepage'),
    path('contact/', views.contacts, name='contacts'),
    path('contacts/', views.view_contacts, name='clients'),

    path('login/', views.login_page, name='login'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)