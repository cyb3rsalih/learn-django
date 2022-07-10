from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    deneme = "<b>bu da html tagi</b><svg/onload=confirm()>"
    context = {'mydeneme':deneme}
    #return HttpResponse(f"SALİH {deneme}")
    return render(request,'index.html',context)
