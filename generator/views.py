from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
  return render(request,'generator/homepage.html') 

def password(request):
  generated_pass = ''
  chars = list('abcdefghijklmnopqrstuvwxyz')
  
  #12 is the default length if not given any 
  length = int(request.GET.get('length',12))
  
  if request.GET.get('uppercase'):
    chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
  if request.GET.get('numbers'):
    chars.extend(list('1234567890'))
  if request.GET.get('special'):
    chars.extend(list('!@#$%^&*()<>+={}[]\|'))
	
  for i in range(length):
    generated_pass += random.choice(chars)	
  
  return render(request,'generator/password.html',{'password':generated_pass}) 
  
def nikhil(request):
  return HttpResponse("<h1>Nikhil Choudhary is an awesome guy!</h1>")

def show(request):
  return render(request,'generator/page.html',{'name':'Nikhil Choudhary'}) 

def about(request):
  return render(request,'generator/about.html')