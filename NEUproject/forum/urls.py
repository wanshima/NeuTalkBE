from django.urls import path
from . import views

urlpatterns = [
    # List all threads
    path('', views.ThreadListView.as_view(), name='thread_list'),

    # View a specific thread and its posts
    path('thread/<int:pk>/', views.ThreadDetailView.as_view(), name='thread_detail'),

    # Create a new post in a thread
    path('thread/create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('thread/create/', views.CreateThreadView.as_view(), name='create_thread'),
    path('thread/<int:pk>/', views.ThreadDetailView.as_view(), name='thread_detail')
]