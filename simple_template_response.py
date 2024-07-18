
from django.template.response import SimpleTemplateResponse

def my_view(request):
      template_name = "myapp/templates/home.html"
      context_data = {"users":"10K"}

      response = SimpleTemplateResponse(template_name, context = context_data)

      return response.render()

