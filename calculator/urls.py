from django.urls import path
from calculator import views
urlpatterns=[
    path("home",views.HomeView.as_view(),name="calc-home"),
    path("add",views.AddView.as_view(),name="calc-add"),
    path("sub",views.SubView.as_view(),name="calc-sub"),
    path("fact",views.FactView.as_view(),name="calc-fact"),
    path("div",views.DivView.as_view(),name="calc-div"),
    path("multi",views.MultiView.as_view(),name="calc-multi"),
    path("wordcount",views.WordcountView.as_view(),name="calc-wordcount"),
    path("primerange",views.PrimerangeView.as_view(),name="calc-prime"),
]