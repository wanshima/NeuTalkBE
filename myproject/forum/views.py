from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Thread, Post

class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'  # Create this template
    context_object_name = 'threads'  

class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'  # Create this template
    context_object_name = 'thread'

class CreatePostView(CreateView):
    model = Post
    fields = ['content']
    template_name = 'forum/create_post.html'

@login_required
def create_post(request, thread_id):
    thread = Thread.objects.get(pk=thread_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post(thread=thread, content=content, author=request.user)
        post.save()
        return redirect('thread_detail', pk=thread_id)
    return render(request, 'forum/create_post.html', {'thread': thread})

# from django.views.generic.edit import CreateView
# from .models import Thread
# from django.urls import reverse_lazy

# class CreateThreadView(CreateView):
#     model = Thread
#     fields = ['title']
#     fields = ['content']
#     success_url = reverse_lazy('thread_list')
#     template_name = 'forum/create_thread.html'

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Thread
from .forms import ThreadForm

class CreateThreadView(CreateView):
    model = Thread
    form_class = ThreadForm  # Use the custom form
    success_url = reverse_lazy('thread_list')
    template_name = 'forum/create_thread.html'