
from django.contrib import admin
from django.urls import path,include

from website.views import welcome,date, detailGrandeur,listGrandeur

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome),
    path('date',date),
    path('',include('website.urls')),
]
