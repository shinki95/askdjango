# _*_ coding: utf-8 _*_

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from .models import Post
from PIL import Image,ImageDraw,ImageFont
from django.http import HttpResponse, Http404
import os.path
import random

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'blog/post_list.html', {
        'post_list':qs,
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })




def post_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('/blog/')
    else: 
        form = PostModelForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('/blog/')
    else: 
        form = PostModelForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

def hello(request, name, company):
    size = (250, 250)
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    x = random.randrange(10,150)
    y = random.randrange(10,150)
    a = random.randrange(10,150)
    b = random.randrange(10,150)
    red = (255, 255, 255)
    text1 = name
    text2 = company
    draw.text((x, y), text1, fill=red)
    draw.text((a, b), text2, fill=None)
    response = HttpResponse(content_type="image/jpg")
    image.save(response, 'JPEG')
    return response
