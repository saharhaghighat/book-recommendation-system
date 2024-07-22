from rest_framework import serializers
from .models import Review, Book


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'book', 'user', 'rating')


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Optional: Include reviews in book serialization

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'reviews','genre')  # Include reviews if desired
