from django.contrib import admin
from django.urls import path, include

from book.views import BookListView, BookListGenreView

urlpatterns = [
    path('/api/book/list/', BookListView.as_view(), name='Book list'),
    path('api/books/', BookListGenreView.as_view(), name='book-list-genre'),

]