from django.urls import path

from . import views

# (Mashutin, 2024; Writing Your First Django App, Part 1, n.d.)
urlpatterns = [
    path("", views.showLink, name = 'index'),
]