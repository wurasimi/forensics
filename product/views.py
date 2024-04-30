from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import ContactForm, PostForm
from  django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts':posts
    }
    return render(request,'product/product.html',context)
def about(request):
    return render(request,'product/about.html')
def services(request):
    return render(request,'product/services.html')
def ai(request):
    return render(request,'product/ai.html')
def item(request):
   posts = Post.objects.all().order_by('-id')
   post_count = Post.objects.all().count()
   paginator = Paginator(posts , 3)
   page = request.GET.get('page')
   paged_post = paginator.get_page(page)
    
   context = {
        'posts':paged_post,
        'post_count': post_count
    }
   return render(request,'product/item.html', context)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('product-item')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
        
    return render(request, 'product/contact.html', context)
def search(request):
    posts = Post.objects.all().order_by('-id')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
             posts = posts.filter(title__icontains=keyword)
    context = {
        'posts':posts,
    }
    return render(request, 'product/search.html',context)