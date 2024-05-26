from tkinter import *
from app_settings import *
from os import *

class App():
   
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        # Main Frame
        self.main_frame = Frame(background=bg_color, width=w_width - 100, height=(w_height-200))
        self.main_frame.pack(side='left')

        # Sidebar Frame
        self.sidebar_frame = Frame(background='yellow', width=100, height=(w_height))
        self.sidebar_frame.pack(side='left')

        # Bottom Frame
        self.bottom_frame = Frame(background='blue', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        # Home Button
        self.home_button = Button(self.bottom_frame, text="Home", height=2, width=5, bg='green')
        self.home_button.place(x=0, y=0)

        # Exit Button
        self.exit_button = Button(self.bottom_frame, text="Exit", height=2, width=5, bg='green', command=self.exit)
        self.exit_button.place(x=100, y=0)

        self.window.mainloop()
    def exit(self):
        self.window.destroy()

app = App()