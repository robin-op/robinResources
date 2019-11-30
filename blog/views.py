from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import Post
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .forms import PostForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages




# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('')
    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html',{'form':form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/blog/login/")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})




def main(request):
    return render(request, 'blog/Index.html')
def listaPersonajes (request):
    return render(request, 'blog/ListaPersonajes.html')
def tierlist (request):
        return render(request, 'blog/tiers.html')

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
       