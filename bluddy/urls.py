from . import settings
from django.contrib import admin
from django.urls import path, include
from blood import views as v
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('django.contrib.auth.urls')),
    path('register/', v.register, name='register'),
    path('', v.home, name='home'),
    path('campaign/', v.campaign, name='campaign'),
    path('campaign/new/', v.campaign_new, name='new_campaign'),
    path('map/', v.map, name='map'),
    path('profile/', v.profile, name='profile'),
    path('rewards/', v.rewards, name='rewards'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
