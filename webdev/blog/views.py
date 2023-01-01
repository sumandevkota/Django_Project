from django.shortcuts import render

posts = [ 
    {
        'author':'SumanD',
        'title':'Blog post 1',
        'content': 'First post Content',
        'date_posted':'December 30,2022'
    },
    {
        'author':'Ojashpi',
        'title':'Blog post 2',
        'content': 'Second post Content',
        'date_posted':'December 25,2022'
    },
    {
        'author':'Sadeep',
        'title':'Blog post 3',
        'content': 'Third post Content',
        'date_posted':'December 20,2022'
    },
    {
        'author':'Ashika',
        'title':'Blog post 4',
        'content': 'Fourth post Content',
        'date_posted':'December 15,2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})


