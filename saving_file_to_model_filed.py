from django.core.files import File
from .models import MyModel

with open("path/to/file.txt") as new_file:
      file = File(new_file)
      file.name = "myfile.txt"

      x = MyModel()
      x.file_filed.save(file.name, file)
