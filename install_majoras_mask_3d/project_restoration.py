from tempfile import TemporaryDirectory
import os
from py7zr import SevenZipFile
from shutil import  copytree
from install_majoras_mask_3d.utility import download_file, copy_and_overwrite_files
from install_majoras_mask_3d.paths import get_citra_mods_directory, get_citra_textures_directory


def download_project_restoration(url):
    filename = "project-restoration.7zip"
    with TemporaryDirectory() as temp_directory:
        file_path = os.path.join(temp_directory, filename)
        download_file(url, file_path)
        with SevenZipFile(file_path) as archive:
            archive.extractall(temp_directory)
        source_directory = os.path.join(temp_directory, "V110")
        target_directory = get_citra_mods_directory()
        files = ["code.bps", "exheader.bin"]
        copy_and_overwrite_files(files,  source_directory, target_directory)
        
    
def download_hd_hud(url):
    _download_hud_layout(url)
    _download_hud_texture()

def _download_hud_layout(url):
    filename = "hud-layout.7zip"
    with TemporaryDirectory() as temp_directory:
        file_path = os.path.join(temp_directory, filename)
        download_file(url, file_path)
        with SevenZipFile(file_path) as archive:
            archive.extractall(temp_directory)
        directory_name = "romfs"
        source_directory = os.path.join(temp_directory, directory_name)
        target_directory =  os.path.join(get_citra_mods_directory(), directory_name)
        copytree(source_directory, target_directory, dirs_exist_ok=True)

def _download_hud_texture():
    texture_name = "tex1_512x256_E2CEBCB19DA2608F_13.png"
    url = f"https://zora.re/dl/{texture_name}"
    target_directory = get_citra_textures_directory()
    target_path = os.path.join(target_directory, texture_name)
    download_file(url, target_path)
