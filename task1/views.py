from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.


class Home(View):
    def get(self, requests, *args, **kwargs):
        return HttpResponse("hello,world")
