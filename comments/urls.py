from django.urls import path
from .views import add_comment, edit_comment, delete_comment, comment_list

urlpatterns = [
    path('add/<int:tweet_id>/', add_comment, name='add_comment'),
    path('<int:tweet_id>/comments/', comment_list, name='comment_list'),
    path('edit/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]
