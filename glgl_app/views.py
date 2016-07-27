from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from glgl_app.models import *
# Create your views here.
@require_http_methods(["GET"])
def index(request):
	return render(request, "index.html", context={'popular_videos': Video.objects.filter(status=0).order_by("-play")[:12],})
def category(request,category_id):
	return render(request, "index.html", context={'category_videos': Video.objects.filter(status=0, category = category_id)})
def home(request):
	return render(request, "home.html")
def setPasswordSuc(request):
	return render(request,"setpassword-suc.html")

@require_http_methods(["GET"])
def homepage(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
	except User.DoesNotExist:
		raise Http404("User does not exist")
	return render(request, 'homepage.html',{'pageuser': user})

@require_http_methods(["GET"])
def checkpage(request):
	if not request.user.is_staff:
		return render(request, 'notadmin.html')
	else:
		return render(request, 'check.html', context={'checking_videos': Video.objects.filter(status=4).order_by("time"),})