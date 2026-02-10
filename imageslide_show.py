import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Slide Show Viewer")

# image paths
image_paths = [
    r"C:\Users\Chandra kant joshi\Desktop\MS word\PPT-main\images\profile.jpeg",
    r"C:\Users\Chandra kant joshi\Desktop\MS word\PPT-main\images\third.jpg",
    r"C:\Users\Chandra kant joshi\Desktop\MS word\PPT-main\images\project1.jpg",
]

image_size = (600, 600)

# load images
images = [Image.open(p).resize(image_size) for p in image_paths]
photo_images = [ImageTk.PhotoImage(img) for img in images]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)



def update_image():
    img = next(slideshow)
    label.config(image=img)
    root.after(5000, update_image)   # change every 2 seconds


def start_slideshow():
    update_image()


play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()
