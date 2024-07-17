from django.http import HttpResponse

def your_vies(request):
    if request.method == "GET":
        return HttpResponse(f"Hey it's a response to the GET method!")

    elif request.method == "POST":
        return HttpResponse(f"Hey this is a respnse to the POST method!")

    else:
        return HttpResponse(f"Hey it's neither GET nor POST method!")
