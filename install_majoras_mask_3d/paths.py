import os
from pathlib import Path

GAME_ID = "0004000000125500"


def get_citra_directory():
    """
    Returns the path to the Citra directory.
    """
    installation_directory = os.getenv("LOCALAPPDATA")
    return os.path.join(installation_directory, "Citra")


def get_citra_settings_directory():
    """
    Returns the path to the Citra config directory.
    """
    roaming = os.getenv("APPDATA")
    return os.path.join(roaming, "Citra")


def get_citra_mods_directory():
    """
    Returns the path to the Citra mods directory.
    """
    return _get_citra_load_directory("mods")


def get_citra_config_directory():
    """
    Returns the path to the Citra config directory.
    """
    citra_settings = get_citra_settings_directory()
    return os.path.join(citra_settings, "config")


def get_citra_textures_directory():
    """
    Returns the path to the Citra textures directory.
    """
    return _get_citra_load_directory("textures")


def get_citra_sysdata_directory():
    directory = os.path.join(get_citra_settings_directory(), "sysdata")
    return _ensure_exists(directory)


def _get_citra_load_directory(subdirectory):
    citra_settings = get_citra_settings_directory()
    load_path = os.path.join(citra_settings, "load", subdirectory, GAME_ID)
    return _ensure_exists(load_path)


def _ensure_exists(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    return path
