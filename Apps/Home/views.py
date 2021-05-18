from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import datetime

class Home(View):
    template = 'Home/base.html'
    def get(self,request):
        return render(request,self.template)
    def post(self,request):
        pass