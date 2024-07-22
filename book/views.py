from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Review, Book
from .serializer import ReviewSerializer, BookSerializer


class BookListView(generics.ListAPIView):
    pass


class BookListGenreView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Book.objects.all()
        genre = self.request.query_params.get('genre', None)
        if genre:
            queryset = queryset.filter(genre=genre)
        return queryset
