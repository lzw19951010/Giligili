from django.shortcuts import render
from .models import Video
from .models import Comment
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse

def video_play(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    if (not request.user.is_authenticated() or not request.user.is_staff) and video.status != 4:
        return render(request, "video-notfound.html")
    comments = video.comment_set.all()#.order_by("-date")[:3]
    return render(request, 'video.html', {'video': video,'latest_comment':comments})

@require_http_methods(["POST"])
def video_pass(request, video_id):
	if not request.user.is_authenticated() or not request.user.is_staff:
		return HttpResponseForbidden()
	try:
		video = Video.objects.get(pk=video_id)
	except Video.DoesNotExist:
		return Http404("Video not found")
	video.status = 0
	video.save()
	return HttpResponse()

@require_http_methods(["POST"])
def video_ban(request, video_id):
	if not request.user.is_authenticated() or not request.user.is_staff:
		return HttpResponseForbidden()
	try:
		video = Video.objects.get(pk=video_id)
	except Video.DoesNotExist:
		return Http404("Video not found")
	video.status = 2
	video.save()
	return HttpResponse()