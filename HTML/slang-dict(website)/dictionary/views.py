from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Baslik
from .forms import PostForm

# Create your views here.

def kelime_listesi(request):
	basliklar = Baslik.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'dictionary/kelime_listesi.html', {'basliklar': basliklar})

def kelime_detail(request, pk):
    basliklar = get_object_or_404(Baslik, pk=pk)
    return render(request, 'dictionary/kelime_detail.html', {'basliklar': basliklar})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('kelime_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'dictionary/kelime_editle.html', {'form': form})

def kelime_editle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auth = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('kelime_editle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'dictionary/kelime_editle.html', {'form': form})
