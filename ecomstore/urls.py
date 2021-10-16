from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
]
