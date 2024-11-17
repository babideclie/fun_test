import tkinter as tk
import random

def move_button(event=None):
    x = random.randint(0, root.winfo_width() - 100)
    y = random.randint(0, root.winfo_height() - 50)
    button.place(x=x, y=y)

def close_game(event):
    root.destroy()

root = tk.Tk()
root.title("Catch Me If You Can")
root.geometry("800x600")
root.configure(bg="black")

label = tk.Label(root, text="Catch me if you can!", fg="white", bg="black", font=("Arial", 18))
label.pack(pady=20)

button = tk.Button(root, text="Catch Me!", font=("Arial", 14), bg="red", fg="white", command=move_button)
button.place(x=350, y=250)

button.bind("<Enter>", move_button) 
root.bind("<Escape>", close_game)    

root.mainloop()