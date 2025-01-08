from django.urls import path

from .views import homepage, GameDetailView, game_details, category_view, CategoryList, GameList, CategoryDetail, GameDetail, addGamesAPI

urlpatterns = [
    path('', homepage, name='homepage'),
    path('game/<int:pk>/', game_details, name='game_details'),
    path('category/<str:category_name>/', category_view, name='category'),
    path('api/categories/', CategoryList.as_view(), name='category-list'),
    path('api/categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('api/games/', GameList.as_view(), name='game-list'),
    path('api/games/<int:pk>/', GameDetail.as_view(), name='game-detail'),
    path('addGamesAPI/<str:name>', addGamesAPI, name='addGamesAPI'),
]
