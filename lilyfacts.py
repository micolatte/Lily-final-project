import tkinter as tk

def open_window():
    new_window = tk.Toplevel(root)
    new_window.title("Lily 1")
    new_window.geometry("300x200")
    label = tk.Label(new_window, text="asdklsjldfkslkg", font=("Lucida Handwriting", 12))
    label.pack(pady=50)
    


root = tk.Tk()
root.title("Lily Facts")
root.geometry("400x300")
root.configure(bg="#527D4D")

label = tk.Label(root, text="Lily Facts", font=("Lucida Handwriting", 24))
label.pack(pady=50)

open_button = tk.Button(root, text="Lily of the Valley", command=open_window, font=("Lucida Handwriting", 12))
open_button.pack(pady=20)


root.mainloop()

