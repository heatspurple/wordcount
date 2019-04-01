from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋 #메소드
    return render(request, 'home.html', {'blogs': blogs})
    #Blog 안에있는 objects를 blogs안에 담아줄것이다.
