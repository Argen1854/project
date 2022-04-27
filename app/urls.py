from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('detail/<int:id>/', views.DetailView.as_view())
]