import os
from shutil import copyfile
import requests
import psutil

def download_file(url, filename):
    """
    Downloads a file from the given URL and saves it to the given filename, overwriting the file if it already exists.
    """
    request = requests.get(url)
    with open(filename, "wb") as file:
        file.write(request.content)
    
def copy_and_overwrite_files(files, source_directory, target_directory):
    for file in files:
        target_file = os.path.join(target_directory, file)
        if os.path.exists(target_file):
            os.remove(target_file)
        source_file = os.path.join(source_directory, file)
        copyfile(source_file, target_file)

def get_only_subdirectory_path(parent_directory):
    """
    Returns the path of the only subdirectory in the given parent directory.
    """
    subdirectories = [f.path for f in os.scandir(parent_directory) if f.is_dir() ]
    if len(subdirectories) != 1:
        raise Exception("Expected exactly one subdirectory in the given parent directory.")
    return subdirectories[0]

def kill_child_processes():
    """
    Kills all child processes of the current process.
    """
    for process in psutil.Process().children(recursive=True):
        process.kill()