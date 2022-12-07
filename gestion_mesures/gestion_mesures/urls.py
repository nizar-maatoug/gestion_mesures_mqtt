
from django.contrib import admin
from django.urls import path,include

from website.views import welcome,date

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome),
    path('date',date),
    path('',include('website.urls')),
    path('api/',include('webapi.urls')),
    path('dashboard/',include('dashboardapp.urls')),
]
