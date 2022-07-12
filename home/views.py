
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubmitForm
from .forms import ChisForm
from scipy.stats import t
from scipy.stats import chi2
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
            m1 = form.cleaned_data['mean_1']
            m2 = form.cleaned_data['mean_2']
            s1 = form.cleaned_data['stdev_1']
            s2 = form.cleaned_data['stdev_2']

            #print(f"n1: {n1}\nn2: {n2}\nm1: {m1}\nm2: {m2}\ns1: {s1}\ns2: {s2}") # Debug
            
            t_value = abs(m1-m2) / math.sqrt( ( s1**2/n1) + (s2**2/n2))
            p_value = 2*(1 - t.cdf(t_value,n1+n2-2))
            t_value = round(t_value,3)
            p_value = round(p_value,3)
            data = {'t_value':t_value,'p_value':p_value}
            return render(request,'result.html',data)
    form = SubmitForm
    return render(request,'form.html',{'form':form})


def chisform(request):

    if request.method == 'POST':
        form = ChisForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = form.cleaned_data['d']

            N = a+b+c+d
            ae = ((a+c) * (a+b)) / N
            be = ((b+d) * (b+a)) / N
            ce = ((c+a) * (c+d)) / N
            de = ((d+b) * (d+c)) / N

            cs = (((a - ae)**2) / ae) + (((b - be)**2) / be) + (((c - ce)**2) / ce) + (((d - de)**2) / de)

            chcdf =  chi2.cdf(cs,1)
            # print("AAAAAA"+str(cs))
            p_value = 1 - chcdf

            cs = round(cs,3)
            p_value = round(p_value,3)

            data = { "chi_square":cs, "p_value":p_value }
           
            return render(request,'result2.html',data)
    form = ChisForm
    return render(request,'form2.html',{'form':form})
