from django.shortcuts import render
from . models import Movieinfo
# Create your views here.
from . forms import Movieform
def create(request):
    frm=Movieform()
    if request.POST:
         frm=Movieform(request.POST)
         if frm.is_valid:
              frm.save()
    else:
         frm=Movieform()
    return render(request,'create.html',{'frm':frm})

def list(request):
        data_set=Movieinfo.objects.all()
        print(data_set)
        return render(request,'list.html',{'movie' : data_set} )

def edit(request,pk):
      instance_to_be_edited=Movieinfo.objects.get(pk=pk)
      if request.POST:
            frm=Movieform(request.POST,instance=instance_to_be_edited)
            if frm.is_valid():
                  instance_to_be_edited.save()
      else:
            frm=Movieform(instance=instance_to_be_edited)

      return render(request,'create.html',{'frm':frm})

def delete(request,pk):
        instance=Movieinfo.objects.get(pk=pk)
        instance.delete()
        data_set=Movieinfo.objects.all()
        return render(request,'list.html',{'movie' : data_set} )
