from django.contrib import admin

from book.models import Book, Review


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating')
    search_fields = ('book__title', 'user__username')
    list_filter = ('rating',)


admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
