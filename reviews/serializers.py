# reviews/serializers.py
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Display username
    game = serializers.StringRelatedField(read_only=True)  # Display game name

    class Meta:
        model = Review
        fields = ['id', 'user', 'game', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'game', 'created_at']
