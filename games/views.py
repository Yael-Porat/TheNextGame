import requests
from django.http import JsonResponse
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics, permissions
from .serializers import GameSerializer, CategorySerializer, GameImageSerializer
from .models import GameImage, Game, Category
from reviews.forms import ReviewForm
from rest_framework import viewsets
from .models import GameImage
from .serializers import GameImageSerializer

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


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GameImageList(generics.ListCreateAPIView):
    queryset = GameImage.objects.all()
    serializer_class = GameImageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

def game_details(request, pk):
    game = get_object_or_404(Game, id=pk)
    reviews = game.reviews.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.game = game
            review.save()
            return redirect('game_details', pk=game.pk)
    else:
        form = ReviewForm()

    return render(request, 'game_details.html', {
        'game': game,
        'reviews': reviews,
        'form': form,
    })


class GameImageViewSet(viewsets.ModelViewSet):
    queryset = GameImage.objects.all()
    serializer_class = GameImageSerializer



def addGamesAPI(request, name):
    url = "https://meepleit.p.rapidapi.com/meepleit-search"

    querystring = {"search": name, "limit": "100"}

    headers = {
        "x-rapidapi-key": "948e4e7cd0mshc8581de36eecddcp1e7d5fjsna423c2e1db5e",
        "x-rapidapi-host": "meepleit.p.rapidapi.com"
    }

    try:
        # Make the request
        response = requests.get(url, headers=headers, params=querystring)

        # Check for a successful response
        if response.status_code == 200:
            print(response.json())
            return JsonResponse(response.json())  # Return the JSON response directly to the client
        else:
            # Handle unsuccessful responses
            return JsonResponse({"error": f"Failed to fetch data. Status code: {response.status_code}"})

    except requests.exceptions.RequestException as e:
        # Catch any exceptions related to the request
        return JsonResponse({"error": f"An error occurred while processing the request: {e}"})
