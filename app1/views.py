from django.shortcuts import render

# Create your views here.

def home(request):
    data={
        "title":"this is django app",
        "clist":["jiya","krish"],
        "dlist":[{"A":"best","B":"better"},{"A":"good","B":"ok"}]}
    return render(request, 'index.html',data)
