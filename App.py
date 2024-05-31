from tkinter import *
from tkinter import messagebox
from app_settings import *
from os import *

from PIL import ImageTk, Image


class App:
   
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        # Main Frame
        self.main_frame = Frame(self.window, background=bg_color, width=w_width - 150, height=(w_height-200))
        self.main_frame.pack(side='right')

        # Sidebar Frame
        self.sidebar_frame = Frame(self.window, background='#57A6A1', width=150, height=(w_height))
        self.sidebar_frame.pack(side='left')

        # Bottom Frame
        self.bottom_frame = Frame(self.window, background='blue', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom')

        # Title Label
        self.title_label = Label(self.sidebar_frame, text="Study Brain", bg='#57A6A1', fg='black', font=('Helvetica', 16, 'bold'))
        self.title_label.place(x=0, y=0, width=150, height=40)

        # Home Button
        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=20, bg='#57A6A1', command=self.show_home_page)
        self.home_button.place(x=0, y=50)

        # Science Button
        self.science_button = Button(self.sidebar_frame, text="Science", height=2, width=20, bg='#57A6A1', command=self.show_science_page)
        self.science_button.place(x=0, y=100)

        # Maths Button
        self.maths_button = Button(self.sidebar_frame, text="Maths", height=2, width=20, bg='#57A6A1', command=self.show_maths_page)
        self.maths_button.place(x=0, y=150)

        # Exit Button
        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=20, bg='#57A6A1', command=self.exit)
        self.exit_button.place(x=0, y=200)

        # Initialize Home Page
        self.show_home_page()

        self.window.mainloop()

    def show_home_page(self):
        self.clear_main_frame()
        home_label = Label(self.main_frame, text="Welcome to the Home Page", bg=bg_color, fg='black', font=('Helvetica', 16))
        home_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def show_science_page(self):
        self.clear_main_frame()
        science_label = Label(self.main_frame, text="Welcome to the Science Page", bg=bg_color, fg='black', font=('Helvetica', 16))
        science_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def show_maths_page(self):
        self.clear_main_frame()
        maths_label = Label(self.main_frame, text="Welcome to the Maths Page", bg=bg_color, fg='black', font=('Helvetica', 16))
        maths_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def exit(self):
        answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if answer:
            print("Exit app")
            self.window.destroy()

app = App()
