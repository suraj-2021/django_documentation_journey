from django.http import HttpResponse
from django.template import loader

def my_csv(rquest):
    response  = HttpResponse(content_type = "text/css",headers = { "Content-Disposition":'attachment';filename = "myfilecsv.txt"})
    csv_data = (("First Row", "Apple","Ball","Cat","Dog",), ("Second Row","Elephant","Firefly","Green",),)

   t = loader.get_template("myfile.txt")
   c = {'data':csv_data}
   response.write(t.render(c))
   return response
