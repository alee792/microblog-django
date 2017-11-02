from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# Create your views here.
def index(request): 
    posts = Post.objects.all()

    return render(request, 'index.html', {
        'posts': posts,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

# @login_required
# def edit_post(request, pk):
#     post = Post.objects.get(pk=pk)

#     if post.user != request.user:
#         raise Http404

#     form_class = PostForm
    
#     if request.method == 'POST':
#         form = form_class(data=request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = form_class(instance=post)
    
#     return render(request, 'edit_post.html', {
#         'post': post,
#         'form': form,
# })

class PostUpdateView(LoginRequiredMixin, UpdateView):
    # fields = ('content',)
    form_class = PostForm
    model = Post
    template_name = "post_update.html"

# def create_post(request):
#     form_class = PostForm
#     if request.method == 'POST':
#         form = form_class(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)

#             post.user = request.user
            
#             post.save()

#             return redirect('post_detail', pk=post.pk)

#     else:
#         form = form_class()
    
#     return render(request, 'create_post.html', {
#         'form': form,
#     })

class PostCreateView(LoginRequiredMixin, CreateView, ListView): 
    context_object_name = "posts"
    # fields = ('content',)
    model = Post
    template_name = "post_create.html"
    success_url="/"
    paginate_by = 10
    form_class = PostForm

    # Associate post with user
    def form_valid(self, form):
         user = self.request.user
         form.instance.user = user
         return super(PostCreateView, self).form_valid(form)

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url='/'
    template_name = "post_delete.html"