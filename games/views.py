from django.views.generic import DetailView
from .models import Game
from django.shortcuts import render, get_object_or_404
from .models import Category

def homepage(request):
    games = Game.objects.all()
    print(games)
    return render(request, 'games_gallery.html', {'games': games, 'category': None})


class GameDetailView(DetailView):
    model = Game
    template_name = 'game_details.html'
    context_object_name = 'game'

def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    games = Game.objects.filter(categories=category)
    print(games)

    return render(request, 'games_gallery.html', {
        'category': category,
        'games': games
    })