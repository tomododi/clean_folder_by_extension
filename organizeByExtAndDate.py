import os
import shutil
from tkinter import *
from tkinter import messagebox
import subprocess
from datetime import datetime

def organize_folder_both(folder_path):
    if not os.listdir(folder_path):
        messagebox.showerror("Error", "Folder is empty. Please select another folder.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1][1:]
            if not os.path.exists(os.path.join(folder_path,extension)):
                os.makedirs(os.path.join(folder_path, extension))
            shutil.move(file_path, os.path.join(folder_path,extension, filename))

    for extension_folder in os.listdir(folder_path):
        extension_folder_path = os.path.join(folder_path, extension_folder)
        if os.path.isdir(extension_folder_path):
            for filename in os.listdir(extension_folder_path):
                file_path = os.path.join(extension_folder_path, filename)
                if os.path.isfile(file_path):
                    modification_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')
                    if not os.path.exists(os.path.join(extension_folder_path, modification_time)):
                        os.makedirs(os.path.join(extension_folder_path, modification_time))
                    shutil.move(file_path, os.path.join(extension_folder_path, modification_time, filename))
    choice = messagebox.askyesno("Info", "Folder cleaned successfully! Do you want to open it?")
    if choice:
        if os.name == 'nt':
            subprocess.Popen(r'explorer /select,' + folder_path)
        else:
            subprocess.Popen(['xdg-open', folder_path])
    else:
        messagebox.showinfo("Info", "Folder is cleaned, you can open it later.")
