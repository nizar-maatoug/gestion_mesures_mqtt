from django.urls import path
from website.views import detailGrandeur,listGrandeur


urlpatterns=[
    path('<int:id>', detailGrandeur, name="detailGrandeur"),
    path('', listGrandeur)
]