
from django.contrib import admin
from django.urls import path

from website.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome.html',welcome),
]
