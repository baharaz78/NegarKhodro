from django.urls import path
from animals.views import AnimalView

urlpatterns = [
    path("", AnimalView.as_view(), name="animals")
]
