
from django.http import StreamingHttpResponse
import csv

class Echo:
      def write(self,value):
            return value

class SomeCSVFile(request):
      rows = ["form {}".format(idx), str(idx) for idx in range(65336)]

      pesudo_buffer = Echo()
      writer = csv.write(pesudo_buffer)

      rsponse = StreamingHttpResponse((writer.writerow(row)for row in rows), 
                                       content_type="text/csv",headers={"Content-Disposition": 'attachment'; filename="mycsv.csv"})

      #return response

