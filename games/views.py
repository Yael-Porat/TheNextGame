from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Game
from .forms import AdvancedSearchForm


def homepage(request):
    games = None
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        if query:
            games = Game.objects.filter(
                Q(games__name__icontains=query)
            ).distinct()
    if not games:
        games = Game.objects.all()
    print(games)
    return render(request, 'homepage.html', {'games': games})


class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'


def search_games(request):
    form = AdvancedSearchForm(request.POST or None)  # Allow POST data

    games = Game.objects.all()

    if request.method == 'POST' and form.is_valid():
        # Apply filters based on form inputs
        query = form.cleaned_data.get('query')
        if query:
            games = games.filter(title__icontains=query) | games.filter(description__icontains=query)

        min_price = form.cleaned_data.get('min_price')
        if min_price:
            games = games.filter(price__gte=min_price)

        max_price = form.cleaned_data.get('max_price')
        if max_price:
            games = games.filter(price__lte=max_price)

        min_rating = form.cleaned_data.get('min_rating')
        if min_rating:
            games = games.filter(rating__gte=min_rating)

        max_rating = form.cleaned_data.get('max_rating')
        if max_rating:
            games = games.filter(rating__lte=max_rating)

        category = form.cleaned_data.get('category')
        if category:
            games = games.filter(category=category)

        min_players = form.cleaned_data.get('min_players')
        if min_players:
            games = games.filter(min_players__gte=min_players)

        max_players = form.cleaned_data.get('max_players')
        if max_players:
            games = games.filter(max_players__lte=max_players)

        min_duration = form.cleaned_data.get('min_duration')
        if min_duration:
            games = games.filter(duration__gte=min_duration)

        max_duration = form.cleaned_data.get('max_duration')
        if max_duration:
            games = games.filter(duration__lte=max_duration)

    return render(request, 'homepage.html', {'form': form, 'games': games})


from django.shortcuts import render, get_object_or_404
from .models import Category


def category_view(request, category_name):
    # Get the category by name (or you can use another identifier if needed)
    category = get_object_or_404(Category, name=category_name)

    # Render the category page, passing the category and related games
    return render(request, 'category.html', {
        'category': category
    })
