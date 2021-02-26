from django.contrib import admin
from django.urls import path
from blood import views as v

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', v.home, name='home'),
    path('map/', v.map, name='map'),
    path('profile/', v.profile, name='profile')
]
