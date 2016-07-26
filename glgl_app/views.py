from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from glgl_app.models import *
# Create your views here.
@require_http_methods(["GET"])
def index(request):
	return render(request, "index.html", context={'popular_videos': Video.objects.filter(status=4).order_by("-play")[:12],})
def home(request):
	return render(request, "home.html")
def setPasswordSuc(request):
	return render(request,"setpassword-suc.html")