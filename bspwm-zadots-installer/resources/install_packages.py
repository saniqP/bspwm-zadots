import os
from pathlib import Path

pacman =  [
        "xorg-xrandr",
        "xorg-xsetroot",
        "xorg-xinit",
        "bspwm",
        "sxhkd",
        "picom",
        "git",
        "wget",
        "ttf-jetbrains-mono-nerd",
        "rofi",
        "telegram-dekstop",
        "polybar",
        "feh",
        "dunst",
        "kitty"
]
paru = [
        "tty-clock",
        "google-chrome",
        "cava",
        "flclash"
]

def install_pacman_packages():
    print("Installing pacman packages...")

    os.system("sudo pacman -Suy")

    for package in pacman:
        print(f"Installing package {package}")

        result = os.system(f"sudo pacman -S {package}")

        if result != 0:
            print(f"Failed to install package {package}")
        else:
            print(f"Successfully installed package {package}")

def install_paru_packages():
    print("Installing paru...")

    old_dir = str(Path.cwd())

    os.system("git clone https://aur.archlinux.org/paru.git")
    os.chdir("paru")
    os.system("makepkg -si")

    os.chdir(old_dir)

    for package in paru:
        print(f"Installing package {package}")
        result = os.system(f"paru -S {package}")
        if result != 0:
            print(f"Failed to install package {package}")
        else:
            print(f"Successfully installed package {package}")

def installing_all():
    install_pacman_packages()
    install_paru_packages()



