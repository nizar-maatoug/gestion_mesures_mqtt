from django.urls import path
from .views import add_list_grandeur


urlpatterns=[
    path('grandeurs', add_list_grandeur, name="api_grandeurs"),

]