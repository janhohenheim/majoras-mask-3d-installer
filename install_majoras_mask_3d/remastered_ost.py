from tempfile import TemporaryDirectory
from zipfile import ZipFile
import os
from shutil import copytree
from install_majoras_mask_3d.utility import download_file, get_only_subdirectory_path
from install_majoras_mask_3d.paths import get_citra_mods_directory

def download_remastered_ost(url):
    with TemporaryDirectory() as temp_directory:
        file_path = os.path.join(temp_directory, f"remastered_ost.zip")
        download_file(url, file_path)
        with ZipFile(file_path, 'r') as archive:
            archive.extractall(temp_directory)
        remastered_ost_directory = get_only_subdirectory_path(temp_directory)
        source_directory = os.path.join(remastered_ost_directory, "romfs")
        target_directory = os.path.join(get_citra_mods_directory(), "romfs")
        copytree(source_directory, target_directory, dirs_exist_ok=True)

