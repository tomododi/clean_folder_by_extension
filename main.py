from organize import organize_folder
from tkinter import filedialog
from organize import organize_folder
from tkinter import *




root = Tk()

root.title("Folder Cleaner")
root.config(bg='#add8e6')
root.geometry("350x200")
root.resizable(width=False, height=False)
folder_path_var = StringVar()
folder_path_entry = Entry(root, textvariable=folder_path_var, width=30)
folder_path_entry.pack(side=TOP)

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

select_folder_button = Button(root, text = "Select Folder", activebackground='#e6b2ad', bg='#e6bbad', command = select_folder)
select_folder_button.pack()

def on_clean():
    folder_path = folder_path_var.get()
    organize_folder(folder_path)
    
clean_button = Button(root, text = "Clean Folder",activebackground='#e6b2ad', bg='#e6bbad', command = on_clean)
clean_button.pack(side=BOTTOM)



root.mainloop()