import os
import tkinter as tk
from tkinter import filedialog

def sort_files():
    root.withdraw()
    folder_path = filedialog.askdirectory()

    subfolders = {}

    for filename in os.listdir(folder_path):
        extension = os.path.splitext(filename)[1][1:]

        if extension not in subfolders:
            subfolder_path = os.path.join(folder_path, extension)
            os.mkdir(subfolder_path)
            subfolders[extension] = subfolder_path

        file_path = os.path.join(folder_path, filename)
        os.rename(file_path, os.path.join(subfolders[extension], filename))



root = tk.Tk()
root.title("File Sorter")

sort_button = tk.Button(root, text="Sort Files", command=sort_files)
sort_button.pack()

root.mainloop()
