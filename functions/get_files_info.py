import os

def get_files_info(working_directory, directory=None):
    result = ""
    path = os.path.join(working_directory, directory)
    
    if not os.path.isdir(path):
        #print(f'Error: "{directory}" is not a directory')
        return f'    Error: "{directory}" is not a directory\n'

    if working_directory not in os.path.abspath(path):
        #print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

    for file in os.listdir(path):
        #print(f'- {file} file_size={os.path.getsize(os.path.join(path, file))} bytes, is_dir={os.path.isdir(os.path.join(path, file))}')
        result += f' - {file}: file_size={os.path.getsize(os.path.join(path, file))} bytes, is_dir={os.path.isdir(os.path.join(path, file))}\n'
    
    return result