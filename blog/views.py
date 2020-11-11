from django.shortcuts import render

posts = [
  {
    'author' : 'Pratik',
    'title' : 'Blog Post 1',
    'content' : 'This is the content.',
    'date_posted' : 'November 11, 2020'
  },
  {
    'author' : 'Pratik',
    'title' : 'Blog Post 2',
    'content' : 'This is the content of 2nd Post.',
    'date_posted' : 'November 10, 2020'
  },
]

def home(request):
  context = {
    'posts' : posts,
    'title' : 'Home'
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')