from django.shortcuts import render

# Create your views here.


def forloops(request):
    d={'name':'Siva'}
    return render(request,'forloops.html',d)
