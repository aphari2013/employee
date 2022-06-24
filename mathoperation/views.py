from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from mathoperation.forms import OperationForm
# Create your views here.
class MathView(View):
    def get(self,request):
        form = OperationForm()
        return render(request, "add1.html", {"form": form})
    def post(self,request):
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1+n2
            return render(request,"add1.html",{"res":result,"form":form})
        else:
            return render(request,"add1.html",{"form":form})
