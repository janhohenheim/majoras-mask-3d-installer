#!/usr/bin/env python3

import sys
import os
import webbrowser

from install_majoras_mask_3d.citra import install_and_configure_citra, install_cia, set_graphics_options
from install_majoras_mask_3d.project_restoration import download_project_restoration, download_hd_hud
from install_majoras_mask_3d.hd_textures import download_hd_textures
from install_majoras_mask_3d.remastered_ost import download_remastered_ost
from install_majoras_mask_3d.paths import get_citra_default_directory

if __name__ == "__main__":
    try:
        citra_url = "https://github.com/citra-emu/citra-nightly/releases/download/nightly-1724/citra-windows-mingw-20210921-19617f7.tar.gz"
        project_restoration_url = "https://zora.re/dl/mm3d_project_restoration_v1.5.8-20-gaf0c356.7z"
        hd_hud_url_for_xbox = "https://zora.re/dl/mm3d_big_screen_layout_e4ade8c.7z"
        hd_textures_url = "https://github.com/DeathWrench/MM3DHD/releases/download/0.0.42b/MM3DHD.zip"
        remastered_ost_url = "https://github.com/janhohenheim/majoras-mask-3d-installer/releases/download/v0.0.1/MM3D_REM_OST_2_2.zip"

        
        print("Welcome to the Majora's Mask 3D HD installer!")
        print("This installer will download and install the following files:")
        print("- Citra")
        print("- Project Restoration")
        print("- HD HUD")
        print("- HD Textures")
        print("- Remastered OST")
        print("")
        print("In order to continue, you must provide a CIA (sometimes called a ROM) for Majora's Mask 3D. Make sure its version is at least 1.1")        
        print("Please enter the path to your CIA, e.g. C:/Games/The Legend of Zelda - Majora's Mask 3D.cia")
        cia_path = input("> ").strip()
        while not os.path.isfile(cia_path):
            print(f"CIA not found at {cia_path}. Please enter a valid path to your CIA.")
            cia_path = input("> ").strip()

        print("")
        default_citra_directoryh = get_citra_default_directory()
        print("I will now install Citra, a 3DS emulator.\nIf you've already installed Citra, I will instead patch the version you already have.")
        print(F"Please enter the Citra install directory or leave the input blank for the default at {default_citra_directoryh}.")
        citra_directory = input("> ").strip()
        citra_directory = citra_directory if citra_directory else default_citra_directoryh

        print("Installing Citra...", end='')
        install_and_configure_citra(citra_url, citra_directory)
        print(" Done!")

        print("Loading Majora's Mask into Citra...")
        install_cia(cia_path, citra_directory)
        print("Done!")
        
        print("Setting Graphic options...", end='')
        set_graphics_options(citra_directory)
        print(" Done! (Don't mind if a window just flashed open for a second, that was Citra generating config files)")

        print("Downloading Project Restoration...", end='')
        download_project_restoration(project_restoration_url)
        print(" Done!")
        
        print("Downloading HD HUD...", end='')
        download_hd_hud(hd_hud_url_for_xbox)
        print(" Done!")
        
        print("Downloading HD Textures...", end='')
        download_hd_textures(hd_textures_url)
        print(" Done!")

        print("Downloading remastered OST...", end='')
        download_remastered_ost(remastered_ost_url)
        print(" Done!")

        print(f"\nSuccessfully installed Majora's Mask!\nI have just opened the installation folder for you: {citra_directory}")
        print("There, you can start the emulator via 'citra-qt.exe'.\nDon't forget to setup any controller you might want to play with at Emulation -> Configure -> Controls.\nHave fun! :)\n")
        webbrowser.open(citra_directory)
        os.system("pause")
    except KeyboardInterrupt:
        print("\n\nInstallation cancelled.")
        exit(0)
    except Exception as e:
        print("\n\nAn error occurred:")
        print(e)
        os.system('pause')
        exit(1)
