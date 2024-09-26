from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QFileDialog, QInputDialog
import sys
import csv



import json
import re


class Validator:
    """Validator class for validating email, age, and ID."""

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates an email address format.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_age(age: int) -> bool:
        """
        Validates that the age is between 0 and 120.

        Args:
            age (int): Age to validate.

        Returns:
            bool: True if the age is valid, False otherwise.
        """
        return 0 <= age <= 120

    @staticmethod
    def validate_id(id_value: str) -> bool:
        """
        Validates that the ID contains only alphanumeric characters.

        Args:
            id_value (str): ID to validate.

        Returns:
            bool: True if the ID is valid, False otherwise.
        """
        return id_value.isalnum()


class Person:
    """Person class representing a generic person."""

    def __init__(self, name: str, age: int, email: str):
        """
        Initialize a Person with a name, age, and email.

        Args:
            name (str): The person's name.
            age (int): The person's age.
            email (str): The person's email address.

        Raises:
            AssertionError: If the provided data types or values are invalid.
        """
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(age, int), "Age must be an integer"
        assert Validator.validate_age(age), "Invalid age"
        assert isinstance(email, str), "Email must be a string"
        assert Validator.validate_email(email), "Invalid email format"

        self.name = name
        self.age = age
        self.__email = email

    def introduce(self) -> str:
        """
        Introduces the person by returning their name and age in a string format.

        Returns:
            str: A string introducing the person.
        """
        return f"Hi, my name is {self.name} and I am {self.age} years old."


class Student(Person):
    """Student class that inherits from Person and adds a student ID."""

    def __init__(self, name: str, age: int, email: str, student_id: str):
        """
        Initialize a Student with name, age, email, and student ID.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            email (str): The student's email address.
            student_id (str): The student's unique identifier.

        Raises:
            AssertionError: If the student_id is not a string.
        """
        assert isinstance(student_id, str), "Student ID must be a string"
        super().__init__(name, age, email)
        self.student_id = student_id
        self.registered_courses = []

    def register_course(self, course: 'Course'):
        """
        Registers the student for a course.

        Args:
            course (Course): The course to register the student for.

        Returns:
            list: The list of courses the student is registered for.
        """
        self.registered_courses.append(course)
        return self.registered_courses



class Instructor(Person):
    """Instructor class that inherits from Person and adds an instructor ID."""

    def __init__(self, name: str, age: int, email: str, instructor_id: str):
        """
        Initialize an Instructor with name, age, email, and instructor ID.

        Args:
            name (str): The instructor's name.
            age (int): The instructor's age.
            email (str): The instructor's email address.
            instructor_id (str): The instructor's unique identifier.

        Raises:
            AssertionError: If the instructor_id is not a string.
        """
        assert isinstance(instructor_id, str), "Instructor ID must be a string"
        super().__init__(name, age, email)
        self.assigned_courses = []

    def assign_course(self, course: 'Course'):
        """
        Assigns a course to the instructor.

        Args:
            course (Course): The course to assign to the instructor.

        Returns:
            list: The list of courses assigned to the instructor.
        """
        self.assigned_courses.append(course)
        course.instructor = self
        return self.assigned_courses


class Course:
    """Course class representing a course with an ID and name."""

    def __init__(self, course_id: str, course_name: str):
        """
        Initialize a Course with a course ID and name.

        Args:
            course_id (str): The course's unique identifier.
            course_name (str): The course's name.

        Raises:
            AssertionError: If the course_id or course_name is not a string.
        """
        assert isinstance(course_id, str), "Course ID must be a string"
        assert isinstance(course_name, str), "Course name must be a string"
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = None
        self.enrolled_students = []

    def add_student(self, student: 'Student'):
        """
        Adds a student to the course.

        Args:
            student (Student): The student to add to the course.

        Returns:
            list: The list of students enrolled in the course.
        """
        self.enrolled_students.append(student)
        return self.enrolled_students


class SchoolSystem:
    """Class responsible for saving and loading school data to and from files."""

    @staticmethod
    def save_to_file(filename: str, data: dict):
        """
        Saves school data to a file in JSON format.

        Args:
            filename (str): The name of the file to save data to.
            data (dict): The school data to save.

        Returns:
            None
        """
        def custom_serializer(obj):
            if isinstance(obj, Course):
                return {
                    "course_id": obj.course_id,
                    "course_name": obj.course_name
                }
            return obj.__dict__

        with open(filename, 'w') as f:
            json.dump(data, f, default=custom_serializer, indent=4)

    @staticmethod
    def load_from_file(filename: str) -> dict:
        """
        Loads school data from a JSON file.

        Args:
            filename (str): The name of the file to load data from.

        Returns:
            dict: The loaded school data.
        """
        with open(filename, 'r') as f:
            return json.load(f)

"""
z=Course("102","intro_to_comp")   

x=Student("Christy",8,"christy@gmail.com","2")
print(x.introduce())

y=Instructor("Joseph",20,"joseph@gmail.com","202")

y.assign_course(z)
"""

