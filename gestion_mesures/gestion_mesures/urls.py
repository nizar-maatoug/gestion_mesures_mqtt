
from django.contrib import admin
from django.urls import path

from website.views import welcome,date, detailGrandeur

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome),
    path('date',date),
    path('grandeurs/<int:id>',detailGrandeur)
]
