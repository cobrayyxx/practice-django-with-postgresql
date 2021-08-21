from django.shortcuts import render
from django.db import connection
import requests, json 
# Create your views here.
def dummy(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM STUDENT")
        row = cursor.fetchall()
    
    return render(request, 'index.html',{'row':row})

