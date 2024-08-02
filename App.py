from tkinter import *
from tkinter import messagebox, ttk
import webbrowser
from PIL import ImageTk, Image

# Base App Window/Size of window
app_title = "Study Brain!"
w_width = 1200
w_height = 700
bg_color = '#EAEDED'

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(f"{w_width}x{w_height}")
        self.window.title(app_title)

        self.history = []  # Stack for back button

# Main home page frame
        self.main_frame = Frame(self.window, background=bg_color, width=w_width - 150, height=w_height - 200)
        self.main_frame.pack(side='right', fill=BOTH, expand=True)

# Sidebar frame for navigation
        self.sidebar_frame = Frame(self.window, background='#57A6A1', width=150, height=w_height)
        self.sidebar_frame.pack(side='left', fill=Y)

# Bottom frame for back button
        self.bottom_frame = Frame(self.window, background='#3A3A3A', width=w_width, height=100)
        self.bottom_frame.pack(side='bottom', fill=X)

# Sidebar title
        self.title_label = Label(self.sidebar_frame, text=app_title, bg='#57A6A1', fg='white', font=('Helvetica', 16, 'bold'))
        self.title_label.pack(pady=10)

 # Button styling
        button_font = ('Helvetica', 12, 'bold')
        button_bg = '#4ECDC4'
        button_fg = 'white'
        button_active_bg = '#3BA18A'
        button_active_fg = 'white'

# Home button
        self.home_button = Button(self.sidebar_frame, text="Home", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_home_page)
        self.home_button.pack(pady=10)

# Science button
        self.science_button = Button(self.sidebar_frame, text="Science", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_science_page)
        self.science_button.pack(pady=10)

# Maths button
        self.maths_button = Button(self.sidebar_frame, text="Maths", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_maths_page)
        self.maths_button.pack(pady=10)

# Quiz button
        self.quiz_button = Button(self.sidebar_frame, text="Quiz", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_quiz_page)
        self.quiz_button.pack(pady=10)

# Contact Us button
        self.contact_button = Button(self.sidebar_frame, text="Contact Us", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_contact_page)
        self.contact_button.pack(pady=10)

# Exit button
        self.exit_button = Button(self.sidebar_frame, text="Exit", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.exit)
        self.exit_button.pack(pady=10)

# Show home page 
        self.show_home_page()

# Run main loop
        self.window.mainloop()

