from tkinter import *
from tkinter import messagebox, ttk
import webbrowser
from PIL import ImageTk, Image

# Assuming these are your existing app settings
app_title = "Study Brain"
w_width = 1200
w_height = 700
bg_color = '#EAEDED'

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
        self.title_label = Label(self.sidebar_frame, text=app_title, bg='#57A6A1', fg='white', font=('Helvetica', 16, 'bold'))
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
        home_label.place(relx=0.5, rely=0.6, anchor=CENTER)

        # Example image display
        image = Image.open("home_image.png")
        resize_image = image.resize((700, 300))
        img = ImageTk.PhotoImage(resize_image)
        home_image_label = Label(self.main_frame, image=img)
        home_image_label.image = img
        home_image_label.place(relx=0.5, rely=0.3, anchor=CENTER)

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
            subject_button = Button(self.main_frame, text=subject, height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=lambda url=subject_urls[subject]: self.open_resource(url))
            subject_button.place(relx=start_x + i * 0.3, rely=0.5, anchor=CENTER)

        self.add_back_button()

    # Function to display the Maths Page
    def show_maths_page(self):
        self.history.append(self.show_maths_page)  # Add current page to history
        self.clear_main_frame()

        # Set the appropriate level label
        level_label_text = "Select Maths Level"

        maths_label = Label(self.main_frame, text=level_label_text, bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.2, anchor=N)

        # Add dropdown bar for M Level selection
        levels = ["Maths Level 1", "Maths Level 2", "Maths Level 3"]
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

        level_label_text = f"Welcome to the Maths Page - {level}"
        maths_label = Label(self.main_frame, text=level_label_text, bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.2, anchor=N)

        # Depending on the level, display appropriate content
        if level == "Maths Level 1":
            # Display resources or content for Maths Level 1
            url = "https://www.nobraintoosmall.co.nz/maths/NCEA1_mathematics.html"
        elif level == "Maths Level 2":
            # Display resources or content for Maths Level 2
            url = "https://www.nobraintoosmall.co.nz/maths/NCEA2_mathematics.html"
        elif level == "Maths Level 3":
            # Display resources or content for Maths Level 3
            url = "https://www.nobraintoosmall.co.nz/maths/NCEA3_mathematics.html"
        else:
            url = ""

        if url:
            open_url_button = Button(self.main_frame, text="Open Resource", height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=lambda: self.open_resource(url))
            open_url_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.add_back_button()

    # Function to open a web resource in a browser
    def open_resource(self, url):
        webbrowser.open_new(url)

    # Function to display the Quiz Page
    def show_quiz_page(self):
        self.history.append(self.show_quiz_page)  # Add current page to history
        self.clear_main_frame()

        quiz_label = Label(self.main_frame, text="Welcome to the Quiz Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        quiz_label.place(relx=0.5, rely=0.1, anchor=N)

        # Quiz questions and answers
        self.questions = [
            {
                'question': 'What is the powerhouse of the cell?',
                'options': ['Nucleus', 'Mitochondrion', 'Ribosome', 'Lysosome'],
                'correct_answer': 'Mitochondrion'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['Mars', 'Jupiter', 'Saturn', 'Venus'],
                'correct_answer': 'Mars'
            },
            {
                'question': 'What is the value of π (pi) approximately equal to?',
                'options': ['3.14', '2.71', '1.61', '4.20'],
                'correct_answer': '3.14'
            },
            {
                'question': 'Which equation represents the Pythagorean theorem?',
                'options': ['a^2 + b^2 = c^2', 'E = mc^2', 'F = ma', 'F = m * a'],
                'correct_answer': 'a^2 + b^2 = c^2'
            },
            {
                'question': 'What is the chemical symbol for water?',
                'options': ['H2O', 'CO2', 'O2', 'HCl'],
                'correct_answer': 'H2O'
            },
            # Add more questions as needed...
        ]

        self.current_question = 0
        self.score = 0

        self.display_question()

    # Function to display current question and options
    def display_question(self):
        question_text = self.questions[self.current_question]['question']
        options = self.questions[self.current_question]['options']

        question_label = Label(self.main_frame, text=question_text, bg=bg_color, fg='black', font=('Helvetica', 14))
        question_label.place(relx=0.5, rely=0.3, anchor=N)

        self.option_var = StringVar()
        self.option_var.set(None)

        for i, option in enumerate(options):
            option_button = Radiobutton(self.main_frame, text=option, variable=self.option_var, value=option, bg=bg_color, fg='black', font=('Helvetica', 12))
            option_button.place(relx=0.5, rely=0.4 + i * 0.1, anchor=N)

        submit_button = Button(self.main_frame, text="Submit", height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=self.check_answer)
        submit_button.place(relx=0.5, rely=0.8, anchor=N)

        self.add_back_button()

    # Function to check the selected answer
    def check_answer(self):
        selected_answer = self.option_var.get()
        correct_answer = self.questions[self.current_question]['correct_answer']

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.clear_main_frame()
            self.display_question()
        else:
            self.clear_main_frame()
            result_label = Label(self.main_frame, text=f"You scored {self.score} out of {len(self.questions)}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
            result_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.add_back_button()

    # Function to clear the main frame
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Function to add a back button
    def add_back_button(self):
        if len(self.history) > 1:
            back_button = Button(self.bottom_frame, text="Back", height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=self.go_back)
            back_button.place(relx=0.1, rely=0.5, anchor=CENTER)

    # Function to navigate back in history
    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()()  # Call the previous page function from history

    # Function to exit the application
    def exit(self):
        self.window.destroy()

# Run the application
if __name__ == "__main__":
    app = App()
