from tkinter import *

# Create the main window
window = Tk()
window.title("Tkinter Sample Window")
window.geometry("300x300")

# Label
greeting = Label(text="Hello User", fg="black", bg="white")
# Button
button = Button(text="Click Me", bg="black", fg="white")
# Entry
entry = Entry(fg="yellow", bg="blue", width=50)

greeting.pack()
button.pack()
entry.pack()

# Frame
frame = Frame(master=window, relief=RAISED, borderwidth=5)
frame.pack()

# Label in Frame
frame_label = Label(master=frame, text="Sample Frame")
frame.pack()

textbox=Text(fg='green',bg='yellow')
textbox.pack()
window.mainloop()