from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, 'log.html')
def operation(request):
    x = int(request.GET.get('num1'))
    y = int(request.GET.get('num2'))
    sum=x+y
    mul=x*y
    div=x/y
    sub=x-y
    return render(request, 'result.html',{'sum':sum,'mul':mul,'div':div,'sub':sub})


# Create your views here.
