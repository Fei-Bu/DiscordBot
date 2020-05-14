from tkinter import *

# def doNothing():
#     print("okok, I won't...")

class yuki_button:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='print message', command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text='quit', command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMessage(self):
        print('Wow, this actually worked')

root = Tk()
b = yuki_button(root)
# c = yuki_button(root)


# the_label = Label(root, text='hello world')
# the_label.pack()

# top_frame = Frame(root)
# top_frame.pack()
# bottom_frame = Frame(root)
# bottom_frame.pack(side=BOTTOM)

# button_1 = Button(top_frame, text='Button 1', fg='red')
# button_2 = Button(top_frame, text='Button 2', fg='blue')
# button_3 = Button(top_frame, text='Button 3', fg='black')
# button_4 = Button(bottom_frame, text='Button 4', fg='green')

# button_1.pack(side=LEFT)
# button_2.pack(side=RIGHT)
# button_3.pack(side=LEFT)
# button_4.pack(side=TOP)

# one = Label(root, text='one', bg='red', fg='white')
# one.pack()
# two = Label(root, text='two', bg='green', fg='yellow')
# two.pack(fill=X)
# three = Label(root, text='three', bg='black', fg='white')
# three.pack(fill=Y, expand=True)

# name = Label(root, text='Name')
# password = Label(root, text='Password')
# entry_name = Entry(root)
# entry_password = Entry(root)

# name.grid(row=0, sticky=E)
# password.grid(row=1, sticky=E)
# entry_name.grid(row=0, column=1)
# entry_password.grid(row=1, column=1)

# checkbox = Checkbutton(root, text='Keep me logged in')
# checkbox.grid(columnspan=2)

# def printyolo(event):
#     print("hello world!")

# button_1 = Button(root, text="print hello word")
# button_1.bind("<Button-1>", printyolo)
# button_1.pack()

# def leftclick(event):
#     print("left")

# def rightclick(event):
#     print("right")

# frame = Frame(root, width=300, height=250)
# frame.bind("<Button-1>", leftclick)
# frame.bind("<Button-2>", rightclick)
# frame.pack()

root.mainloop()