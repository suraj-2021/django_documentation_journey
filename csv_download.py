
import csv
from django.http import HttpResponse

def my_file(request):
    response = HttpResponse(content_type="text/csc", headers = {
          "Content-Dispositon": 'attachment'; filename = "myfilename.csv"},
      )
    writer = csv.writer(response)
    writer.writerow(["First Row", "First Name", "Last Name","Occupation"])
    writer.writerow(["Second Row","Salrary","Expenses","Vacation"])

    return response


