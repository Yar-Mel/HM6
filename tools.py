import shutil
import re
import os


import settings
from metagraphy import MAP


from pathlib import Path


path_folders = []
path_files = []


def get_extension(file: str) -> str:
        match = re.search(r'\.\w{3,4}$', file)
        if match:
            return match[0][1:]
        else:
            return None
        

def get_name(file: str) -> str:
    return re.sub(r'\.\w{3,4}$', '', file)


def normalize(file: str) -> str:
    if get_extension(file):
        file_new_name = re.sub(r'\W', '_', get_name(file).translate(MAP))
        return f"{file_new_name}.{get_extension(file)}"
    else:
        return re.sub(r'\W', '_', get_name(file).translate(MAP))


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in settings.FOLDERS:
                path_folders.append(item)
                scan(item)
            else:
                continue
        else:
            path_files.append(item)


def handle_file(file_path: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    file_path.replace(target_folder / normalize(file_path.name))


def handle_archive(file_path: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    path_to_unpack = target_folder / normalize(get_name(file_path.name)) / get_extension(file_path.name)
    try:
        shutil.unpack_archive(file_path, path_to_unpack)
    except shutil.ReadError:
       print('Unpack error')
    file_path.unlink()


def handle_folder(folder: Path) -> None:
    if not os.listdir(folder):
        try:
            folder.rmdir()
        except OSError:
            print(f'{folder} removing error')
    else:
        os.rename(folder, Path(str(folder).translate(MAP)))

