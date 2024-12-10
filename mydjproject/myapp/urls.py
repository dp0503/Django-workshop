from django.urls import path
from . import views
urlpatterns=[
    path("",views.homepage),
    path("home",views.homepage),
    path("about",views.aboutpage),
    path("contact",views.conatactpage),
]