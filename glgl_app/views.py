from django.shortcuts import render
from django.views.decorators.http import require_http_methods
# Create your views here.
@require_http_methods(["GET"])
def index(request):
    return render(request, "index.html")
def home(request):
	return render(request, "home.html")
# Create your views here.