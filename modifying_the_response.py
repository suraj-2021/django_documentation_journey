from django.template.response import TemplateResponse

def my_middleware(get_response):
    def middleware(request):
        response = get_respnse(request)
        if isinstance(response,TemplateResponse):
              response.context_data['addtional_info'] = 'This is added by middleware!"
              return response
      return middleware

def about(rquest):
      context={
            "title": "About Us",
            "description": "Learn more about us"      }

      return TempalateResponse(request,'about.html', context)