list_of_students=[]
list_of_instructors=[]
list_of_courses=[]






class SchoolManagementSystem(QMainWindow):
    """Main GUI class for the School Management System."""

    def __init__(self):
        """Initialize the School Management System window and UI components."""
        super().__init__()
        self.setWindowTitle("School Management System")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        """Sets up the user interface for the School Management System."""
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout()

        # Add forms for Student, Instructor, Course
        self.add_student_form(layout)
        self.add_instructor_form(layout)
        self.add_course_form(layout)

        # Buttons for student registration, instructor assignment, and displaying records
        self.add_action_buttons(layout)

        # Search Bar
        self.add_search_bar(layout)

        # Table to display students, instructors, courses
        self.create_table(layout)

        # Buttons for editing and deleting records
        self.add_edit_delete_buttons(layout)

        # Save and Load Data buttons
        self.add_save_load_buttons(layout)

        widget.setLayout(layout)

    def add_student_form(self, layout: QVBoxLayout):
        """
        Adds a form for adding student information.

        Args:
            layout (QVBoxLayout): The layout to add the form to.

        Returns:
            None
        """
        student_label = QLabel("Add Student")
        layout.addWidget(student_label)

        self.student_name_input = QLineEdit()
        self.student_name_input.setPlaceholderText("Student Name")
        layout.addWidget(self.student_name_input)

        self.student_age_input = QLineEdit()
        self.student_age_input.setPlaceholderText("Student Age")
        layout.addWidget(self.student_age_input)

        self.add_student_button = QPushButton("Add Student")
        self.add_student_button.clicked.connect(self.add_student)
        layout.addWidget(self.add_student_button)

    def add_instructor_form(self, layout: QVBoxLayout):
        """
        Adds a form for adding instructor information.

        Args:
            layout (QVBoxLayout): The layout to add the form to.

        Returns:
            None
        """
        instructor_label = QLabel("Add Instructor")
        layout.addWidget(instructor_label)

        self.instructor_name_input = QLineEdit()
        self.instructor_name_input.setPlaceholderText("Instructor Name")
        layout.addWidget(self.instructor_name_input)

        self.instructor_age_input = QLineEdit()
        self.instructor_age_input.setPlaceholderText("Instructor Age")
        layout.addWidget(self.instructor_age_input)

        self.add_instructor_button = QPushButton("Add Instructor")
        self.add_instructor_button.clicked.connect(self.add_instructor)
        layout.addWidget(self.add_instructor_button)

    def add_course_form(self, layout: QVBoxLayout):
        """
        Adds a form for adding course information.

        Args:
            layout (QVBoxLayout): The layout to add the form to.

        Returns:
            None
        """
        course_label = QLabel("Add Course")
        layout.addWidget(course_label)

        self.course_name_input = QLineEdit()
        self.course_name_input.setPlaceholderText("Course Name")
        layout.addWidget(self.course_name_input)

        self.add_course_button = QPushButton("Add Course")
        self.add_course_button.clicked.connect(self.add_course)
        layout.addWidget(self.add_course_button)

    def add_action_buttons(self, layout: QVBoxLayout):
        """
        Adds buttons for registering students in courses and assigning instructors.

        Args:
            layout (QVBoxLayout): The layout to add the buttons to.

        Returns:
            None
        """
        hbox = QHBoxLayout()

        # Dropdown to register a student in a course
        self.course_dropdown = QComboBox()
        hbox.addWidget(self.course_dropdown)

        self.student_dropdown = QComboBox()
        hbox.addWidget(self.student_dropdown)

        self.register_student_button = QPushButton("Register Student to Course")
        self.register_student_button.clicked.connect(self.register_student)
        hbox.addWidget(self.register_student_button)

        layout.addLayout(hbox)

    def add_search_bar(self, layout: QVBoxLayout):
        """
        Adds a search bar for filtering records.

        Args:
            layout (QVBoxLayout): The layout to add the search bar to.

        Returns:
            None
        """
        search_label = QLabel("Search Records")
        layout.addWidget(search_label)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by Student, Instructor, or Course")
        layout.addWidget(self.search_input)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_records)
        layout.addWidget(self.search_button)

    def create_table(self, layout: QVBoxLayout):
        """
        Creates a table for displaying students, instructors, and courses.

        Args:
            layout (QVBoxLayout): The layout to add the table to.

        Returns:
            None
        """
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Columns: Student Name, Instructor Name, Course Name
        self.table.setHorizontalHeaderLabels(["Student Name", "Instructor Name", "Course Name"])
        layout.addWidget(self.table)

    def add_edit_delete_buttons(self, layout: QVBoxLayout):
        """
        Adds buttons for editing and deleting records.

        Args:
            layout (QVBoxLayout): The layout to add the buttons to.

        Returns:
            None
        """
        hbox = QHBoxLayout()

        self.edit_button = QPushButton("Edit Record")
        self.edit_button.clicked.connect(self.edit_record)
        hbox.addWidget(self.edit_button)

        self.delete_button = QPushButton("Delete Record")
        self.delete_button.clicked.connect(self.delete_record)
        hbox.addWidget(self.delete_button)

        layout.addLayout(hbox)

    def add_save_load_buttons(self, layout: QVBoxLayout):
        """
        Adds buttons for saving and loading data to and from CSV files.

        Args:
            layout (QVBoxLayout): The layout to add the buttons to.

        Returns:
            None
        """
        hbox = QHBoxLayout()

        self.save_button = QPushButton("Save to CSV")
        self.save_button.clicked.connect(self.save_to_csv)
        hbox.addWidget(self.save_button)

        self.load_button = QPushButton("Load from CSV")
        self.load_button.clicked.connect(self.load_from_csv)
        hbox.addWidget(self.load_button)

        layout.addLayout(hbox)

    def add_student(self):
        """
        Adds a student based on the user input and displays it in the dropdown.

        Returns:
            None
        """
        name = self.student_name_input.text()
        age = self.student_age_input.text()

        if not name or not age.isdigit():
            QMessageBox.warning(self, "Error", "Invalid input for student.")
            return

        self.student_dropdown.addItem(name)
        self.student_name_input.clear()
        self.student_age_input.clear()

    def add_instructor(self):
        """
        Adds an instructor based on the user input and displays it in the dropdown.

        Returns:
            None
        """
        name = self.instructor_name_input.text()
        age = self.instructor_age_input.text()

        if not name or not age.isdigit():
            QMessageBox.warning(self, "Error", "Invalid input for instructor.")
            return

        self.instructor_name_input.clear()
        self.instructor_age_input.clear()

    def add_course(self):
        """
        Adds a course based on the user input and displays it in the dropdown.

        Returns:
            None
        """
        name = self.course_name_input.text()

        if not name:
            QMessageBox.warning(self, "Error", "Invalid input for course.")
            return

        self.course_dropdown.addItem(name)
        self.course_name_input.clear()

    def register_student(self):
        """
        Registers a student to a selected course and displays the assignment in the table.

        Returns:
            None
        """
        course = self.course_dropdown.currentText()
        student = self.student_dropdown.currentText()

        if not course or not student:
            QMessageBox.warning(self, "Error", "Select both student and course.")
            return

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(student))
        self.table.setItem(row_position, 2, QTableWidgetItem(course))

    def search_records(self):
        """
        Searches and filters records in the table based on user input.

        Returns:
            None
        """
        search_text = self.search_input.text().lower()
        for row in range(self.table.rowCount()):
            student_name = self.table.item(row, 0).text().lower() if self.table.item(row, 0) else ''
            course_name = self.table.item(row, 2).text().lower() if self.table.item(row, 2) else ''
            self.table.setRowHidden(row, search_text not in student_name and search_text not in course_name)

    def edit_record(self):
        """
        Edits a selected record in the table.

        Returns:
            None
        """
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            student_name = self.table.item(selected_row, 0).text() if self.table.item(selected_row, 0) else ''
            course_name = self.table.item(selected_row, 2).text() if self.table.item(selected_row, 2) else ''

            new_student_name, ok1 = QInputDialog.getText(self, "Edit Student Name", "Enter new student name:", text=student_name)
            new_course_name, ok2 = QInputDialog
            new_course_name, ok2 = QInputDialog.getText(self, "Edit Course Name", "Enter new course name:", text=course_name)

            if ok1 and ok2:
                self.table.setItem(selected_row, 0, QTableWidgetItem(new_student_name))
                self.table.setItem(selected_row, 2, QTableWidgetItem(new_course_name))

    def delete_record(self):
        """
        Deletes the selected record from the table.

        Returns:
            None
        """
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            self.table.removeRow(selected_row)

    def save_to_csv(self):
        """
        Saves the table data to a CSV file.

        Returns:
            None
        """
        file_name, _ = QFileDialog.getSaveFileName(self, "Save to CSV", "", "CSV Files (*.csv)")
        if file_name:
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Student Name", "Instructor Name", "Course Name"])

                for row in range(self.table.rowCount()):
                    student_name = self.table.item(row, 0).text() if self.table.item(row, 0) else ''
                    instructor_name = self.table.item(row, 1).text() if self.table.item(row, 1) else ''
                    course_name = self.table.item(row, 2).text() if self.table.item(row, 2) else ''
                    writer.writerow([student_name, instructor_name, course_name])

    def load_from_csv(self):
        """
        Loads data from a CSV file into the table.

        Returns:
            None
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Load from CSV", "", "CSV Files (*.csv)")
        if file_name:
            with open(file_name, mode='r') as file:
                reader = csv.reader(file)
                self.table.setRowCount(0)
                next(reader)  # Skip header row
                for row_data in reader:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    for column, data in enumerate(row_data):
                        self.table.setItem(row_position, column, QTableWidgetItem(data))

def main():
    app = QApplication(sys.argv)
    window = SchoolManagementSystem()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
