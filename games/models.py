from django.db import models
from users.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200, default="")
    description = models.TextField()

    mechanics = models.TextField(blank=True, null=True)  # For storing mechanics, could be a text list
    categories = models.ManyToManyField(Category, related_name="games")  # Categories are linked to your existing Category model

    # Year published
    year_published = models.IntegerField(blank=True, null=True)  # Match yearPublished

    rating = models.FloatField(blank=True, null=True)  # Match rating

    # Publisher and type
    publisher = models.CharField(max_length=200, blank=True, null=True)  # Match publisher
    game_type = models.CharField(max_length=100, blank=True, null=True)  # Match type (boardgame or expansion)

    # Player info
    max_players = models.IntegerField(blank=True, null=True)  # Match maxPlayers
    min_players = models.IntegerField(blank=True, null=True)  # Match minPlayers
    min_play_time = models.IntegerField(blank=True, null=True)  # Match minPlayTime
    max_play_time = models.IntegerField(blank=True, null=True)  # Match maxPlayTime

    # Created and Updated timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserProfile, related_name="games_created", on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(UserProfile, related_name="games_updated", on_delete=models.SET_NULL, null=True, blank=True)
    purchase_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    def main_image(self):
        return self.images.filter(is_main_image=True).first()

    def all_images(self):
        return self.images.all()


class GameImage(models.Model):
    game = models.ForeignKey(Game, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="games/images/")
    is_main_image = models.BooleanField(default=False)  # To mark the main image for the game
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Optional alt text for the image

    def __str__(self):
        return f"Image for {self.game.name}"
