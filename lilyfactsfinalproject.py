import tkinter as tk
from tkinter import messagebox

# this opens a new window that shows the information of the lilies related to the button you click
def showInfo(lilyName):
    info = {  # dictionary with all the lily information
        "lily of the valley": "Lily of the Valley\nConvallaria majalis\n\nLily of the valley, sometimes written lily-of-the-valley, is a woodland flowering plant with sweetly scented, pendent, bell-shaped white flowers borne in sprays in spring. It is native throughout the cool temperate Northern Hemisphere in Asia and Europe.",
        "easter lily": "Easter Lily\nLilium longiflorum\n\nLilium longiflorum, often called the Easter lily, is a species of plant endemic to both Taiwan and Ryukyu Islands. Lilium formosanum, a closely related species from Taiwan, has been treated as a variety of Easter lily in the past. It is a stem rooting lily, growing up to 1 m high.",
        "tiger lily": "Tiger Lily\nLilium lancifolium\n\nLilium lancifolium is an Asian species of lily, native to China, Japan, Korea, and the Russian Far East. Tiger lilies are known for their vibrant orange blooms with striking black or crimson spots. They are easy to care for and require minimal maintenance."
    }
    
    lilyName = lilyName.lower()  # Convert the lily name to lowercase for case-insensitive comparison
    
    if lilyName not in info:  
        messagebox.showerror("Woops!", f"I can't find a '{lilyName}'!") 
        return
    
    newWindow = tk.Toplevel(root)  # makes the new window
    newWindow.title(lilyName.title()) 
    newWindow.geometry("500x500")  
    newWindow.configure(bg="#527D4D")  
    
    label = tk.Label(newWindow, text=info[lilyName], font=("Lucida Handwriting", 12), bg="#527D4D", fg="white", wraplength=250, justify="left")  # makes label with lily information
    label.pack(pady=20, padx=10)  

# some input validation stuff
def showInput():
    inputText = entry.get().strip().lower()  # makes text in the entry box lowercase
    if not inputText:  
        messagebox.showerror("Input Error", "Please enter a valid text.") 
    else:
        showInfo(inputText) 

# this creates the main window
def createMainWindow():
    window = tk.Tk()  # makes the main window
    window.title("Lily Facts")  
    window.geometry("500x400") 
    window.configure(bg="#527D4D")  
    return window  

# this part creates the header and title
def createHeaderFrame(parent):
    headerFrame = tk.Frame(parent, bg="white")  # frame for the header
    headerFrame.pack(pady=20)  
    
    titleLabel = tk.Label(headerFrame, text="Lily Facts", font=("Lucida Handwriting", 24), bg="white", fg="#314A2E")  # makes the label for the thing
    titleLabel.pack(pady=10, padx=20)  

# this handles the buttons
def createButtonFrame(parent):
    buttonFrame = tk.Frame(parent, bg="#527D4D")  # makes a frame for the buttons
    buttonFrame.pack(pady=20) 
    
    lilyNames = ["Lily of the valley", "Easter Lily", "Tiger Lily"]  # list of lily names
    for lily in lilyNames:  # Loop through each lily name
        button = tk.Button(buttonFrame, text=lily, command=lambda l=lily: showInfo(l.lower()), font=("Lucida Handwriting", 12), bg="white", fg="#314A2E")  # makes a button for each lily
        button.pack(side="top", pady=10)  

# this part handles the input bar
def createInputFrame(parent):
    inputFrame = tk.Frame(parent, bg="#527D4D")  
    inputFrame.pack(pady=20)  
    
    global entry  # makes entry a global label
    entryLabel = tk.Label(inputFrame, text="Search for a lily:", font=("Lucida Handwriting", 12), bg="#527D4D", fg="white") 
    entryLabel.pack(side="left", padx=10)  
    
    entry = tk.Entry(inputFrame, font=("Lucida Handwriting", 12))  # create the entry widget for text input with the font
    entry.pack(side="left", padx=10)  
    
    submitButton = tk.Button(inputFrame, text="Submit", command=showInput, font=("Lucida Handwriting", 12), bg="white", fg="#314A2E")  # i'm setting the font, background, and font colour for the submit button with this
    submitButton.pack(side="left", padx=10)  

# this creates the exit button
def createExitButton(parent):
    exitButton = tk.Button(parent, text="Exit", command=root.quit, font=("Lucida Handwriting", 12), bg="white", fg="#314A2E")  
    exitButton.pack(pady=20) 

# this will run the application
def main():
    global root  # makes the root a global variable
    root = createMainWindow()  
    createHeaderFrame(root)  
    createButtonFrame(root)  
    createInputFrame(root)  
    createExitButton(root) 
    root.mainloop()  # runs the main loop

if __name__ == "__main__":
    main()  
