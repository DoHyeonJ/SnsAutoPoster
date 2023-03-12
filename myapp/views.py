from django.shortcuts import render
from .models import Post

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
    else:
        post = None
    return render(request, 'index.html', {'post': post})