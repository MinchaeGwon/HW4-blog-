from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .form import BlogPost

def home(request): #read
    blogs = Blog.objects #.all(), .count(), .first(), .last()
    cnt = Blog.objects.count()
    return render(request, 'home.html', {'blogs': blogs, 'count': cnt})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    blogImg = Blog.objects

    return render(request, 'detail.html', {'blog':blog_detail, 'images': blogImg})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #create
    # 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def update(request, pk):
    #어떤 블로그를 수정할지 블로그 객체를 갖고 오기
    blog = get_object_or_404(Blog, pk=pk)
    
    #해당하는 블로그 객체 pk에 맞는 입력공간을 가져옴
    form = BlogPost(request.POST, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')
