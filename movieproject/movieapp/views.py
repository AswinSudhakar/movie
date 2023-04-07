
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm
def index(request):
    movie1= movie.objects.all()
    context={
        'movie_list':movie1

    }

    return render(request,'index.html',context)

def detail(request,movie_id):
    movie1= movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie1})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        movie1=movie(name=name,desc=desc,year=year,img=img)
        movie1.save()

    return render(request,'add.html')

def update(request,id):
    movie1=movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie1})

def delete(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')