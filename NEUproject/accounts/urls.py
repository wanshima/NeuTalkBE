from django.urls import path
from .views import register_user, user_login, user_logout, create_post, get_post_detail, thread_list

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('new/', create_post, name='new_post'),
    path('posts/<uuid:post_id>/', get_post_detail, name='post_detail'),
    path('threads/', thread_list, name='thread_list'),
]
