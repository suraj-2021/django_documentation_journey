from django.http import FileResponse, HttpResponseNotFound
from.models import UploadedFile

def returning_uploaded_file(request,file_id):
    try:
          requested_file = UploadedFile.objects.get(id=file_id)
          response = FileResponse(requested_file.file, attachment=true, filename=UploadedFile.filename)
          return response
    except UploadedFile.DoesNotExist:
           return HttpResponseNotFound()
