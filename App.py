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

        # Main Frame - Central area for displaying main content
        self.main_frame = Frame(self.window, background=bg_color, width=w_width - 150, height=(w_height - 200))
        self.main_frame.pack(side='right', fill=BOTH, expand=True)

        # Sidebar Frame - Navigation bar on the left side
        self.sidebar_frame = Frame(self.window, background='#57A6A1', width=150, height=(w_height))
        self.sidebar_frame.pack(side='left', fill=Y)

        # Bottom Frame - Bottom bar
        self.bottom_frame = Frame(self.window, background='#3A3A3A', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom', fill=X)

        # Title Label - Title displayed at the top of the sidebar
        self.title_label = Label(self.sidebar_frame, text="Study Brain", bg='#57A6A1', fg='white', font=('Helvetica', 16, 'bold'))
        self.title_label.pack(pady=10)

        # Button styles
        button_font = ('Helvetica', 12, 'bold')
        button_bg = '#4ECDC4'
        button_fg = 'white'
        button_active_bg = '#3BA18A'
        button_active_fg = 'white'

        # Home Button - Navigates to the Home page
        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_home_page)
        self.home_button.pack(pady=10)

        # Science Button - Navigates to the Science page
        self.science_button = Button(self.sidebar_frame, text="Science", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_science_page)
        self.science_button.pack(pady=10)

        # Maths Button - Navigates to the Maths page
        self.maths_button = Button(self.sidebar_frame, text="Maths", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_maths_page)
        self.maths_button.pack(pady=10)

        # Exit Button - Exits the application
        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.exit)
        self.exit_button.pack(pady=10)

        # Initialize Home Page - Displays the home page initially
        self.show_home_page()

        # Start the main loop
        self.window.mainloop()

    # Function to display the Home Page
    def show_home_page(self):
        self.clear_main_frame()
        home_label = Label(self.main_frame, text="Welcome to the Home Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        home_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Function to display the Science Page
    def show_science_page(self):
        self.clear_main_frame()
        science_label = Label(self.main_frame, text="Welcome to the Science Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        science_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Function to display the Maths Page
    def show_maths_page(self):
        self.clear_main_frame()
        maths_label = Label(self.main_frame, text="Welcome to the Maths Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Function to clear the main frame
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Function to exit the application
    def exit(self):
        answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if answer:
            print("Exit app")
            self.window.destroy()

# Create and run the app
app = App()
