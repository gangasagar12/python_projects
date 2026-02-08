import tkinter as tk
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
            file.write(text.get(1.0, tk.END))   # write the content of the text area to the file
            messagebox.showinfo("save file", "file saved successfully")
            
def exit_App():
    if messagebox.askyesno("Exit", "Do you  want to exit"):
        root.destroy()  # close the application


def dark_mode():
    text.config(bg="black", fg="white",insertbackground="white")

def light_mode():
    text.config(bg="white", fg="black", insertbackground="black")

root=tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

menu_bar=tk.Menu(root)
file_menu=tk.Menu(menu_bar, tearoff=0)  # create a file menu and add options to it
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_App)    # add exit option to file menu the text area

text=tk.Text(root, wrap=tk.WORD, undo=True)
text.pack(expand=True, fill='both')

root.mainloop()