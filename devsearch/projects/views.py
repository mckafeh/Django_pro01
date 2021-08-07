from django.shortcuts import render
from django.http import HttpResponse
from projects.models import project


def projects(request):
    #return HttpResponse('here are our products')
     projects = Project.objects.all()
     context = {'projects':projects}
     return render(request,'projects/projects.html', context)

def project(request,pk):
    #return HttpResponse('SINGLE Project'+ ' '+ str(pk))
    projectObj = Project.object.get(id=pk)
    return render(request,'projects/single-project.html',{'project':projectObj})


# Create your views here.
