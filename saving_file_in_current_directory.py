from django.core.files.base import ContentFile
from.django.core.files.storage import default_storage

file_content = ContentFile(b"Hello World!")
file_name = default_storage.save("hello.txt", file_content)

print(f"File saved at : {file_name}")
