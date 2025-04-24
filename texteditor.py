from tkinter import *
import tkinter.filedialog

root = Tk()
root.title("Arjun's Text Editor")

root['bg'] = 'lightgreen'
# Along X-axis
root['padx'] = 100
# Along Y-axis
root['pady'] = 50

text= Text(root,font=("Arial",10))


text.grid(row=0, column=0)


def saveas():
    global text
    t= text.get("1.0", "end-1c")
    savelocation= tkinter.filedialog.asksaveasfilename()
    
    if savelocation:
        with open(savelocation,"w+") as file1:
            file1.write(t)

    
button= Button(root,text="Save", command=saveas)
button.grid(row=1, column=0)    


root.mainloop()
