from django.views.decorators import require_http_methods
from django.shortcuts import HttpResponse

#require_http_methods decorator
@require_http_methods(["GET","POST"])
def sample_view(request):
    return HttpResponse("Only the GET and POST methods can access this view")



#require_GET() decorator ]
from django.view.decorators import require_GET
from django.shortcuts import HttpResponse

@require_GET()
def sample_view(request):
    return HttpResponse("Only the GET requests can access this view!")

#require_POST() decorator
@require_POST()
def sample_view(request):
    return HttpResponse("This view only responds to POST requessts")

#require_safe() decorator
@require_safe()
def sample_view(request):
    return HttpResponse("Only the GeT and HEAD request methods can access this view")
