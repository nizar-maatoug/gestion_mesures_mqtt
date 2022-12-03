from django.urls import path
from .views import add_list_grandeur,get_modif_delete_grandeur


urlpatterns=[
    path('grandeurs', add_list_grandeur, name="list_post_api_grandeurs"),
    path('grandeurs/<int:pk>',get_modif_delete_grandeur,name="get_put_delete_api_grandeurs")

]