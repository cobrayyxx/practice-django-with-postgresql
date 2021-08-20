from django.shortcuts import render
import requests, json 
# Create your views here.
def dummy(request):
    return(request, 'index.html')