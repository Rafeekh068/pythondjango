from django.shortcuts import render
from . models import Movieinfo
# Create your views here.

def create(request):
    if request.POST:
         title = request.POST.get('Title')
         year = request.POST.get('Year')
         desc = request.POST.get('Summary')
         movie_obj=Movieinfo(title=title,year=year,summary=desc)
         movie_obj.save()
    return render(request,'create.html')

def list(request):
        movie_data={
        'movie':[
             {
        'title':'premalu',
        'year':2024,
        'summary':'love story',
        'sucess':True,
        'img':'alpha.jpg'
        },
        {
        'title':'marakkar',
        'year':2021,
        'sucess':False,
        'img':'beta.jpg'
        },
        {
        'title':'pulimurukan',
        'year':2017,
        'summary':'action',
        'sucess':True,
        'img':'gama.jpg' 
        },
        {
        'title':'ozler',
        'year':2024,
        'summary':'investigation thriller ',
        'sucess':True,
        'img':'neo.jpg'
        }
        ]
        }
        return render(request,'list.html',movie_data)

def edit(request):
    return render(request,'edit.html')
