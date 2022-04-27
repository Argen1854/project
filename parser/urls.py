from django.urls import path
from . import views

urlpatterns = [
    path('parser/', views.ParserFormView.as_view())
]