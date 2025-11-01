import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    #restrict to working space
    rel_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(rel_path)
    abs_working_path = os.path.abspath(working_directory)
    if not abs_path.startswith(abs_working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path[-3:] == ".py":
        return f'Error: "{file_path}" is not a Python file.'


    #setup restriction
    restricted_env = os.environ.copy()
    restricted_env['Home'] = abs_working_path
    restricted_env['PATH'] = '/usr/bin:/bin'

    try:
        command = ["python3", abs_path] + args
        run_object = subprocess.run(command, capture_output=True,text=True, timeout=30, env=restricted_env, cwd=abs_working_path)

        if run_object.stdout == None and run_object.stderr == None:
            return_string = "No output produced."
        else:
            return_string = f'STDOUT: {run_object.stdout}\n STDERR: "{run_object.stderr}".'
        if not (run_object.returncode == 0):
            return_string += f'\n Process exited with code {run_object.returncode}.'

        return return_string

    except Exception as e:
        return f'Error occured during execution of {file_path}:\n{e}'