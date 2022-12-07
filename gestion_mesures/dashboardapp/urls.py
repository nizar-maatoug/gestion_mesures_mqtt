from django.urls import path

from dashboardapp.views import dashboard

urlpatterns = [
    path('', dashboard, name="dashboard"),
]