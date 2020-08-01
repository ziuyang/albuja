from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog, QnA, Post
from .forms import PostForm
from django.core.paginator import Paginator


def home(request):
    
    blogs = Post.objects
    blog_list = Post.objects.all()
    blog3 = Paginator(blog_list, 3)
    page = request.GET.get('page')
    blogposts = blog3.get_page(page)

    qna=QnA.objects
    questions = QnA.objects.all()
    questions3 = Paginator(questions,3)
    page = request.GET.get('page')
    qnaposts = questions3.get_page(page)
    return render(request,'home.html',{'blogs':blogposts, 'qna':qnaposts})

# Create your views here.
# def home2(request):
#     return render(request,'home.html',{})

def search(request):
    blogs = Blog.objects.all().order_by('-id')
    q = request.POST.get('q', "") 

    if q:
        blogs = blogs.filter(title__icontains=q)
        return render(request, 'search.html', {'blogs' : blogs, 'q' : q})
    
    else:
        return render(request, 'search.html')

def qnaListView(request):
    questions = QnA.objects.all()
    questions3 = Paginator(questions,3)
    return render(request, 'qnaList.html', {'questions':questions} )

def qnaDetailView(request, questions_id):
    questions_detail = get_object_or_404(QnA, pk=questions_id)
    return render(request, 'qnaDetail.html', {'questions_detail':questions_detail})

def qnaNewView(request):
    return render(request, 'qnaNew.html')

def qnaCreateView(request):
    questions = QnA()
    questions.title = request.POST.get('title')
    questions.body = request.POST.get('body')
    questions.pub_date = timezone.datetime.now()
    questions.save()
    return redirect('/questions/' + str(questions.id))

def qnaUpdateView(request, questions_id):
    questions = get_object_or_404(QnA, pk=questions_id)

    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        questions.title = title
        questions.body = body
        questions.pub_date = timezone.datetime.now()
        questions.save()
        return redirect('qnaDetail', questions.id)
    
    return render(request, 'qnaEdit.html', {'questions':questions})

def qnaDeleteView(request, questions_id):
    questions_delete = get_object_or_404(QnA, pk=questions_id)
    questions_delete.delete()
    return redirect('qnaList')


## review Post 기능
def reviewPosts(request):
    posts = Post.objects.all()
    return render(request, 'review_posts.html', {'posts':posts})

def reviewCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviewPosts')
    else:
        form = PostForm()
    return render(request, 'review_create.html', {'form':form})

def reviewDetail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'review_detail.html', {'post':post})

def reviewUpdate(request, pk):
    post = get_object_or_404(Post, pk = pk)

    if request.method == 'POST':
        form  = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('reviewPosts')
    else:
        form = PostForm(instance=post)

    return render(request, 'review_update.html', {'form':form})

def reviewDelete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('reviewPosts')

def mypage(request):
    return render(request, 'mypage.html')