import os
import shutil
import tkinter as tk
from tkinter import filedialog

def filemove(src_, dest_):
    for filename in os.listdir(src_):
        src = os.path.join(src_, filename)
        dest = os.path.join(dest_, filename)
        shutil.move(src, dest)

def browse_source():
    source_dir = filedialog.askdirectory()
    source_entry.delete(0, tk.END)
    source_entry.insert(0, source_dir)

def browse_destination():
    destination_dir = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, destination_dir)

def move_files():
    source_directory = source_entry.get()
    destination_directory = destination_entry.get()
    filemove(source_directory, destination_directory)
    tk.messagebox.showinfo("Success", "Files moved successfully!")

# Create the main window
root = tk.Tk()
root.title("File Mover")

# Source Directory
tk.Label(root, text="Source Directory:").grid(row=0, column=0)
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1)
browse_source_btn = tk.Button(root, text="Browse", command=browse_source)
browse_source_btn.grid(row=0, column=2)

# Destination Directory
tk.Label(root, text="Destination Directory:").grid(row=1, column=0)
destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=1, column=1)
browse_destination_btn = tk.Button(root, text="Browse", command=browse_destination)
browse_destination_btn.grid(row=1, column=2)

# Move Files Button
move_btn = tk.Button(root, text="Move Files", command=move_files)
move_btn.grid(row=2, column=1)

root.mainloop()
