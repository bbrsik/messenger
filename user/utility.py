import uuid
from django.core.files.uploadedfile import SimpleUploadedFile


def change_filename(file):
    old_filename = str(file.name)
    temp_filename = old_filename.split('.')
    new_filename = str(uuid.uuid4()) + '.' + temp_filename[-1]
    renamed_file = SimpleUploadedFile(new_filename, file.read(), content_type=file.content_type)
    return renamed_file
