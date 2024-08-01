from tkinter import *
from tkinter import messagebox, ttk
import webbrowser
from PIL import ImageTk, Image


app_title = "Study Brain"
w_width = 1200
w_height = 700
bg_color = '#EAEDED'

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry(f"{w_width}x{w_height}")
        self.window.title(app_title)

        self.history = []  # History stack for navigation

        # Main Frame - Central area for displaying main content
        self.main_frame = Frame(self.window, background=bg_color, width=w_width - 150, height=w_height - 200)
        self.main_frame.pack(side='right', fill=BOTH, expand=True)

        # Sidebar Frame - Navigation bar on the left side
        self.sidebar_frame = Frame(self.window, background='#57A6A1', width=150, height=w_height)
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

        # Contact Us Button - Navigates to the Contact Us page
        self.contact_button = Button(self.sidebar_frame, text="Contact Us", height=2, width=15, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg, font=button_font, command=self.show_contact_page)
        self.contact_button.pack(pady=10)

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

        maths_label = Label(self.main_frame, text=f"Welcome to the Maths Page - {level}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        maths_label.place(relx=0.5, rely=0.2, anchor=N)

        if level == "Maths Level 1":
            topics = ["Algebra", "Geometry", "Statistics"]
            topic_urls = {
                "Algebra": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=algebra&view=all&level=01",
                "Geometry": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=geometry&view=all&level=01",
                "Statistics": "https://www.nzqa.govt.nz/ncea/assessment/search.do?"
            }
        elif level == "Maths Level 2":
            topics = ["Trigonometry", "Calculus", "Probability"]
            topic_urls = {
                "Trigonometry": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=calculus&view=all&level=02",
                "Calculus": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=trigonometry&view=all&level=02",
                "Probability": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=probability&view=all&level=02"
            }
        elif level == "Maths Level 3":
            topics = ["Advanced Calculus", "Linear Algebra", "Number Theory"]
            topic_urls = {
                "Advanced Calculus": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=advanced+calculus&view=all&level=03",
                "Linear Algebra": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=advanced+algebra&view=all&level=03",
                "Number Theory": "https://www.nzqa.govt.nz/ncea/assessment/search.do?query=advanced+statistics&view=all&level=03"   
            }

        # Calculate starting position for buttons
        start_x = 0.5 - (len(topics) / 2 * 0.15)

        for i, topic in enumerate(topics):
            topic_button = Button(self.main_frame, text=topic, height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=lambda url=topic_urls[topic]: self.open_resource(url))
            topic_button.place(relx=start_x + i * 0.3, rely=0.5, anchor=CENTER)

        self.add_back_button()

    # Function to display the Quiz Page
    def show_quiz_page(self):
        self.history.append(self.show_quiz_page)  # Add current page to history
        self.clear_main_frame()

        quiz_label = Label(self.main_frame, text="Welcome to the Quiz Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        quiz_label.place(relx=0.5, rely=0.2, anchor=N)

        # Example Quiz questions (at least 10 questions)
        questions = [
            {"question": "What is the square root of 81?", "options": ["9", "8", "7", "6"], "answer": "9"},
            {"question": "What is the value of pi (π) correct to two decimal places?", "options": ["3.14", "3.12", "3.16", "3.18"], "answer": "3.14"},
            {"question": "What is the area of a rectangle with length 5 units and width 3 units?", "options": ["8 sq units", "15 sq units", "12 sq units", "7 sq units"], "answer": "15 sq units"},
            {"question": "What is the formula for the volume of a sphere?", "options": ["πr^2", "4/3πr^3", "2πr", "πr"], "answer": "4/3πr^3"},
            {"question": "Which mathematical constant is the base of natural logarithms?", "options": ["e", "π", "φ", "γ"], "answer": "e"},
            {"question": "What is the derivative of sin(x) with respect to x?", "options": ["cos(x)", "sin(x)", "-cos(x)", "-sin(x)"], "answer": "cos(x)"},
            {"question": "What is the sum of the interior angles of a triangle?", "options": ["180 degrees", "270 degrees", "360 degrees", "90 degrees"], "answer": "180 degrees"},
            {"question": "What is the formula for the area of a circle?", "options": ["πr^2", "2πr", "πr", "2r"], "answer": "πr^2"},
            {"question": "What is the value of log10(100)?", "options": ["1", "2", "3", "4"], "answer": "2"},
            {"question": "What is the equation of a straight line in slope-intercept form?", "options": ["y = mx + b", "y = bx + m", "x = my + b", "x = by + m"], "answer": "y = mx + b"}
        ]

        self.current_question = 0
        self.answer_var = StringVar()

        question_label = Label(self.main_frame, text=questions[self.current_question]["question"], bg=bg_color, fg='black', font=('Helvetica', 12))
        question_label.place(relx=0.5, rely=0.3, anchor=N)

        for i, option in enumerate(questions[self.current_question]["options"]):
            option_button = Radiobutton(self.main_frame, text=option, variable=self.answer_var, value=option)
            option_button.place(relx=0.5, rely=0.4 + i * 0.1, anchor=N)

        next_button = Button(self.main_frame, text="Next", height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=lambda: self.next_question(questions))
        next_button.place(relx=0.5, rely=0.7, anchor=N)

        self.add_back_button()

    # Function to move to the next question in the quiz
    def next_question(self, questions):
        # Check if an answer is selected
        if self.answer_var.get():
            self.current_question += 1
            if self.current_question < len(questions):
                # Display next question
                self.clear_main_frame()

                question_label = Label(self.main_frame, text=questions[self.current_question]["question"], bg=bg_color, fg='black', font=('Helvetica', 12))
                question_label.place(relx=0.5, rely=0.3, anchor=N)

                for i, option in enumerate(questions[self.current_question]["options"]):
                    option_button = Radiobutton(self.main_frame, text=option, variable=self.answer_var, value=option)
                    option_button.place(relx=0.5, rely=0.4 + i * 0.1, anchor=N)

                next_button = Button(self.main_frame, text="Next", height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=lambda: self.next_question(questions))
                next_button.place(relx=0.5, rely=0.7, anchor=N)
            else:
                # Quiz completed
                self.show_quiz_complete(questions)
        else:
            messagebox.showwarning("Warning", "Please select an answer!")

    # Function to display the Quiz completion message without showing correct answers
    def show_quiz_complete(self, questions):
        self.clear_main_frame()

        correct_answers = sum(1 for q in questions if q["answer"] == self.answer_var.get())
        total_questions = len(questions)

        score_label = Label(self.main_frame, text=f"Quiz Complete!\nYour Score: {correct_answers}/{total_questions}", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        score_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Reset quiz state
        self.current_question = 0
        self.answer_var = None

        self.add_back_button()

    # Function to display the Contact Us Page
    def show_contact_page(self):
        self.history.append(self.show_contact_page)  # Add current page to history
        self.clear_main_frame()

        contact_label = Label(self.main_frame, text="Welcome to the Contact Us Page", bg=bg_color, fg='black', font=('Helvetica', 16, 'bold'))
        contact_label.place(relx=0.5, rely=0.2, anchor=N)

        contact_text = Text(self.main_frame, height=10, width=50)
        contact_text.insert(END, "For any queries, please email us at: 22305@students.mrgs.school.nz")
        contact_text.config(state=DISABLED)
        contact_text.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.add_back_button()

    # Function to clear the main frame before loading new content
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # Function to add a back button for navigation
    def add_back_button(self):
        back_button = Button(self.bottom_frame, text="Back", height=2, width=15, bg='#4ECDC4', fg='white', activebackground='#3BA18A', activeforeground='white', font=('Helvetica', 12, 'bold'), command=self.back)
        back_button.pack(side=LEFT, padx=20, pady=20)

    # Function to navigate back to the previous page
    def back(self):
        if len(self.history) > 1:
            self.history.pop()  # Remove current page from history
            previous_page = self.history[-1]
            previous_page()

    # Function to open a web resource in a browser
    def open_resource(self, url):
        webbrowser.open_new(url)

    # Function to exit the application
    def exit(self):
        self.window.destroy()

# Create an instance of the App class to start the application
app = App()
