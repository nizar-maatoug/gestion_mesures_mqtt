from django.urls import path
from website.views import detailGrandeur,listGrandeur,newGrandeur


urlpatterns=[
    path('/<int:id>', detailGrandeur, name="detailGrandeur"),
    path('', listGrandeur,name="grandeurs"),
    path('/new',newGrandeur,name="newGrandeur")
]