from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    # return HttpResponse('projects')
    return render(request, 'projects/projects.html')


def single_project(request, pk):
    # return HttpResponse('single project ' + str(pk))
    return render(request, 'projects/single-project.html')
