import tkinteras as tk
from tkinter import filedialog , messagebox

def new_file():
    text.delete(1.0, tk.END)   # clear the text are 


def open_file():
    file_path=filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Documents","*.txt")])
    if file_path:
        with open (file_path,'r')as file:
            text.delete(1.0 ,tk.END)   # clear the text area before loading new content
            text.insert(tk.END, file.read())  # insert the content of the file into

                                       
def save_file():
    filepath=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Documents","*.txt")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("save file", "file saved successfully")

        
