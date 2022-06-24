from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm
# Create your views here.


class HomeView(View):
    def get(self,request):
        return render(request,"calc-home.html")

class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"add1.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)+int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1+n2
            print(form.cleaned_data)
            return render(request,"add1.html",{"res":result,"form":form})
        else:
            return render(request,"add1.html",{"form":form})
class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"sub.html",{"form":form})
    def post(self,request):
        # n1 = request.POST.get("num1")
        # n2 = request.POST.get("num2")
        # result = int(n1) - int(n2)
        form=OperationForm(request.POST)
        if not form.is_valid():
             return render(request,"sub.html",{"form":form})
        n1=form.cleaned_data.get("num1")
        n2=form.cleaned_data.get("num2")
        result=n1-n2
        return render(request,"sub.html",{"subres":result,"form":form})
class FactView(View):
    def get(self,request):
        return render(request,"fact.html")
    def post(self,request):
        n1 = int(request.POST.get("num1"))
        def fact(n1):
            if n1 == 1:
                return n1
            else:
                return n1 * fact(n1 - 1)

        result = fact(n1)
        return render(request, "fact.html", {"factres": result})
class DivView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"div.html",{"form":form})
    def post(self,request):
        # n1 = request.POST.get("num1")
        # n2 = request.POST.get("num2")
        # result = int(n1) /int(n2)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1/n2
            return render(request,"div.html",{"divres":result,"form":form})
        else:
            return render(request,"div.html",{"form":form})
class MultiView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"multi.html",{"form":form})
    def post(self,request):
        # n1 = request.POST.get("num1")
        # n2 = request.POST.get("num2")
        # result = int(n1) *int(n2)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1*n2
            return render(request,"multi.html",{"multires":result})
        else:
            return render(request,"multi.html",{"form":form})
class WordcountView(View):
    def get(self,request):
        return render(request,"wordcount.html")
    def post(self,request):
        word=request.POST.get("word")
        words=word.split(" ")
        wc={}
        for w in words:
            if w not in wc:
                wc[w]=1
            else:
                wc[w]+=1
        for k,v in wc.items():
            print(k,v)
        return render(request,"wordcount.html",{"wordres":wc})

class PrimerangeView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"primerange.html",{"form":form})
    def post(self,request):
        l=int(request.POST.get("num1"))
        u=int(request.POST.get("num2"))
        p=[]
        for i in range(l, u + 1):  # i=5,6,...,25
            for j in range(2, i):  # j=2,3,...24
                if i % j == 0:
                    # print(i,"not prime")
                    break
            else:
                p.append(i)
        return render(request,"primerange.html",{"primeres":p})
