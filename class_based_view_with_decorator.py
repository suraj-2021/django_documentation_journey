class MyView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, authenticated user!")

    @method_decorator(some_other_decorator)
    def post(self, request, *args, **kwargs):
        return HttpResponse("This is a POST request.")
