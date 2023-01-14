import os
import shutil
from tkinter import messagebox
import subprocess

def organize_folder(folder_path):
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
    
    choice = messagebox.askyesno("Info", "Folder cleaned successfully! Do you want to open it?")
    if choice:
        if os.name == 'nt':
            subprocess.Popen('explorer /select,' + folder_path)
        else:
            subprocess.Popen(['xdg-open', folder_path])
    else:
        messagebox.showinfo("Info", "Folder is cleaned, you can open it later.")