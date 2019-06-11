from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    path('home/', wordcount.views.home, name=""),
    path('about/', wordcount.views.about, name="about"),
    path('result/', wordcount.views.result, name="result"),

]
