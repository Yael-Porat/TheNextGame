from django.urls import path

from .views import homepage, GameDetailView, category_view

urlpatterns = [
    path('', homepage, name='homepage'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('category/<str:category>/', category_view, name='category'),

]
