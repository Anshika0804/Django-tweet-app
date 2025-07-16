from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TweetViewSet
from rest_framework.authtoken.views import obtain_auth_token 
from tweet import views as tweet_views


router = DefaultRouter()
router.register(r'tweets', TweetViewSet, basename='tweet')
urlpatterns = [
    path("", views.tweet_list, name='tweet_list'),
    path('tweet/', tweet_views.tweet_list, name='tweet_list_alias'),
    path("create/", views.tweet_create, name='tweet_create'),
    path("<int:tweet_id>/edit/", views.tweet_edit, name='tweet_edit'),
    path("<int:tweet_id>/delete/", views.tweet_delete, name='tweet_delete'),
    path("register/", views.register, name='register'),
    path('my-tweets/', views.my_tweets, name='my_tweets'), 

    # API Routes
    path('api/', include(router.urls)),                        
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
