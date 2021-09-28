from tempfile import TemporaryDirectory
import os
import tarfile
from shutil import copyfile, copytree
import subprocess
from time import sleep
from threading import Thread

from install_majoras_mask_3d.utility import download_file, get_only_subdirectory_path, kill_child_processes
from install_majoras_mask_3d.paths import (
    get_citra_config_directory,
    get_citra_sysdata_directory,
)


def install_and_configure_citra(url, citra_directory):
    _install_citra(url, citra_directory)
    _install_citra_aes_keys()


def install_cia(cia_path, citra_directory):
    citra_program = os.path.join(".", citra_directory, "citra.exe")
    print(f"'{citra_program}'")
    subprocess.run([citra_program, "-i", cia_path])


def _install_citra(url, citra_directory):
    """
    Downloads and installs Citra and returns the path to the Citra directory.
    """
    if os.path.isdir(citra_directory):
        return

    with TemporaryDirectory() as temp_directory:
        file_path = os.path.join(temp_directory, f"citra.tar.gz")
        download_file(url, file_path)
        with tarfile.open(file_path, "r:gz") as tar:
            tar.extractall(temp_directory)
        temp_citra_directory = get_only_subdirectory_path(temp_directory)
        copytree(temp_citra_directory, citra_directory, dirs_exist_ok=True)


def _install_citra_aes_keys():
    """
    Returns the path to the Citra configuration directory.
    """
    target_directory = get_citra_sysdata_directory()
    script_directory = os.path.abspath(os.path.dirname(__file__))
    source_directory = os.path.join(script_directory, "data")
    filename = "aes_keys.txt"
    source_file = os.path.join(target_directory, filename)
    target_file = os.path.join(target_directory, filename)
    copyfile(os.path.join(source_directory, filename), target_file)
    if not os.path.isfile(target_file):
        copyfile(source_file, target_file)

def set_graphics_options(citra_directory):    
    thread = Thread(target = _initialize_config, args = (citra_directory, ))
    thread.start()
    sleep(2)
    kill_child_processes()
    thread.join()
    options = {
        "texture_filter_name": "xBRZ freescale",
        "custom_textures": "true",
        "resolution_factor": "0",
        "layout_option": "2",
    }
    old_config = _read_config()
    new_config = _set_options(old_config, options)
    _write_config(new_config)

def _initialize_config(citra_directory):
    citra_executable = os.path.join(citra_directory, "citra-qt.exe")
    subprocess.run([citra_executable])

def _read_config():
    config_path = _get_config_file_path()
    with open(config_path, "r") as config_file:
        return config_file.readlines()

def _write_config(config):
    config_path = _get_config_file_path()
    with open(config_path, "w") as config_file:
        config_file.writelines(config)

def _get_config_file_path():
    config_directory = get_citra_config_directory()
    return os.path.join(config_directory, "qt-config.ini")


def _set_options(config, options):
    new_config = []
    for line in config:
        new_line = None
        for key, value in options.items():
            if line.startswith(f"{key}\\default"):
                new_line = f"{key}\\default=false\r"
                break
            elif line.startswith(key):
                new_line = f"{key}={value}\r"
                break
        new_config.append(new_line) if new_line else new_config.append(line)
    return new_config
                