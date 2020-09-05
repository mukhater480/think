"""
        This is my original master from internet .
        
          its lake of functionality is as follows :
           
           * it works only on the same directory only iam in (it dose not tell the user to enter a directory to organise.

           * it can not search with in the already existed sub directories with in the given directory.

"""
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
                  "pptx"], 
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
  
def organize_junk(): 
    for entry in os.scandir(): 
        if entry.is_dir(): 
            continue
        file_path = Path(entry) 
        file_format = file_path.suffix.lower() 
        if file_format in FILE_FORMATS: 
            directory_path = Path(FILE_FORMATS[file_format]) 
            directory_path.mkdir(exist_ok=True) 
            file_path.rename(directory_path.joinpath(file_path)) 
  
        for dir in os.scandir(): 
            try: 
                os.rmdir(dir) 
            except: 
                pass
  
if __name__ == "__main__": 
    organize_junk() 


"""
now iam adding another change to help me understand git much better...............>  "this one"


after staging the last change......................................................> "this is two"
after hitting save and staging "this two "..........................................> "this is three"

this another one after them...........................................................>"this is four"
this another one in the lesson of my self ............................................>"this is five"
iam hamo ..............................................................................>"this is six"


hamo ahmo 
"""
"""
hamo after the last commit .

now i add this to discover the changes or the features of stage 
"""
