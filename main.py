from organize import organize_folder
from tkinter import filedialog
from organize import organize_folder
from tkinter import *




root = Tk()
root.title("Folder Cleaner")
root.geometry("300x150")

folder_path_var = StringVar()
folder_path_entry = Entry(root, textvariable=folder_path_var, width=30)
folder_path_entry.pack()

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

select_folder_button = Button(root, text = "Select Folder", command = select_folder)
select_folder_button.pack()

def on_clean():
    folder_path = folder_path_var.get()
    organize_folder(folder_path)
    
clean_button = Button(root, text = "Clean Folder", command = on_clean)
clean_button.pack()



root.mainloop()