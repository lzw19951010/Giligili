from django.shortcuts import render
from .models import Video
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_http_methods


def video_play(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    if (not request.user.is_authenticated() or not request.user.is_staff) and video.status != 4:
        return render(request, "video-notfound.html")
    return render(request, 'video.html', {'video': video})