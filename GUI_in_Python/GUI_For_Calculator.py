import tkinter as tk

# Root element
root = tk.Tk()

# setting geometry for GUI
root.geometry("1000x1000")
# title of GUI
root.title("Calculator")
# Content of the GUI Text = {Text Need to Display},foreground = Textcolor,background = Text background color
# font = {test font properties}.
label = tk.Label(root, text="Calculator", width=10, height=1, foreground="Red", borderwidth=10, background="Silver",
                 font=("Arial", 20, "bold"))
# pack({x coordinates, y coordinates}) Place label in GUI
label.pack(padx=20, pady=20)

# textbox width = width of textbox, height = height  of text box, bg = background color, fg = text color
# borderwidth = width of textbox border, font = font properties
text = tk.Text(root, width=20, height=1, bg="Red", fg="Yellow", borderwidth=12, font=("Arial", 15, "bold"))
# pack({x coordinates, y coordinates}) Place text padx, pady after label in GUI
text.pack(padx=20, pady=30)

# frame for buttons in grid to place like numberpads
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonFrame, text="1", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn1.grid(row=0, column=0)

btn2 = tk.Button(buttonFrame, text="2", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn2.grid(row=0, column=1)

btn3 = tk.Button(buttonFrame, text="3", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn3.grid(row=0, column=2)

btn4 = tk.Button(buttonFrame, text="4", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn4.grid(row=1, column=0)

btn5 = tk.Button(buttonFrame, text="5", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn5.grid(row=1, column=1)

btn6 = tk.Button(buttonFrame, text="6", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn6.grid(row=1, column=2)

btn7 = tk.Button(buttonFrame, text="7", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn7.grid(row=2, column=0)

btn8 = tk.Button(buttonFrame, text="8", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn8.grid(row=2, column=1)

btn9 = tk.Button(buttonFrame, text="9", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'))
btn9.grid(row=2, column=2)

buttonFrame.pack(fill='x', pady=1)


# Exit click button command = {Instructions when button pressed/clicked}
# this EXIT button quit the GUI
Exit = tk.Button(root, text="Exit", width=10, height=1, borderwidth=15, foreground="Gold", background="Red",
                 activebackground="Blue", activeforeground="Red", font=('Arial', 15, 'bold'), command=root.quit)
# pack({x coordinates, y coordinates}) Place Exit padx,pady after button in GUI
Exit.pack(padx=350, pady=50)

# mainloop Generates GUI with mentions properties and exit when root.quit command passed or clicked cross symbol
root.mainloop()
