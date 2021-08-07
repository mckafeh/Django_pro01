from django.shortcuts import render
from django.http import HttpResponse
from projects.models import project


projectsList = [
    {
        'id':'1',
        'title':"Ecommerce website",
        'description': 'Fully functionla ecommerce web site'
    },
    {
        'id':'2',
        'title':"Portfolio website",
        'description': 'This was a prject where I built out my portfolio'
    },

    {
        'id':'3',
        'title':"Socila Network",
        'description': 'Awesome open source project I am still working'
    },

]

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
