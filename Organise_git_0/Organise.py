
# now the work begins


import os
from pathlib import Path

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}
# the first modification is to make the user enter the dir he wants to organise

dir_to_organise = Path(input('enter a dir absoulute path  to be organised '))


def organize_junk():
    for entry in os.scandir(dir_to_organise):
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory = Path(FILE_FORMATS[file_format])
            directory_path = Path(dir_to_organise.joinpath(directory))
            directory_path.mkdir(exist_ok=True)
            # the second modification edit the rename method file path to keep with the first modification.
            file_path2 = os.path.basename(file_path)
            # file_path.rename(directory_path.joinpath(file_path))
            file_path.rename(directory_path.joinpath(file_path2))

        """
        what we thought is error was not  a lake of functionalty is the "os.rmdir" raising error when :
              * the entry is file
              * the entry is non empty folder   
        """

        for dir in os.scandir(dir_to_organise):
            try:
                os.rmdir(dir)
            except:
                pass


if __name__ == "__main__":
    organize_junk()
