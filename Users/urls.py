from django.urls import path
#from .views import 
from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    #path("<int:pk>/", DetailPostView.as_view(), name="post-page"),
]