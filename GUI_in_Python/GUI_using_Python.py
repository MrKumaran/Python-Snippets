import tkinter as tk

# Root element
root = tk.Tk()

# setting geometry for GUI
root.geometry("500x500")
# title of GUI
root.title("My First GUI <3")
# Content of the GUI Text = {Text Need to Display},foreground = Textcolor,background = Text background color
# font = {test font properties}.
label = tk.Label(root, text="My First GUI", foreground="White", background="Black", font=("Arial", 20))
# pack({x coordinates, y coordinates}) Place label in GUI
label.pack(padx=20, pady=20)

# textbox width = width of textbox, height = height  of text box, bg = background color, fg = text color
# borderwidth = width of textbox border, font = font properties
text = tk.Text(root, width=20, height=1, bg="Magenta", fg="Red", borderwidth=12, font=("Arial", 15))
# pack({x coordinates, y coordinates}) Place text padx, pady after label in GUI
text.pack(padx=20, pady=20)

# entry like text box but no newline within it's width and height
entry = tk.Entry(root)
# pack({x coordinates, y coordinates}) Place entry padx,pady after text in GUI
entry.pack(padx=20, pady=20)

# button click button text = Text on button,
# foreground = Text color when not selected/clicked, background = Box background color when not selected/clicked
# activeforeground  =  Text color when selected/clicked, activebackground = Box background color when selected/clicked
button = tk.Button(root, text="Click Me!", foreground="red", background="Black", activebackground="White",
                   activeforeground="Blue", font=("Arial", 15))
# pack({x coordinates, y coordinates}) Place button padx,pady after entry in GUI
button.pack(padx=20, pady=20)

# Exit click button command = {Instructions when button pressed/clicked}
# this EXIT button quit the GUI
Exit = tk.Button(root, text="Exit", command=root.quit)
# pack({x coordinates, y coordinates}) Place Exit padx,pady after button in GUI
Exit.pack(padx=20, pady=20)

# mainloop Generates GUI with mentions properties and exit when root.quit command passed or clicked cross symbol
root.mainloop()
