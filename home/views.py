from django.http import HttpResponse
from django.shortcuts import render_to_response, render
def home(request):
    return render(request, "home/home.html", {},content_type="application/xhtml+xml")
