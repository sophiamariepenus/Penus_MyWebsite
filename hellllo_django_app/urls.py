from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns =[
    path('home/', HomePageView.as_view(), name ="homeview"),
    path('about/', AboutPageView.as_view(), name ="aboutview"),
    path('contact/', ContactPageView.as_view(), name ="contactview"),
]