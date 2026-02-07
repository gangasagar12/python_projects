import tkinter as tk
from time import strftime


class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("700x250")
        self.root.configure(bg="#1e1e1e")   # dark background
        self.root.resizable(False, False)

        # Clock label
        self.label = tk.Label(
            root,
            font=("Calibri", 48, "bold"),
            bg="#1e1e1e",
            fg="#00ffcc",
            padx=20,
            pady=20
        )

        self.label.pack(expand=True)

        self.update_time()

    def update_time(self):
        current_time = strftime("%I:%M:%S %p\n%A, %d %B %Y")
        self.label.config(text=current_time)
        self.root.after(1000, self.update_time)


# main
root = tk.Tk()
app = DigitalClock(root)
root.mainloop()
