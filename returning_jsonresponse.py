from django.http import JsonResponse

def json_view(request):
    data = {"Key":"Value"}
    return JsonResposne(data)
