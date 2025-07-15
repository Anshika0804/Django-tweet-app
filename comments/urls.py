from django.urls import path
from .views import add_comment

urlpatterns = [
    path('add/<int:tweet_id>/', add_comment, name='add_comment'),
]
