import os
from google.genai import types


def write_file(working_directory, file_path, content):
    #restrict to working space
    rel_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(rel_path)
    abs_working_path = os.path.abspath(working_directory)
    if not abs_path.startswith(abs_working_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    #if file not exist, create directory if necessary
    if not os.path.exists(os.path.dirname(abs_path)):
        os.makedirs(os.path.dirname(abs_path))
    
    with open(abs_path, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'







schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites a file with the content or if nonexistant creates a new file with the content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file that is beeing overwritten or created, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that overwrites an existing file, or is inserted in a newly created file.",
            ),
        },
    ),
)