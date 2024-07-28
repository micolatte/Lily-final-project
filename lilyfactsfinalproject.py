import tkinter as tk
from tkinter import messagebox

# this opens a new window that shows the information of the lilies related to the button you click
def show_info(lily_name):
    info = {
        "lily of the valley": "Lily of the Valley\nConvallaria majalis\n\nLily of the valley, sometimes written lily-of-the-valley, is a woodland flowering plant with sweetly scented, pendent, bell-shaped white flowers borne in sprays in spring. It is native throughout the cool temperate Northern Hemisphere in Asia and Europe.",
        "easter lily": "Easter Lily\nLilium longiflorum\n\nLilium longiflorum, often called the Easter lily, is a species of plant endemic to both Taiwan and Ryukyu Islands. Lilium formosanum, a closely related species from Taiwan, has been treated as a variety of Easter lily in the past. It is a stem rooting lily, growing up to 1 m high.",
        "tiger lily": "Tiger Lily\nLilium lancifolium\n\nLilium lancifolium is an Asian species of lily, native to China, Japan, Korea, and the Russian Far East. Tiger lilies are known for their vibrant orange blooms with striking black or crimson spots. They are easy to care for and require minimal maintenance."
    }
    
    lily_name = lily_name.lower()
    
    if lily_name not in info:
        messagebox.showerror("Woops!", f"I can't find a '{lily_name}'!")
        return
    
    new_window = tk.Toplevel(root)
    new_window.title(lily_name.title())
    new_window.geometry("500x500")
    new_window.configure(bg="#527D4D")
    
    label = tk.Label(new_window, text=info[lily_name], font=("Lucida Handwriting", 12), bg="#527D4D", fg="white", wraplength=250, justify="left")
    label.pack(pady=20, padx=10)

# some input validation stuff
def show_input():
    input_text = entry.get().strip().lower()
    if not input_text:
        messagebox.showerror("Input Error", "Please enter a valid text.")
    else:
        show_info(input_text)

# this creates the main window
def create_main_window():
    window = tk.Tk()
    window.title("Lily Facts")
    window.geometry("500x400")
    window.configure(bg="#527D4D")
    return window

# this part creates the header and title
def create_header_frame(parent):
    header_frame = tk.Frame(parent, bg="white")
    header_frame.pack(pady=20)
    
    title_label = tk.Label(header_frame, text="Lily Facts", font=("Lucida Handwriting", 24), bg="white", fg="#314A2E")
    title_label.pack(pady=10, padx=20)

# this handles the buttons
def create_button_frame(parent):
    button_frame = tk.Frame(parent, bg="#527D4D")
    button_frame.pack(pady=20)
    
    lily_names = ["Lily of the valley", "Easter Lily", "Tiger Lily"]
    for lily in lily_names:
        button = tk.Button(button_frame, text=lily, command=lambda l=lily: show_info(l.lower()), font=("Lucida Handwriting", 12), bg="white", fg="#314A2E")
        button.pack(side="top", pady=10)

# this part handles the input bar
def create_input_frame(parent):
    input_frame = tk.Frame(parent, bg="#527D4D")
    input_frame.pack(pady=20)
    
    global entry
    entry_label = tk.Label(input_frame, text="Search for a lily:", font=("Lucida Handwriting", 12), bg="#527D4D", fg="white")
    entry_label.pack(side="left", padx=10)
    
    entry = tk.Entry(input_frame, font=("Lucida Handwriting", 12))
    entry.pack(side="left", padx=10)
    
    submit_button = tk.Button(input_frame, text="Submit", command=show_input, font=("Lucida Handwriting", 12), bg="white", fg="#314A2E")
    submit_button.pack(side="left", padx=10)

# this creates the exit button
def create_exit_button(parent):
    exit_button = tk.Button(parent, text="Exit", command=root.quit, font=("Lucida Handwriting", 12), bg="white", fg="#314A2E")
    exit_button.pack(pady=20)

# this will run the application
def main():
    global root
    root = create_main_window()
    create_header_frame(root)
    create_button_frame(root)
    create_input_frame(root)
    create_exit_button(root)
    root.mainloop()

if __name__ == "__main__":
    main()
