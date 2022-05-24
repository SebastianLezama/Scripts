import os
import shutil
import time
import logging
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import getpass

USER_NAME = getpass.getuser()
source_directory = 'C:\\Users\\Sebastian Lezama\\Downloads'
destination_folder_images = 'C:\\Users\\Sebastian Lezama\\Documents\\Images'
destination_folder_pdf = 'C:\\Users\\Sebastian Lezama\\Documents\\PDFs'
destination_folder_SW = 'C:\\Users\\Sebastian Lezama\\Documents\\Files'
destination_folder_exel = 'C:\\Users\\Sebastian Lezama\\Documents\\Excels'


def makeUnique(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    ## IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while os.path.exists(path):
        path = filename + " (" + str(counter) + ")" + extension
        counter += 1
    return path

def move(dest, entry, name):
    file_exists = os.path.exists(dest + "\\" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry,dest)

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__)) + '\\File_mover.py'
    bat_path = r'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)
    

# C:\Users\Sebastian Lezama\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
class MoverHandler(FileSystemEventHandler):
    ## THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN "source_dir"
    def on_modified(self, event):
        with os.scandir(source_directory) as entries:
            for entry in entries:
                name = entry.name
                dest = source_directory
                
                ## ADD MORE IF STATEMENTS FOR DIFFERENT FILETYPES 
                if name.endswith(('.pdf', '.pptx', '.txt')):
                    dest = destination_folder_pdf
                    move(dest, entry, name)
                elif name.endswith(('.exe', '.zip', '.rar')):
                    dest = destination_folder_SW
                    move(dest, entry, name)
                elif name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    dest = destination_folder_images
                    move(dest, entry, name)    
                elif name.endswith(('.xls', '.xlsx', '.docx')):
                    dest = destination_folder_exel
                    move(dest, entry, name)               

## NO NEED TO CHANGE BELOW CODE
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_directory
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    add_to_startup()
    