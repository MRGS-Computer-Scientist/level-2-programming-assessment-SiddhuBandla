from tkinter import *
from tkinter import messagebox, ttk
from app_settings import *
from os import *
from PIL import ImageTk, Image
import webbrowser

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

        # Dark Mode Button - Toggle Dark mode
        self.dark_mode_button = Button(self.window, text="Dark Mode", bg='#222', fg='white', font=('Helvetica', 10, 'bold'), command=self.toggle_dark_mode)
        self.dark_mode_button.place(relx=1, rely=0, anchor=NE, x=-10, y=10)

        # Initialize Home Page - Displays the home page initially
        self.show_home_page()

        # Start the main loop
        self.window.mainloop()

    # Function to toggle Dark mode
    def toggle_dark_mode(self):
        # Toggle background and text colors
        global bg_color
        if bg_color == 'white':
            bg_color = '#222'  # Dark mode background color
            self.window.config(bg=bg_color)
            self.sidebar_frame.config(bg='#444')
            self.bottom_frame.config(bg='#111')
            self.title_label.config(bg='#444', fg='white')
            self.home_button.config(bg='#444', fg='white', activebackground='#333', activeforeground='white')
            self.science_button.config(bg='#444', fg='white', activebackground='#333', activeforeground='white')
            self.maths_button.config(bg='#444', fg='white', activebackground='#333', activeforeground='white')
            self.quiz_button.config(bg='#444', fg='white', activebackground='#333', activeforeground='white')
            self.dark_mode_button.config(bg='#444', fg='white', activebackground='#333', activeforeground='white')
            for widget in self.main_frame.winfo_children():
                widget.config(bg='#222', fg='white' if isinstance(widget, Button) else 'black')
        else:
            bg_color = 'white'  # Light mode background color
            self.window.config(bg=bg_color)
            self.sidebar_frame.config(bg='#57A6A1')
            self.bottom_frame.config(bg='#3A3A3A')
            self.title_label.config(bg='#57A6A1', fg='white')
            self.home_button.config(bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white')
            self.science_button.config(bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white')
            self.maths_button.config(bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white')
            self.quiz_button.config(bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white')
            self.dark_mode_button.config(bg='#222', fg='white', activebackground='#333', activeforeground='white')
            for widget in self.main_frame.winfo_children():
                widget.config(bg=bg_color, fg='black')

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
        science_label.place(relx=0.5, rely=0.2, anchor=N)

        # Add dropdown bar for Level selection
        levels = ["Level 1", "Level 2", "Level 3"]
        self.level_combobox = ttk.Combobox(self.main_frame, values=levels, font=('Helvetica', 12))
        self.level_combobox.set("Select Level")
        self.level_combobox.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.level_combobox.bind("<<ComboboxSelected>>", self.level_selected_science)

        self.add_back_button()

    # Function called when a science level is selected
    def level_selected_science(self, event):
        level = self.level_combobox.get()
        self.history.append(lambda: self.level_selected_science(event))  # Add current page to history
        self.clear_main_frame()

        science_label = Label(self.main_frame, text=f"Welcome to the Science Page - {level}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        science_label.place(relx=0.5, rely=0.2, anchor=N)

        if level == "Level 1":
            subjects = ["General Science"]
            subject_urls = {
                "General Science": "https://www.nobraintoosmall.co.nz/science/general_science.html"
            }
        elif level == "Level 2":
            subjects = ["Physics", "Chemistry", "Biology"]
            subject_urls = {
                "Physics": "https://www.nobraintoosmall.co.nz/html/senior_physics/NCEA2_physics.html",
                "Chemistry": "https://www.nobraintoosmall.co.nz/html/senior_chemistry/NCEA2_chemistry.html",
                "Biology": "https://www.nobraintoosmall.co.nz/html/senior_biology/NCEA2_biology.html"
            }
        elif level == "Level 3":
            subjects = ["Physics", "Chemistry", "Biology"]
            subject_urls = {
                "Physics": "https://www.nobraintoosmall.co.nz/html/senior_physics/NCEA3_physics.html",
                "Chemistry": "https://www.nobraintoosmall.co.nz/html/senior_chemistry/NCEA3_chemistry.html",
                "Biology": "https://www.nobraintoosmall.co.nz/html/senior_biology/NCEA3_biology.html"
            }

        # Calculate starting position for buttons
        start_x = 0.5 - (len(subjects) / 2 * 0.15)

        for i, subject in enumerate(subjects):
            subject_button = Button(self.main_frame, text=subject, height=2, width=15, bg=button_bg, fg=button_fg,
                                    activebackground=button_active_bg, activeforeground=button_active_fg,
                                    font=button_font,
                                    command=lambda subj=subject: self.open_subject_page(subject_urls.get(subj)))
            subject_button.place(relx=start_x + i * 0.15, rely=0.5, anchor=N)

        self.add_back_button()

    # Function to open a subject page in a web browser
    def open_subject_page(self, url):
        webbrowser.open_new(url)

    # Function to display the Maths Page
    def show_maths_page(self):
        self.history.append(self.show_maths_page)  # Add current page to history
        self.clear_main_frame()

        maths_label = Label(self.main_frame, text="Welcome to the Maths Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.2, anchor=N)

        # Add dropdown bar for Level selection
        levels = ["Level 1", "Level 2", "Level 3"]
        self.level_combobox = ttk.Combobox(self.main_frame, values=levels, font=('Helvetica', 12))
        self.level_combobox.set("Select Level")
        self.level_combobox.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.level_combobox.bind("<<ComboboxSelected>>", self.level_selected_maths)

        self.add_back_button()

    # Function called when a maths level is selected
    def level_selected_maths(self, event):
        level = self.level_combobox.get()
        self.history.append(lambda: self.level_selected_maths(event))  # Add current page to history
        self.clear_main_frame()

        maths_label = Label(self.main_frame, text=f"Welcome to the Maths Page - {level}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.2, anchor=N)

        if level == "Level 1":
            subjects = ["Algebra", "Statistics", "Calculus"]
            subject_urls = {
                "Algebra": "https://www.nobraintoosmall.co.nz/maths/algebra.html",
                "Statistics": "https://www.nobraintoosmall.co.nz/maths/statistics.html",
                "Calculus": "https://www.nobraintoosmall.co.nz/maths/calculus.html"
            }
        elif level == "Level 2":
            subjects = ["Algebra", "Statistics", "Calculus"]
            subject_urls = {
                "Algebra": "https://www.nobraintoosmall.co.nz/maths/NCEA2_algebra.html",
                "Statistics": "https://www.nobraintoosmall.co.nz/maths/NCEA2_statistics.html",
                "Calculus": "https://www.nobraintoosmall.co.nz/maths/NCEA2_calculus.html"
            }
        elif level == "Level 3":
            subjects = ["Algebra", "Statistics", "Calculus"]
            subject_urls = {
                "Algebra": "https://www.nobraintoosmall.co.nz/maths/NCEA3_algebra.html",
                "Statistics": "https://www.nobraintoosmall.co.nz/maths/NCEA3_statistics.html",
                "Calculus": "https://www.nobraintoosmall.co.nz/maths/NCEA3_calculus.html"
            }

        # Calculate starting position for buttons
        start_x = 0.5 - (len(subjects) / 2 * 0.15)

        for i, subject in enumerate(subjects):
            subject_button = Button(self.main_frame, text=subject, height=2, width=15, bg=button_bg, fg=button_fg,
                                    activebackground=button_active_bg, activeforeground=button_active_fg,
                                    font=button_font,
                                    command=lambda subj=subject: self.open_subject_page(subject_urls.get(subj)))
            subject_button.place(relx=start_x + i * 0.15, rely=0.5, anchor=N)

        self.add_back_button()

    # Function to display the Quiz Page
    def show_quiz_page(self):
        self.history.append(self.show_quiz_page)  # Add current page to history
        self.clear_main_frame()
        quiz_label = Label(self.main_frame, text="Welcome to the Quiz Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        quiz_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.add_back_button()

    # Function to clear the main frame before loading a new page
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Function to add a Back button for navigation
    def add_back_button(self):
        if len(self.history) > 1:
            back_button = Button(self.bottom_frame, text="Back", bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.go_back)
            back_button.place(relx=0.02, rely=0.5, anchor=W)

    # Function to navigate back to the previous page
    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()  # Remove current page
            previous_page = self.history.pop()  # Get previous page function
            previous_page()  # Display previous page

if __name__ == "__main__":
    app = App()
