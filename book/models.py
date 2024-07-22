from django.db import models
from rest_framework.exceptions import ValidationError

from account.models import CustomUser


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)

    class Meta:
        unique_together = ('title', 'author', 'genre')

    def __str__(self):
        return f"{self.title} by {self.author} - {self.genre}"


def validate_rating(value):
    if value < 1:
        raise ValidationError(
            'Rating must be at least 1.'
        )
    elif value > 5:
        raise ValidationError(
            'Rating must be at most 5.'
        )


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[validate_rating]
    )

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f'{self.user} - {self.book} - {self.rating}'
