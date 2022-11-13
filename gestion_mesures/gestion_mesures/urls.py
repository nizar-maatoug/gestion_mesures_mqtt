
from django.contrib import admin
from django.urls import path

from website.views import welcome,date

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome.html',welcome),
    path('date',date)
]
