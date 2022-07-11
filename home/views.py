
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubmitForm
from scipy.stats import t
import math
# Create your views here.
def index(request):
    deneme = "<b>bu da html tagi</b><svg/onload=confirm()>"
    context = {'mydeneme':deneme}
    #return HttpResponse(f"SALİH {deneme}")
    return render(request,'index.html',context)



def myform(request):

    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data['n1']
            n2 = form.cleaned_data['n2']
            m1 = form.cleaned_data['m1']
            m2 = form.cleaned_data['m2']
            s1 = form.cleaned_data['s1']
            s2 = form.cleaned_data['s2']

            #print(f"n1: {n1}\nn2: {n2}\nm1: {m1}\nm2: {m2}\ns1: {s1}\ns2: {s2}") # Debug
            
            t_value = abs(m1-m2) / math.sqrt( ( s1**2/n1) + (s2**2/n2))
            p_value = 2*(1 - t.cdf(t_value,n1+n2-2))

            data = {'t_value':t_value,'p_value':p_value}
            return render(request,'result.html',data)
    form = SubmitForm
    return render(request,'form.html',{'form':form})