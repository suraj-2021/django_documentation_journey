from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def your_view(requst):
    user_name = request.user

    return HttpResponse(f"Hello {user_name.username}!")



