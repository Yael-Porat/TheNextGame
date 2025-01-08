from rest_framework import serializers
from .models import Game, Category, GameImage
from reviews.serializers import ReviewSerializer
from users.models import UserProfile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['url','id', 'name','description']  # Include whatever fields you need from Category model


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')  # Get 'username' from the related 'User' model

    class Meta:
        model = UserProfile
        fields = ['url', 'id', 'username', 'role']

class GameImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameImage
        fields = ['url','image', 'is_main_image', 'alt_text']  # You can add more fields if necessary

class GameSerializer(serializers.ModelSerializer):

   # main_image = serializers.SerializerMethodField()  # Custom field for the main image
   # all_images = GameImageSerializer(many=True)  # Serialize all images associated with the game

    categories = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='category-detail',  # View name for related resources
        queryset=Category.objects.all()
    )

    reviews = ReviewSerializer(many=True, read_only=True)  # Nested reviews

    class Meta:
        model = Game
        fields = [
            'url', 'id', 'name', 'short_description', 'description', 'categories',
            'created_at', 'updated_at', 'created_by', 'updated_by',
            'recommended_age', 'price_range', 'purchase_url', 'number_of_players',
            'reviews'  # 'main_image', 'all_images'
        ]

    def get_main_image(self, obj):
        # Retrieve the main image for the game if available
        main_image = obj.main_image()
        if main_image:
            return {
                'image': main_image.image.url,  # Assuming 'image' is the field in GameImage model
                'alt_text': main_image.alt_text
            }
        return None
