from django.urls import path
from website.views import detailGrandeur,listGrandeur,newGrandeur,detailMesure,listMesure,newMesure


urlpatterns=[
    path('grandeurs/<int:id>', detailGrandeur, name="detailGrandeur"),
    path('grandeurs', listGrandeur,name="grandeurs"),
    path('grandeurs/new',newGrandeur,name="newGrandeur"),

    path('mesures/<int:id>', detailMesure, name="detailMesure"),
    path('mesures/<int:grandeur_id>', listMesure,name="mesures"),
    path('mesures/new',newMesure,name="newMesure")

]