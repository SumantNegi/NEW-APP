from django.shortcuts import render
import requests
import json

API_KEY  = '38a50a4437614a73ae624ec0c5e05578'

# Create your views here.
def home(request):
   url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
   response= requests.get(url)
   articles= json.loads(response.content) 

   return render(request,'home.html',{'articles':articles},)

def sports(request):
   url = f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}'
   response= requests.get(url)
   articles= json.loads(response.content) 

   return render(request,'sports.html',{'articles':articles} )

def health(request):
   url = f'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={API_KEY}'
   response= requests.get(url)
   articles= json.loads(response.content) 

   return render(request,'health.html',{'articles':articles} )

def ent(request):
   url = f'https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={API_KEY}'
   response= requests.get(url)
   articles= json.loads(response.content) 

   return render(request,'general.html',{'articles':articles} )

def business(request):
   url = f'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}'
   response= requests.get(url)
   articles= json.loads(response.content) 

   return render(request,'business.html',{'articles':articles} )

def tech(request):
   url = f'https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={API_KEY}'
   response= requests.get(url)
   articles= json.loads(response.content) 

   return render(request,'tech.html',{'articles':articles} )