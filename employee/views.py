# from django.shortcuts import render
# from django.shortcuts import redirect
# from django.http import HttpResponse
# from django.views.generic import View
# from employee.forms import EmployeeForm
# from django.contrib import messages
# # Create your views here.
#
# # function based views
# # class based views
#
# def index(request):
#     return render(request,"index.html")
#
# def login(request):
#     return render(request,"login.html")
#
# def registration(request):
#     return HttpResponse("Registration")
#
#
# class IndexView(View):
#     def get(self,request):
#         return render(request,"index.html")
# class LoginView(View):
#     def get(self,request):
#         return render(request,"login.html")
#     def post(self,request):
#         print(request.POST.get("u_name"))
#         print(request.POST.get("pwd"))
#         return render(request,"login.html")
# class RegView(View):
#     def get(self,request):
#         return render(request,"reg.html")
#     def post(self,request):
#         print(request.POST.get("f_name"))
#         print(request.POST.get("l_name"))
#         print(request.POST.get("u_name"))
#         print(request.POST.get("e_mail"))
#         print(request.POST.get("pwd"))
#         return render(request,"reg.html")
# class EmployeeCreateView(View):
#     form_class=EmployeeForm
#     template_name="emp-add.html"
#
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         print("values in request.POST")
#         print(request.POST)
#         if form.is_valid():
#             print("cleaned_data")
#             print(form.cleaned_data)
#             print(form.cleaned_data.get("eid"))
#             print(form.cleaned_data.get("employee_name"))
#             print(form.cleaned_data.get("designation"))
#             # return render(request,self.template_name,{"form":form})
#             messages.success(request,"Profile has been added")
#             return redirect("emp-add")
#         else:
#             messages.error(request,"Profile adding failed")
#             return render(request,self.template_name,{"form":form})

from django.shortcuts import render
from django.shortcuts import redirect
from employee.models import Employee
from django.contrib import messages
from django.views.generic import View
from employee.forms import EmployeeCreateForm

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeCreateForm()
        return render(request,"emp-add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # Employee.objects.create(
            #     eid=form.cleaned_data.get("eid"),
            #     employee_name=form.cleaned_data.get("employee_name"),
            #     designation=form.cleaned_data.get("designation"),
            #     salary=form.cleaned_data.get("salary"),
            #     email=form.cleaned_data.get("email"),
            #     experience=form.cleaned_data.get("experience"),
            #
            # )
            messages.success(request,'employee has been added')
            return redirect("emp-add")
        else:
            messages.ERROR(request,"employee not added")
            return render(request, "emp-add.html",{"form":form})

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        return render(request,"emp-list.html",{"employees":qs})
class EmployeeDetails(View):
    def get(self,request,*args,**kwargs):
        #kwargs={emp_id:emp_100}
        # print(kwargs)
        emp_id=kwargs.get("emp_id")
        qs=Employee.objects.get(eid=emp_id)
        return render(request,"emp-detail.html",{"employee":qs})

class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(eid=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request,"emp-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(eid=eid)
        form = EmployeeCreateForm(request.POST,instance=employee,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'employee has been updated')
            return render(request, "emp-add.html", {"form": form})
        else:
            messages.ERROR(request, "employee not added")
            return render(request, "emp-add.html", {"form": form})
def remove_employee(request,*args,**kwargs):
    eid=kwargs.get("e_id")
    employee=Employee.objects.get(eid=eid)
    employee.delete()
    messages.error(request,"employee has been removed")
    return redirect("emp-list")


