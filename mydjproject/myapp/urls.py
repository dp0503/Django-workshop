from django.urls import path
from . import views
urlpatterns=[
    path("",views.homepageview),
    path("home",views.homepageview),
    path("form",views.formpageview),
    path('process',views.formpageprocess),

]