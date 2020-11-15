from django.urls import path
from .views import WorkersView, CompanyView


app_name = "workers"

urlpatterns = [
    path('workers/', WorkersView.as_view()),
    path('company/', CompanyView.as_view()),

]