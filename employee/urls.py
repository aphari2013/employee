from django.urls import path
from employee import views
urlpatterns=[
    # path('index',views.IndexView.as_view()),
    # path('login',views.LoginView.as_view()),
    # path('registration',views.RegView.as_view(),name="register"),
    # path('profile/add',views.EmployeeCreateView.as_view(),name="emp-add"),

    path('add',views.EmployeeCreateView.as_view(),name="emp-add"),
    path('all',views.EmployeeListView.as_view(),name="emp-list"),
    path("details/<str:emp_id>",views.EmployeeDetails.as_view(),name="emp-detail"),
    path("change/<str:e_id>",views.EmployeeEditView.as_view(),name="emp-edit"),
    path("remove/<str:e_id>",views.remove_employee,name="emp-remove")

]

