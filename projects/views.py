from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return HttpResponse('projects')


def single_project(request, pk):
    return HttpResponse('single project ' + str(pk))
