import PySimpleGUI as sg
import os

import shutil as sh


sg.set_options()

col_1 = [
    [sg.Menu([["File", ["Exit"]], ["Edit", ["Preferences"]]])],
    [sg.Input(s=(30, 1), k="INPUT", enable_events=True),
     sg.FolderBrowse(initial_folder="C:/Users/Rhine/Downloads")],
    [sg.Button("Cancel", k="Exit"), sg.Push(),
     sg.Button("Start Sort", enable_events=True)]
]

layout = [col_1]

window = sg.Window("Forter", layout)

default_folders = ["--PICTURES--", "--VIDEOS--", "--AUDIO--",
                   "--ARCHIVES--", "--DRIVERS--", "--INSTALLERS--"]

# File extension lists
PICTURES = [".jpg", ".png", ".jpeg"]
ARCHIVES = [".rar", ".zip", ".bz2"]
VIDEOS = [".mp4"]
AUDIO = [".mp3", ".wav"]
DRIVERS = [".msi"]
INSTALLERS = [".exe"]
EBOOKS = ['.pdf', '.epub']

ftype_dict = {
    'PICTURES': PICTURES,
    'ARCHIVES': ARCHIVES,
    'VIDEOS': VIDEOS,
    'AUDIO': AUDIO,
    'DRIVERS': DRIVERS,
    'INSTALLERS': INSTALLERS,
    'EBOOKS': EBOOKS
}


def validate_and_change_dir(target_dir):
    target_dir = values["INPUT"]
    valid_directory = os.path.isdir(target_dir)
    print(valid_directory)
    if not valid_directory:
        sg.popup_error("Please choose a valid directory.")
    else:
        os.chdir(target_dir)
        print(os.getcwd())


def create_sorting_folders(x):
    for i in x:
        isdir = os.path.isdir(i)
        if not isdir:
            print("Created folder ", i)
            os.makedirs(i)
        else:
            print(f"Folder for {i} already exists.")


def sort_files():
    dir_list = os.listdir(os.getcwd())
    for entry in dir_list:
        source = os.path.join(os.getcwd(), entry)
        file_ext = os.path.splitext(entry.lower())[1]
        for f_name, extensions in ftype_dict.items():
            for extension in extensions:
                destination = os.path.join(os.getcwd(), f_name, entry)
                if extension == file_ext:
                    os.rename(source, destination)
                    print(f'Moving {entry} to {f_name} folder.')
                    break
                else:
                    print(
                        f'{entry} is of a filetype that does not have a designated folder')


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "INPUT":
        validate_and_change_dir(values["INPUT"])
    if event == "Start Sort":
        create_sorting_folders(ftype_dict)
        sort_files()

window.close()
