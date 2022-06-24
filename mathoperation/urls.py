from django.urls import path
from mathoperation import views
urlpatterns=[
    path("add",views.MathView.as_view()),
]