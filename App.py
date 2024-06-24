from tkinter import *
from tkinter import messagebox, ttk
from app_settings import *
from os import *
from PIL import ImageTk, Image

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(str(w_width) + "x" + str(w_height))
        self.window.title(app_title)

        self.history = []  # History stack for navigation

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

        # Quiz Button - Navigates to the Quiz page
        self.quiz_button = Button(self.sidebar_frame, text="Quiz", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_quiz_page)
        self.quiz_button.pack(pady=10)

        # Exit Button - Exits the application
        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.exit)
        self.exit_button.pack(pady=10)

        # Initialize Home Page - Displays the home page initially
        self.show_home_page()

        # Start the main loop
        self.window.mainloop()

    # Function to display the Home Page
    def show_home_page(self):
        self.history.append(self.show_home_page)  # Add current page to history
        self.clear_main_frame()
        home_label = Label(self.main_frame, text="Welcome to the Home Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        home_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.add_back_button()

    # Function to display the Science Page
    def show_science_page(self):
        self.history.append(self.show_science_page)  # Add current page to history
        self.clear_main_frame()
        science_label = Label(self.main_frame, text="Welcome to the Science Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        science_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Add dropdown bar for Level selection
        levels = ["Level 1", "Level 2", "Level 3"]
        self.level_combobox = ttk.Combobox(self.main_frame, values=levels, font=('Helvetica', 12))
        self.level_combobox.set("Select Level")
        self.level_combobox.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.level_combobox.bind("<<ComboboxSelected>>", self.level_selected)

        self.add_back_button()

    # Function called when a level is selected
    def level_selected(self, event):
        level = self.level_combobox.get()
        self.history.append(lambda: self.level_selected(event))  # Add current page to history
        self.clear_main_frame()

        science_label = Label(self.main_frame, text=f"Welcome to the Science Page - {level}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        science_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        subjects = ["Physics", "Chemistry", "Biology"]
        for i, subject in enumerate(subjects):
            subject_button = Button(self.main_frame, text=subject, height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'))
            subject_button.place(relx=0.5, rely=0.6 + (i * 0.1), anchor=CENTER)

        self.add_back_button()

    # Function to display the Maths Page
    def show_maths_page(self):
        self.history.append(self.show_maths_page)  # Add current page to history
        self.clear_main_frame()
        maths_label = Label(self.main_frame, text="Welcome to the Maths Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.add_back_button()

    # Function to display the Quiz Page
    def show_quiz_page(self):
        self.history.append(self.show_quiz_page)  # Add current page to history
        self.clear_main_frame()
        quiz_label = Label(self.main_frame, text="Welcome to the Quiz Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        quiz_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.add_back_button()

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

    # Function to go back to the previous page
    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()  # Remove the current page
            last_page = self.history.pop()  # Get the previous page
            last_page()  # Show the previous page

    # Function to add a back button
    def add_back_button(self):
        back_button = Button(self.main_frame, text="Back", height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=self.go_back)
        back_button.place(relx=0.05, rely=0.95, anchor=SW)

# Create and run the app
app = App()
