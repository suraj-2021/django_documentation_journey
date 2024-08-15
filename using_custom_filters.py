#Creating a custom filter fuction
#myapp/templatetags/my_filters.py

from django import template
register = template.Library()

@register.filter
def shout(value):
      return f"{value.upper()}!"



#views.py #this handles rendering of the template
def my_view(request):
      context = {
            'message': "Hey! this is the message!"
      }
      return render(request,"my_template.html", context)



#using this fiolter in orignal template
<html>
<head> <title> MyTitle</head>
<body>
   <h1> {{messgae|shout}}
</body>
