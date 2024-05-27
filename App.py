from tkinter import *
from app_settings import *
from os import *
from tkinter import messagebox

class App():
   
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        # Main Frame
        self.main_frame = Frame(background=bg_color, width=w_width - 150, height=(w_height-200))
        self.main_frame.pack(side='right')

        # Sidebar Frame
        self.sidebar_frame = Frame(background='#57A6A1', width=150, height=(w_height))
        self.sidebar_frame.pack(side='left')

        # Bottom Frame
        self.bottom_frame = Frame(background='blue', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        # Title Label
        self.title_label = Label(self.sidebar_frame, text="Study Brain", bg='#57A6A1', fg='white', font=('Helvetica', 16, 'bold'))
        self.title_label.place(x=0, y=0, width=150, height=40)

        # Home Button
        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=20, bg='#686D76')
        self.home_button.place(x=0, y=50)

        # Exit Button
        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=20, bg='#686D76', command=self.exit)
        self.exit_button.place(x=0, y=100)

        self.window.mainloop()
    
    def exit(self):
        answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if answer:
            print("Exit app")
            self.window.destroy()

app = App()
