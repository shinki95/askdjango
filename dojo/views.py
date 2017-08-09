from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView
from .forms import PostForm
from .models import Post


post_detail = DetailView.as_view(model=Post)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form_is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else: 
        form = PostForm()
    return render(request, 'dojo/post_form.html', {
            'form': form,
        })

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form_is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')
    else: 
        form = PostForm(instance=post)
    return render(request, 'dojo/post_form.html', {
            'form': form,
        })


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse("안녕하세요 {}.{}살이시네요.".format(name, age))


def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>Askdjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
        '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name': name})


def post_list3(request):
    return JsonResponse({
        'message':'안녕, 파이썬&장고',
        'items': ['파이썬','장고', 'Celery', 'Azure', 'AWS'],
        }, json_dumps_params={'ensure_ascii': False})

