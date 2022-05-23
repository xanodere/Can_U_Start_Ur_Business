from django.urls import path

from .views import home, results


urlpatterns = [
    path("", home, name="home"),
    path("results/", results, name="results")
]