import os
from .config import CHAR_LIMIT


def get_file_content(working_directory, file_path):
    #restrict to working space
    rel_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(rel_path)
    abs_working_path = os.path.abspath(working_directory)
    if not abs_path.startswith(abs_working_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(rel_path): 
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(abs_path, "r") as f:
        file_content_string = f.read(CHAR_LIMIT)
        extra = f.read(1)
        if extra:
            file_content_string += f'[...File "{file_path}" truncated at {CHAR_LIMIT} characters]'

    return file_content_string