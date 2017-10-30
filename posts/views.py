from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostForm

# Create your views here.
def index(request): 
    posts = Post.objects.all()

    return render(request, 'index.html', {
        'posts': posts,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    form_class = PostForm
    
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = form_class(instance=post)
    
    return render(request, 'edit_post.html', {
        'post': post,
        'form': form,
})