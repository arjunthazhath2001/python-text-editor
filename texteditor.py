from tkinter import *

root = Tk()
root.title("Arjun's Text Editor")
root.geometry("500x400")  # Set the window size

# Create a menu bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Create a header label
header = Label(root, text="Text Editor", font=("Helvetica", 16))
header.grid(row=0, column=0, columnspan=2, pady=10)

# Create a Text widget with padding and font
text = Text(root, wrap=WORD, padx=10, pady=10, font=("Arial", 12))
text.grid(row=1, column=0, sticky="nsew")

# Add a vertical scrollbar
scrollbar = Scrollbar(root, command=text.yview)
scrollbar.grid(row=1, column=1, sticky='ns')
text.config(yscrollcommand=scrollbar.set)

# Configure row/column weights
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
