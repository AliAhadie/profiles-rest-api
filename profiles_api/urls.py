from django.urls import path
from profiles_api import views

urlpatterns=[
    path('test/',views.HelloApiView.as_view()),
]