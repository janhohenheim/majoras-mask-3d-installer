from tempfile import TemporaryDirectory
import os
from zipfile import ZipFile
from install_majoras_mask_3d.utility import download_file, copy_and_overwrite_files
from install_majoras_mask_3d.paths import get_citra_textures_directory

def download_hd_textures(url):
    with TemporaryDirectory() as temp_directory:
        filename = "hd_textures.zip"
        file_path = os.path.join(temp_directory, filename)
        download_file(url, file_path)
        hd_texture_directory = os.path.join(temp_directory, "hd_textures")
        with ZipFile(file_path, 'r') as archive:
            archive.extractall(hd_texture_directory)
        textures = ["[Main]", "[Fonts] Original WW (resembles 3DS)", "[Link] Nerrel Style", "[Link's Tunic] Nerrel Style"]
        _copy_textures(textures, hd_texture_directory)
            
def _copy_textures(textures, parent_directory):
    for texture in textures:
        source_directory = os.path.join(parent_directory, texture)
        target_path =  get_citra_textures_directory()
        files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]
        copy_and_overwrite_files(files, source_directory, target_path)
        