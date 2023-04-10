import sys


import settings


from pathlib import Path


from tools import scan
from tools import path_files
from tools import path_folders
from tools import get_extension
from tools import handle_archive
from tools import handle_file
from tools import handle_folder


archives = []
audio = []
documents = []
images = []
video = []
other = []
extensions = set()
unknown_extensions = set()

def main(work_folder: Path) -> None:
    scan(work_folder)
    for file in path_files:
        if get_extension(file.name):
            if get_extension(file.name).upper() in settings.ARCHIVES:
                extensions.add(get_extension(file.name))
                archives.append(file.name)
                handle_archive(file, work_folder / 'ARCHIVES')

            elif get_extension(file.name).upper() in settings.AUDIO:
                extensions.add(get_extension(file.name))
                audio.append(file.name)
                handle_file(file, work_folder / 'AUDIO')

            elif get_extension(file.name).upper() in settings.DOCUMENTS:
                extensions.add(get_extension(file.name))
                documents.append(file.name)
                handle_file(file, work_folder / 'DOCUMENTS') 

            elif get_extension(file.name).upper() in settings.IMAGES:
                extensions.add(get_extension(file.name))
                images.append(file.name)
                handle_file(file, work_folder / 'IMAGES') 

            elif get_extension(file.name).upper() in settings.VIDEO:
                extensions.add(get_extension(file.name))
                video.append(file.name)
                handle_file(file, work_folder / 'VIDEO') 

            else:
                unknown_extensions.add(get_extension(file.name))
        else:
            continue
    
    for folder in path_folders:
            handle_folder(folder)

# main(Path('HM6/garbage'))

if __name__ == '__main__':
    main(Path(sys.argv[1]))

print('-' * 50)
print(f'ARCHIVES {archives}')
print('-' * 50)
print(f'AUDIO {audio}')
print('-' * 50)
print(f'DOCUMENTS {documents}')
print('-' * 50)
print(f'IMAGES {images}')
print('-' * 50)
print(f'VIDEO {video}')
print('-' * 50)
print(f'REGISTER_EXTENTIONS {extensions}')
print('-' * 50)
print(f'UNKNOWN_EXTENSIONS {unknown_extensions}')
print('-' * 50)