from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# >>> 10

def learNow_list(request):
    return render(request, 'learnow/learnow_list.html')

