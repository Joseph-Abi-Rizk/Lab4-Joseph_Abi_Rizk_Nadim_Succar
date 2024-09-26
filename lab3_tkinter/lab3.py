import json
import tkinter as tk
from tkinter import ttk, messagebox

class SchoolManagementApp:
    """
    SchoolManagementApp is a Tkinter-based GUI for managing a school system.

    The app allows users to manage students, instructors, and courses,
    and register students for courses.

    :param root: The root Tkinter window.
    :type root: Tk()
    """

    def __init__(self, root):
        """
        Initializes the SchoolManagementApp with the Tkinter root window.
        
        :param root: The root window of the application.
        :type root: Tk()
        """
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("700x500")

        self.students = []
        self.instructors = []
        self.courses = []

        self.setup_gui()

    def setup_gui(self):
        """Sets up the graphical user interface for the application."""
        self.setup_student_form()
        self.setup_instructor_form()
        self.setup_course_form()
        self.setup_course_registration_form()
        self.setup_record_display()
        self.setup_search_bar()
        self.setup_save_load_buttons()

    def setup_student_form(self):
        """Sets up the form to add student information."""
        student_frame = tk.LabelFrame(self.root, text="Add Student", padx=10, pady=10)
        student_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(student_frame, text="Name").grid(row=0, column=0)
        self.student_name_entry = tk.Entry(student_frame)
        self.student_name_entry.grid(row=0, column=1)

        tk.Label(student_frame, text="Age").grid(row=1, column=0)
        self.student_age_entry = tk.Entry(student_frame)
        self.student_age_entry.grid(row=1, column=1)

        tk.Label(student_frame, text="Email").grid(row=2, column=0)
        self.student_email_entry = tk.Entry(student_frame)
        self.student_email_entry.grid(row=2, column=1)

        tk.Label(student_frame, text="Student ID").grid(row=3, column=0)
        self.student_id_entry = tk.Entry(student_frame)
        self.student_id_entry.grid(row=3, column=1)

        tk.Button(student_frame, text="Add Student", command=self.add_student).grid(row=4, column=1)

    def setup_instructor_form(self):
        """Sets up the form to add instructor information."""
        instructor_frame = tk.LabelFrame(self.root, text="Add Instructor", padx=10, pady=10)
        instructor_frame.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(instructor_frame, text="Name").grid(row=0, column=0)
        self.instructor_name_entry = tk.Entry(instructor_frame)
        self.instructor_name_entry.grid(row=0, column=1)

        tk.Label(instructor_frame, text="Age").grid(row=1, column=0)
        self.instructor_age_entry = tk.Entry(instructor_frame)
        self.instructor_age_entry.grid(row=1, column=1)

        tk.Label(instructor_frame, text="Email").grid(row=2, column=0)
        self.instructor_email_entry = tk.Entry(instructor_frame)
        self.instructor_email_entry.grid(row=2, column=1)

        tk.Label(instructor_frame, text="Instructor ID").grid(row=3, column=0)
        self.instructor_id_entry = tk.Entry(instructor_frame)
        self.instructor_id_entry.grid(row=3, column=1)

        tk.Button(instructor_frame, text="Add Instructor", command=self.add_instructor).grid(row=4, column=1)

    def setup_course_form(self):
        """Sets up the form to add course information."""
        course_frame = tk.LabelFrame(self.root, text="Add Course", padx=10, pady=10)
        course_frame.grid(row=2, column=0, padx=10, pady=10)

        tk.Label(course_frame, text="Course Name").grid(row=0, column=0)
        self.course_name_entry = tk.Entry(course_frame)
        self.course_name_entry.grid(row=0, column=1)

        tk.Label(course_frame, text="Course ID").grid(row=1, column=0)
        self.course_id_entry = tk.Entry(course_frame)
        self.course_id_entry.grid(row=1, column=1)

        tk.Button(course_frame, text="Add Course", command=self.add_course).grid(row=2, column=1)

    def setup_course_registration_form(self):
        """
        Sets up the form for registering students to courses and assigning instructors to courses.
        
        Comboboxes are dynamically updated based on the current students, courses, and instructors.
        """
        registration_frame = tk.LabelFrame(self.root, text="Course Registration & Assignment", padx=10, pady=10)
        registration_frame.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

        tk.Label(registration_frame, text="Select Student").grid(row=0, column=0)
        self.student_combobox = ttk.Combobox(registration_frame, values=[s.name for s in self.students])
        self.student_combobox.grid(row=0, column=1)

        tk.Label(registration_frame, text="Select Course").grid(row=1, column=0)
        self.course_combobox = ttk.Combobox(registration_frame, values=[c.course_name for c in self.courses])
        self.course_combobox.grid(row=1, column=1)

        tk.Button(registration_frame, text="Register Student", command=self.register_student_to_course).grid(row=2, column=1)

        tk.Label(registration_frame, text="Select Instructor").grid(row=3, column=0)
        self.instructor_combobox = ttk.Combobox(registration_frame, values=[i.name for i in self.instructors])
        self.instructor_combobox.grid(row=3, column=1)

        tk.Button(registration_frame, text="Assign Instructor", command=self.assign_instructor_to_course).grid(row=4, column=1)

    def setup_record_display(self):
        """Sets up the display for viewing records of students, instructors, and courses."""
        self.tree = ttk.Treeview(self.root, columns=("Type", "Name", "ID"))
        self.tree.heading("#0", text="Type")
        self.tree.heading("Name", text="Name")
        self.tree.heading("ID", text="ID")
        self.tree.grid(row=3, column=0, columnspan=2, pady=20)

        tk.Button(self.root, text="Display All Records", command=self.display_all_records).grid(row=4, column=0, columnspan=2)

        tk.Button(self.root, text="Edit Record", command=self.edit_record).grid(row=5, column=0)
        tk.Button(self.root, text="Delete Record", command=self.delete_record).grid(row=5, column=1)

    def setup_search_bar(self):
        """Sets up the search bar for finding records by name, ID, or course."""
        search_frame = tk.LabelFrame(self.root, text="Search", padx=10, pady=10)
        search_frame.grid(row=6, column=0, columnspan=2, pady=10)

        tk.Label(search_frame, text="Search by:").grid(row=0, column=0)

        self.search_criteria = ttk.Combobox(search_frame, values=["Name", "ID", "Course"])
        self.search_criteria.grid(row=0, column=1)

        self.search_entry = tk.Entry(search_frame)
        self.search_entry.grid(row=0, column=2)

        tk.Button(search_frame, text="Search", command=self.search_records).grid(row=0, column=3)

    def setup_save_load_buttons(self):
        """Sets up the buttons to save and load data from a JSON file."""
        tk.Button(self.root, text="Save Data", command=self.save_data).grid(row=7, column=0)
        tk.Button(self.root, text="Load Data", command=self.load_data).grid(row=7, column=1)

    def add_student(self):
        """
        Adds a new student to the system based on input fields.
        
        :raises ValueError: If the age is not a valid integer.
        """
        try:
            name = self.student_name_entry.get()
            age = int(self.student_age_entry.get())
            email = self.student_email_entry.get()
            student_id = self.student_id_entry.get()
            student = Student(name, age, email, student_id)
            self.students.append(student)
            messagebox.showinfo("Success", f"Student {name} added.")
            self.update_comboboxes()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")

    def add_instructor(self):
        """
        Adds a new instructor to the system based on input fields.
        
        :raises ValueError: If the age is not a valid integer.
        """
        try:
            name = self.instructor_name_entry.get()
            age = int(self.instructor_age_entry.get())
            email = self.instructor_email_entry.get()
            instructor_id = self.instructor_id_entry.get()
            instructor = Instructor(name, age, email, instructor_id)
            self.instructors.append(instructor)
            messagebox.showinfo("Success", f"Instructor {name} added.")
            self.update_comboboxes()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age.")

    def add_course(self):
        """
        Adds a new course to the system based on input fields.
        
        :raises ValueError: If the course ID or name is invalid.
        """
        course_name = self.course_name_entry.get()
        course_id = self.course_id_entry.get()
        course = Course(course_id, course_name)
        self.courses.append(course)
        messagebox.showinfo("Success", f"Course {course_name} added.")
        self.update_comboboxes()

    def register_student_to_course(self):
        """Registers a student to a selected course."""
        student_name = self.student_combobox.get()
        course_name = self.course_combobox.get()

        student = next((s for s in self.students if s.name == student_name), None)
        course = next((c for c in self.courses if c.course_name == course_name), None)

        if student and course:
            student.register_course(course)
            messagebox.showinfo("Success", f"Student {student_name} registered to {course_name}")
        else:
            messagebox.showerror("Error", "Student or course not found")

    def assign_instructor_to_course(self):
        """Assigns an instructor to a selected course."""
        instructor_name = self.instructor_combobox.get()
        course_name = self.course_combobox.get()

        instructor = next((i for i in self.instructors if i.name == instructor_name), None)
        course = next((c for c in self.courses if c.course_name == course_name), None)

        if instructor and course:
            instructor.assign_course(course)
            messagebox.showinfo("Success", f"Instructor {instructor_name} assigned to {course_name}")
        else:
            messagebox.showerror("Error", "Instructor or course not found")

    def display_all_records(self):
        """Displays all students, instructors, and courses in the Treeview."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for student in self.students:
            self.tree.insert("", "end", text="Student", values=(student.name, student.student_id))

        for instructor in self.instructors:
            self.tree.insert("", "end", text="Instructor", values=(instructor.name, instructor.instructor_id))

        for course in self.courses:
            self.tree.insert("", "end", text="Course", values=(course.course_name, course.course_id))

    def search_records(self):
        """Searches for records based on selected criteria and displays the result."""
        search_by = self.search_criteria.get()
        search_value = self.search_entry.get().lower()

        for row in self.tree.get_children():
            self.tree.delete(row)

        if search_by == "Name":
            for student in self.students:
                if search_value in student.name.lower():
                    self.tree.insert("", "end", text="Student", values=(student.name, student.student_id))
            for instructor in self.instructors:
                if search_value in instructor.name.lower():
                    self.tree.insert("", "end", text="Instructor", values=(instructor.name, instructor.instructor_id))
        elif search_by == "ID":
            for student in self.students:
                if search_value in student.student_id.lower():
                    self.tree.insert("", "end", text="Student", values=(student.name, student.student_id))
            for instructor in self.instructors:
                if search_value in instructor.instructor_id.lower():
                    self.tree.insert("", "end", text="Instructor", values=(instructor.name, instructor.instructor_id))
        elif search_by == "Course":
            for course in self.courses:
                if search_value in course.course_name.lower():
                    self.tree.insert("", "end", text="Course", values=(course.course_name, course.course_id))

    def update_comboboxes(self):
        """Updates comboboxes with current values of students, instructors, and courses."""
        self.student_combobox["values"] = [s.name for s in self.students]
        self.course_combobox["values"] = [c.course_name for c in self.courses]
        self.instructor_combobox["values"] = [i.name for i in self.instructors]

    def edit_record(self):
        """Allows editing of selected student, instructor, or course record."""
        selected_item = self.tree.selection()
        if selected_item:
            record = self.tree.item(selected_item)
            record_type = record["text"]
            record_values = record["values"]

            if record_type == "Student":
                student = next((s for s in self.students if s.student_id == record_values[1]), None)
                if student:
                    self.student_name_entry.delete(0, tk.END)
                    self.student_name_entry.insert(0, student.name)
                    self.student_age_entry.delete(0, tk.END)
                    self.student_age_entry.insert(0, student.age)
                    self.student_email_entry.delete(0, tk.END)
                    self.student_email_entry.insert(0, student.get_email())
                    self.student_id_entry.delete(0, tk.END)
                    self.student_id_entry.insert(0, student.student_id)
                    self.students.remove(student)
            elif record_type == "Instructor":
                instructor = next((i for i in self.instructors if i.instructor_id == record_values[1]), None)
                if instructor:
                    self.instructor_name_entry.delete(0, tk.END)
                    self.instructor_name_entry.insert(0, instructor.name)
                    self.instructor_age_entry.delete(0, tk.END)
                    self.instructor_age_entry.insert(0, instructor.age)
                    self.instructor_email_entry.delete(0, tk.END)
                    self.instructor_email_entry.insert(0, instructor.get_email())
                    self.instructor_id_entry.delete(0, tk.END)
                    self.instructor_id_entry.insert(0, instructor.instructor_id)
                    self.instructors.remove(instructor)
            elif record_type == "Course":
                course = next((c for c in self.courses if c.course_id == record_values[1]), None)
                if course:
                    self.course_name_entry.delete(0, tk.END)
                    self.course_name_entry.insert(0, course.course_name)
                    self.course_id_entry.delete(0, tk.END)
                    self.course_id_entry.insert(0, course.course_id)
                    self.courses.remove(course)

    def delete_record(self):
        """Deletes the selected student, instructor, or course record."""
        selected_item = self.tree.selection()
        if selected_item:
            record = self.tree.item(selected_item)
            record_type = record["text"]
            record_values = record["values"]

            if record_type == "Student":
                student = next((s for s in self.students if s.student_id == record_values[1]), None)
                if student:
                    self.students.remove(student)
            elif record_type == "Instructor":
                instructor = next((i for i in self.instructors if i.instructor_id == record_values[1]), None)
                if instructor:
                    self.instructors.remove(instructor)
            elif record_type == "Course":
                course = next((c for c in self.courses if c.course_id == record_values[1]), None)
                if course:
                    self.courses.remove(course)

            self.tree.delete(selected_item)
            messagebox.showinfo("Success", f"{record_type} record deleted.")

    def save_data(self):
        """Saves the current data to a JSON file."""
        try:
            data = {
                "students": [s.__dict__ for s in self.students],
                "instructors": [i.__dict__ for i in self.instructors],
                "courses": [c.__dict__ for c in self.courses]
            }
            with open("school_data.json", "w") as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {e}")

    def load_data(self):
        """Loads data from a JSON file into the system."""
        try:
            with open("school_data.json", "r") as file:
                data = json.load(file)
                self.students = [Student(**s) for s in data["students"]]
                self.instructors = [Instructor(**i) for i in data["instructors"]]
                self.courses = [Course(**c) for c in data["courses"]]
            messagebox.showinfo("Success", "Data loaded successfully!")
            self.display_all_records()  
        except FileNotFoundError:
            messagebox.showerror("Error", "No saved data found.")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementApp(root)
    root.mainloop()