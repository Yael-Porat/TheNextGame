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
    category = models.ForeignKey(Category, related_name="games", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserProfile, related_name="games_created", on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(UserProfile, related_name="games_updated", on_delete=models.SET_NULL, null=True, blank=True)
    recommended_age = models.CharField(max_length=50, blank=True, null=True)
    price_range = models.CharField(max_length=50, blank=True, null=True)
    purchase_url = models.URLField(max_length=500, blank=True, null=True)
    number_of_players = models.CharField(max_length=50, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def main_image(self):
        """Returns the main image for the game"""
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
