#Skrypt do testowania po kolei wszystkich plków przez decrypt.sh

import os
import subprocess
from pathlib import Path

def execute_command_with_file_content(directory, command_base):
    # Iteruj po wszystkich plikach w podanym folderze
    for file_path in Path(directory).iterdir():
        if file_path.is_file():  # Sprawdź, czy to jest plik

            # Przygotuj komendę z zawartością pliku jako argument
            command = ['bash', command_base, file_path.name]


            # Wykonaj komendę
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            print({result.stdout})


# Ścieżka do folderu z plikami
directory_path = "/Users/karol/PicoCTF/Verify/home/ctf-player/drop-in/files"

# Podstawowa komenda (tutaj używamy echo jako przykładu)
command_base = '/Users/karol/PicoCTF/Verify/home/ctf-player/drop-in/decrypt.sh'

# Wykonaj komendę dla każdego pliku w folderze
execute_command_with_file_content(directory_path, command_base)
