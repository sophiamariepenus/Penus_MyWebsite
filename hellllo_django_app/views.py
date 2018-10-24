from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView (TemplateView):
    template_name = "home.html"
    def get_context_data(self):
        data = { "fav_quote" : "IF YOU CAN DREAM IT, YOU CAN DO IT." }
        return data

class AboutPageView (TemplateView):
    template_name = "about.html"

class ContactPageView (TemplateView):
    template_name = "contact.html"

    