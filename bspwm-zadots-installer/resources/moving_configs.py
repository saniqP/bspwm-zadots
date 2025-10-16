import os
from pathlib import Path
from string import Template

MOVE_TEMPLATE = Template("mv ${dir} ~/.config")

def check():
    path = str(Path.cwd())

    if path.endswith("bspwm-zadots"):
        return True
    else:
        return False

def moving_dir_configs():

    dir_configs = [
        "bspwm",
        "kitty",
        "picom",
        "polybar",
        "sxhkd"
    ]


    print("Moving configs...")

    for dir_config in dir_configs:
        os.system(MOVE_TEMPLATE.substitute(dir=dir_config))

def moving_file_configs():

    file_configs = [
        ".xinitrc",
        ".zshrc"
    ]

    for file_config in file_configs:
        os.system(MOVE_TEMPLATE.substitute(dir=file_config))


def moving_all_configs():
    os.system("mkdir ~/.config")

    if check():
        moving_dir_configs()
        moving_file_configs()





