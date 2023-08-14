from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name='home'),
    path('sendSMS', views.sendSMS, name='sendSMS'),
    path('net', views.net, name='net')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)