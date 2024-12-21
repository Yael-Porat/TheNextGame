from django.urls import path

from .views import homepage, GameDetailView, category_view

urlpatterns = [
    path('', homepage, name='homepage'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_details'),
    path('category/<str:category_name>/', category_view, name='category'),
]
