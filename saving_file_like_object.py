from django.core.file.base import ContentFile
from .models import MyModel

data = "This is our sample data, we can use this sample data anywhere"

file_content = ContentFile(data.encode('utf-8'), name= 'data.txt')

my_model_instance = MyModel()
my_model_instance.file_field.save(file_content.name, file_content)
