from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('post/<str:slug>/', PostPage.as_view(), name='post'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
]