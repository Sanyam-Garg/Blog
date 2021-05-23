from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    return redirect('App_Blog:blog_list')