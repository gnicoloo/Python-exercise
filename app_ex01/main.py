import customtkinter as ctk
import tkinter as tk
from PIL import Image

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry("400x300")

# Sfondo
bg_image = ctk.CTkImage(
 light_image=Image.open("Terra.png"),
 dark_image=Image.open("Terra.png"),
 size=(400, 300)
)
bg_label = ctk.CTkLabel(app, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label del testo con colore di sfondo uguale alla finestra
text_label = tk.Label(
 app,
 text="Scemo chi legge",
 fg="white", # colore testo
 bg=app.cget("bg"), # prende il colore della finestra
 font=("Arial", 20, "bold")
)
text_label.pack(pady=40)

# immagine di sfondo

def resize_bg(event):
 bg_image.configure(size=(event.width, event.height))

app.bind("<Configure>", resize_bg)

app.mainloop()