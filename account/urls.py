from django.contrib import admin
from django.urls import path, include

from account.views import LoginView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),

]
