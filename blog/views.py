from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
{
'author':'AlexMa',
'title':'Blog Post 1',
'content': 'First post content',
'date_posted': 'August 27 , 2019'
},
{
'author':'Jane',
'title':'Blog Post 2',
'content': 'Second post content',
'date_posted': 'July 27 , 2020'
}
]

# Create your views here.
def home(request):
    context  = {
    'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
