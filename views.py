from inspect import EndOfBlock
from django.shortcuts import render
def primeload(request):
    return render(request,"primeapp/index.html")

def primelogic(request):
    num = int(request.GET["txtnum1"])
    res = ""
    for i in range(2,num):
        if num%i==0:
            res = "Not prime"
            break
    else:
        res = "Prime"   

    return render(request,"primeapp/index.html",{"res":res})

def primeseries(request):
    return render(request,"primeapp/sindex.html")

def primeserieslogic(request):
    start = int(request.GET["txts"])
    end = int(request.GET["txte"])
    x=[]
    for num in range(start,end):
      for j in range(2,num):
        if num%j==0:
           break
      else:
          x.append(num)
         

    return render(request,"primeapp/sindex.html",{"res":x})