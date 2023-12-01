from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib import messages

# Create your views here.
def home(request):
    all_posts = Post.objects.all().order_by("-date_created")
    context = {"posts": all_posts}
    return render(request,'app/index.html', context)
def testing(request):
    return HttpResponse('Homepage')
def big(request):
    return HttpResponse('All is not well')

def asiwaju(request):
    return render(request,'app/men.html')
def crush(request):
    return render(request, 'app/tosin.html')
def reading (request,id):
    item = Post.objects.get(id=id)
    context = {"item":item}
    return render(request, 'app/lola.html',context)
def createblog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES['img']
        new_blog = Post.objects.create(title=title, body=body, picture=image)
        new_blog.save()
        messages.success(request,"Sucessfully created")
        return redirect('home')
    return render( request, 'app/ini.html')
def delete(request,id):
    recyclebin = Post.objects.get(id=id)
    recyclebin.delete()
    messages.success(request,"Deleted successfully")
    return redirect("home")
def edit(request,id):
    editpost = Post.objects.get(id=id)
    context = {"post": editpost}
    if request.method =='POST':
        title=request.POST.get('title')
        body = request.POST.get('body')
        editpost.title = title
        editpost.body = body
        editpost.save()
        messages.success( request,'Edited')
        return redirect('home')
    return render(request, 'app/edit.html', context)
    # editpost.edit()
    # messages.success(r)
# def createblog(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         body = request.POST.get('body')
#         print(title,body)
#     return render( request, 'app/ini.html')
# def createblog(request):
#     print(request.method)
#     return render( request, 'app/ini.html')
# def greeting(request):
#     context = {"name": "Omolola"}
#     return render (request,"app/greet.html",context)
# def greeting(request, name):
#     print(name)
#     context = {"name": "Omolola"}
#     return render (request,"app/greet.html",context)
# def greeting(request, name):
#     context = {"name": name}
#     return render (request,"app/greet.html",context)
# def greeting(request, name, age):
    # context = {"name": name, "age": age}
    # return render (request,"app/greet.html",context)
def greeting(request,name,age):
    try:
        age= int(age)
    except BaseException:
        age = -1
    context ={'name':name,'age':age}
    return render(request,"app/greet.html",context)
def skincare(request):
    data = [
        {'name': 'retinol', "price": 10000},
        {'name':"toner", "price": 5000},
        {'name':'moisturiser', "price": 15000},
        {'name':'sunscreen', "price": 20000}
    ]
    context ={'data':data}
    
    return render(request,"app/products.html",context)
    
    