# Show the home page
    def show_home_page(self):
        self.history.append(self.show_home_page)  # Adds current page to history
        self.clear_main_frame()

        home_label = Label(self.main_frame, text="Welcome to the Home Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        home_label.place(relx=0.5, rely=0.6, anchor=CENTER)

# Display home image
        image = Image.open("home_image.png")
        resize_image = image.resize((700, 300))
        img = ImageTk.PhotoImage(resize_image)
        home_image_label = Label(self.main_frame, image=img)
        home_image_label.image = img
        home_image_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.add_back_button()

# Show the science page
    def show_science_page(self):
        self.history.append(self.show_science_page)  # Adds current page to history
        self.clear_main_frame()

        science_label = Label(self.main_frame, text="Welcome to the Science Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        science_label.place(relx=0.5, rely=0.2, anchor=N)

# dropdown bar for each level
        levels = ["Level 1", "Level 2", "Level 3"]
        self.level_combobox = ttk.Combobox(self.main_frame, values=levels, font=('Helvetica', 12))
        self.level_combobox.set("Select Level")
        self.level_combobox.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.level_combobox.bind("<<ComboboxSelected>>", self.level_selected_science)

        self.add_back_button()

# science level selection
    def level_selected_science(self, event):
        level = self.level_combobox.get()
        self.history.append(lambda: self.level_selected_science(event))  # Adds current selection to history
        self.clear_main_frame()

        science_label = Label(self.main_frame, text=f"Welcome to the Science Page - {level}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        science_label.place(relx=0.5, rely=0.2, anchor=N)

# Subjects and URLs based on level
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

# Subject buttons
        start_x = 0.5 - (len(subjects) / 2 * 0.15)

        for i, subject in enumerate(subjects):
            subject_button = Button(self.main_frame, text=subject, height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=lambda url=subject_urls[subject]: self.open_resource(url))
            subject_button.place(relx=start_x + i * 0.3, rely=0.5, anchor=CENTER)

        self.add_back_button()

# Show the maths page
    def show_maths_page(self):
        self.history.append(self.show_maths_page)  # Adds current page to history
        self.clear_main_frame()

        level_label_text = "Select Maths Level"

        maths_label = Label(self.main_frame, text=level_label_text, bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.2, anchor=N)

# Level dropdown
        levels = ["Maths Level 1", "Maths Level 2", "Maths Level 3"]
        self.level_combobox = ttk.Combobox(self.main_frame, values=levels, font=('Helvetica', 12))
        self.level_combobox.set("Select Level")
        self.level_combobox.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.level_combobox.bind("<<ComboboxSelected>>", self.level_selected_maths)

        self.add_back_button()

# maths level selection
    def level_selected_maths(self, event):
        level = self.level_combobox.get()
        self.history.append(lambda: self.level_selected_maths(event))  # Adds current selection to history
        self.clear_main_frame()

        maths_label = Label(self.main_frame, text=f"Welcome to the Maths Page - {level}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.2, anchor=N)

# Subjects and URLs based each on level
        if level == "Maths Level 1":
            subjects = ["General Maths"]
            subject_urls = {
                "General Maths": "https://www.nobraintoosmall.co.nz/maths/general_maths.html"
            }
        elif level == "Maths Level 2":
            subjects = ["Algebra", "Calculus", "Geometry"]
            subject_urls = {
                "Algebra": "https://www.nobraintoosmall.co.nz/html/senior_algebra/NCEA2_algebra.html",
                "Calculus": "https://www.nobraintoosmall.co.nz/html/senior_calculus/NCEA2_calculus.html",
                "Geometry": "https://www.nobraintoosmall.co.nz/html/senior_geometry/NCEA2_geometry.html"
            }
        elif level == "Maths Level 3":
            subjects = ["Algebra", "Calculus", "Geometry"]
            subject_urls = {
                "Algebra": "https://www.nobraintoosmall.co.nz/html/senior_algebra/NCEA3_algebra.html",
                "Calculus": "https://www.nobraintoosmall.co.nz/html/senior_calculus/NCEA3_calculus.html",
                "Geometry": "https://www.nobraintoosmall.co.nz/html/senior_geometry/NCEA3_geometry.html"
            }

# Subject buttons
        start_x = 0.5 - (len(subjects) / 2 * 0.15)

        for i, subject in enumerate(subjects):
            subject_button = Button(self.main_frame, text=subject, height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=lambda url=subject_urls[subject]: self.open_resource(url))
            subject_button.place(relx=start_x + i * 0.3, rely=0.5, anchor=CENTER)

        self.add_back_button()

# Show the quiz page
    def show_quiz_page(self):
        self.history.append(self.show_quiz_page)  # Adds current page to history
        self.clear_main_frame()

        quiz_label = Label(self.main_frame, text="Quiz Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        quiz_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.add_back_button()

# Show the contact page
    def show_contact_page(self):
        self.history.append(self.show_contact_page)  # Adds current page to history
        self.clear_main_frame()

        contact_label = Label(self.main_frame, text="Contact Us Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        contact_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.add_back_button()

# Adds back button
    def add_back_button(self):
        if len(self.history) > 1:
            back_button = Button(self.bottom_frame, text="Back", height=2, width=15, bg='#3A3A3A', fg='white', activebackground='#282828', activeforeground='white', font=('Helvetica', 12, 'bold'), command=self.go_back)
            back_button.pack(side='left', padx=10, pady=10)

# Go back to the previous page
    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()  # Remove current page from history
            self.history[-1]()  # Show previous page

# Open a URL in the web browser
    def open_resource(self, url):
        webbrowser.open(url)

# Clear the main frame
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

# Exit the application
    def exit(self):
        self.window.destroy()

if __name__ == "__main__":
    app = App()
