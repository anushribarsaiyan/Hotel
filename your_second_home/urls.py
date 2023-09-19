from django.urls import path, include
from your_second_home import views

urlpatterns = [
      path('home', views.home,name="homepage"),
]
