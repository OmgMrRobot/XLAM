from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST
import re


def simple_route(request):
    if request.method == 'GET':
        return HttpResponse(content='', status=200)
    elif request.method == 'POST':
        return HttpResponse(status=405)
    elif request.method == 'PUT':
        return HttpResponse(status=405)
    else:
        return HttpResponse(status=404)



def slug_route(request, slug):
    return HttpResponse(content=slug)


def sum_route(request, a, b):
    return HttpResponse(content=f'{int(a) + int(b)}', status=200)


@require_GET
def sum_get_method(request):
    if len(list(request.GET.values())) > 1:
        a, b = request.GET.values()
        try:
            a, b = int(a), int(b)
        except:
            return HttpResponse(status=400)
        return HttpResponse(content=f'{a + b}', status=200)
    else:
        return HttpResponse(status=400)


@require_POST
def sum_post_method(request):
    if len(list(request.POST.values())) > 1:
        a, b = request.POST.values()
        try:
            a, b = int(a), int(b)
        except:
            return HttpResponse(status=400)
        return HttpResponse(content=f'{int(a) + int(b)}', status=200)
    return HttpResponse(status=400)


