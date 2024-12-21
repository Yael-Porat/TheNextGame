from django.db import models

# A model to store categories of board games (e.g., strategy, family, card games, etc.)
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# A model to store board game information
class Game(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="games", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def main_image(self):
        """Returns the main image for the game"""
        return self.images.filter(is_main_image=True).first()


# A model to store images related to a board game
class GameImage(models.Model):
    game = models.ForeignKey(Game, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="games/images/")
    is_main_image = models.BooleanField(default=False)  # To mark the main image for the game
    alt_text = models.CharField(max_length=255, blank=True, null=True)  # Optional alt text for the image

    def __str__(self):
        return f"Image for {self.game.name}"

