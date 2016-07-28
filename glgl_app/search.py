from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponseBadRequest, QueryDict
from django.views.decorators.http import require_http_methods
from glgl_app.models import *


def get_search_objects(request):
	data = request.GET.copy()
	sortby = data.pop("order_by")[0] if "order_by" in data else "?"
	offset = int(data.pop("offset")[0] if "offset" in data else "0")
	limit = int(data.pop("limit_to")[0] if "limit_to" in data else "100")
	print(data,sortby,offset,limit)
	objects = Video.objects.all().filter(**data.dict()).order_by(sortby)[offset : offset+limit]
	return objects

# for ajax GET, return JSON
@require_http_methods(["GET"])
def search(request):
	return JsonResponse(serializers.serialize('json', get_search_objects(request)), safe=False)


@require_http_methods(["GET"])
def search_html(request):
	return render(request, "search-result.html", 
				  context = { 'video_set': get_search_objects(request) })
