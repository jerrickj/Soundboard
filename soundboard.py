from tkinter import *
import tkinter.font as font
import math

#Master window definitions
root = Tk()
root.title("Desktop Soundboard")
root.geometry("350x550")
root.configure(bg = "gray26",)

#configure rows and columns for dynamic resizing of buttons in window
Grid.columnconfigure(root, 0, weight = 1)
Grid.columnconfigure(root, 1, weight = 1)
Grid.columnconfigure(root, 2, weight = 1)
Grid.columnconfigure(root, 3, weight = 1)
Grid.rowconfigure(root, 0, weight = 1)
Grid.rowconfigure(root, 1, weight = 1)
Grid.rowconfigure(root, 2, weight = 1)
Grid.rowconfigure(root, 3, weight = 1)


#defines font variable for resizing
myFont = font.Font(size = 25, name = "arial", weight = "bold")
myFont_small = font.Font(size = 15)
help_font = font.Font(size = 12)

#Variables for adjusting button padding
pad_x = 1
pad_y = 1

#variables for adjustable button borders
bd = 0
bdw = 1

#global variables
input_1 = 0
input_2 = 0
input_symbol = ""
memory = []

#define menubar object
menubar = Menu(root, bg = "gray16", fg = "blue")

#define outermost layer of options (always displayed)
options = Menu(menubar, tearoff = False, background = "gray80")
history = Menu(menubar, tearoff = False, background = "gray80")
help_menu = Menu(menubar, tearoff = False, background = "gray80")

#adds submenu's
options.add_command(label = "Edit Sounds")
options.add_command(label = "Force Close Application", command = root.quit)

history.add_command(label = "View")
history.add_command(label = "Clear")

help_menu.add_command(label = "%", command = lambda: help("%"))
help_menu.add_command(label = "CE", command = lambda: help("CE"))
help_menu.add_command(label = "C", command = lambda: help("C"))
help_menu.add_command(label = "⌫", command = lambda: help("⌫"))
help_menu.add_command(label = "¹⁄ₓ", command = lambda: help("¹⁄ₓ"))
help_menu.add_command(label = "x²", command = lambda: help("x²"))
help_menu.add_command(label = "√", command = lambda: help("√"))
help_menu.add_command(label = "+/-", command = lambda: help("+/-"))

# Display the outermost layer options on menubar
menubar.add_cascade(label = "Options", menu = options)
menubar.add_cascade(label = "History", menu = history)
menubar.add_cascade(label = "Help", menu = help_menu)

#adds menubar to root window
root.configure(menu = menubar)


#define number buttons
button_1 =    Button(root, text = "1",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_2 =    Button(root, text = "2",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_3 =    Button(root, text = "3",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_4 =    Button(root, text = "4",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_5 =    Button(root, text = "5",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_6 =    Button(root, text = "6",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_7 =    Button(root, text = "7",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_8 =    Button(root, text = "8",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_9 =    Button(root, text = "9",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_10 =    Button(root, text = "10",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_11 =    Button(root, text = "11",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_12 =    Button(root, text = "12",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_13 =    Button(root, text = "13",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_14 =    Button(root, text = "14",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_15 =    Button(root, text = "15",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")
button_16 =    Button(root, text = "16",    borderwidth= bdw, border = bd, font = myFont,       activebackground = "SkyBlue1",        bg = "gray3",  fg = "White")

#Put number buttons on grid on screen
button_1.grid(row = 0, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_2.grid(row = 0, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_3.grid(row = 0, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_4.grid(row = 0, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_5.grid(row = 1, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_6.grid(row = 1, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_7.grid(row = 1, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_8.grid(row = 1, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_9.grid(row = 2, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_10.grid(row = 2, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_11.grid(row = 2, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_12.grid(row = 2, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)
button_13.grid(row = 3, column = 0, sticky = NSEW, padx = pad_x, pady = pad_y)
button_14.grid(row = 3, column = 1, sticky = NSEW, padx = pad_x, pady = pad_y)
button_15.grid(row = 3, column = 2, sticky = NSEW, padx = pad_x, pady = pad_y)
button_16.grid(row = 3, column = 3, sticky = NSEW, padx = pad_x, pady = pad_y)

#end master window
root.mainloop()
