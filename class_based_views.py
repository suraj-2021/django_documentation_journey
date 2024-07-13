from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.views.defaults import page_not_found, server_error

def custom_view(request):
   
    return HttpResponse("Hello from custom view!")

# Class-Based View
class MyListView(ListView):
    model = YourModel  # Replace with your actual model
    template_name = "myapp/my_list.html"
    context_object_name = "objects" 

# Custom error views
handler404 = page_not_found
handler500 = server_error
