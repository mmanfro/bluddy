from django.contrib import admin
from django.urls import path, include
from blood import views as v

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('auth/', include('django.contrib.auth.urls')),
    path('', v.home, name='home'),
    path('map/', v.map, name='map'),
    path('profile/', v.profile, name='profile'),
    path('rewards/', v.rewards, name='rewards'),
]
