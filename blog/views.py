from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


# Create your views here.
def main(request):
    return render(request, 'blog/Index.html')
def listaPersonajes (request):
    return render(request, 'blog/ListaPersonajes.html')
def signup (request):
    return render(request, 'blog/signup.html')

def post_list(request):
    user = request.user
    if user.has_perm('blog.profesor'):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'blog/post_list.html', {'posts': posts })
    else:
        return render(request, 'blog/home.html')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

class personajesView(generic.ListView):
        template_name='blog/ListaPersonajes.html'
       