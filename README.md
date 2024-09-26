# Lab4-Joseph_Abi_Rizk_Nadim_Succar
A project combining Tkinter and PyQt documented implementations
PyQT: Joseph
Tkinter: Nadim

```markdown
# Tkinter: Nadim

This project is a Tkinter-based graphical user interface (GUI) implementation, built to manage a school system. The application allows users to manage students, instructors, and courses, register students for courses, and perform CRUD operations on records.

## Features

1. **Add Students**: Add students by providing name, age, email, and student ID.
2. **Add Instructors**: Add instructors by providing name, age, email, and instructor ID.
3. **Add Courses**: Add courses by providing the course name and course ID.
4. **Register Students to Courses**: Register students to available courses using a dropdown menu.
5. **Assign Instructors to Courses**: Assign instructors to courses using a dropdown menu.
6. **View All Records**: Display all students, instructors, and courses in a tree view format.
7. **Search Functionality**: Search for students, instructors, or courses by name, ID, or course.
8. **Edit Records**: Select and edit existing student, instructor, or course records.
9. **Delete Records**: Delete selected student, instructor, or course records.
10. **Save Data**: Save all records (students, instructors, courses) to a JSON file.
11. **Load Data**: Load records from a previously saved JSON file.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: Download it from the [official Python website](https://www.python.org/).
- **Tkinter**: Tkinter is included with Python, but if needed, you can install it by running:

  ```bash
  sudo apt-get install python3-tk  # On Linux 
  brew install python-tk           # On macOS
  ```

Other standard Python libraries, such as `json`, should already be installed.

## How to Run the Application

1. **Clone the Repository**: First, clone this repository to your local machine:

    ```bash
    git clone https://github.com/Joseph-Abi-Rizk/Lab4-Joseph_Abi_Rizk_Nadim_Succar.git
    ```

2. **Navigate to the Feature Branch**: Since the implementation is in the `feature-tkinter` branch, switch to it:

    ```bash
    cd Lab4-Joseph_Abi_Rizk_Nadim_Succar
    git checkout feature-tkinter
    ```

3. **Run the Application**: Execute the Python script to launch the Tkinter interface:

    ```bash
    python tkinter_app.py
    ```

This will open the School Management System interface.

## How to Use the Application

### 1. Adding Records:
- **Add Student**: Input the student's name, age, email, and ID, then click "Add Student" to add the student to the system.
- **Add Instructor**: Input the instructor's name, age, email, and ID, then click "Add Instructor" to add the instructor to the system.
- **Add Course**: Enter the course name and ID, then click "Add Course" to add the course.

### 2. Course Registration & Instructor Assignment:
- **Register Students to Courses**: Use the dropdown menus to select a student and a course, then click "Register Student" to enroll the student in the selected course.
- **Assign Instructors to Courses**: Use the dropdown menus to select an instructor and a course, then click "Assign Instructor" to assign the instructor to the course.

### 3. Viewing, Editing, and Deleting Records:
- **Display All Records**: Click the "Display All Records" button to view all students, instructors, and courses.
- **Edit Records**: Select a record in the list, click "Edit Record," and modify the details in the input fields.
- **Delete Records**: Select a record in the list and click "Delete Record" to remove it.

### 4. Searching for Records:
- Select a search criteria (Name, ID, or Course) from the dropdown, input a search term, and click "Search" to filter the displayed records.

### 5. Saving and Loading Data:
- **Save Data**: Click "Save Data" to save all students, instructors, and courses to a JSON file.
- **Load Data**: Click "Load Data" to load the data from a previously saved JSON file.

## Documentation with Sphinx

This project also includes detailed documentation generated using **Sphinx**, which provides a structured overview of the entire codebase. The documentation is useful for understanding the architecture, functions, and classes used throughout the project.

### Steps to View the Documentation:
1. After cloning the repository, navigate to the Sphinx-generated documentation in the `/docs/_build/html/` directory.
   
2. Open the `index.html` file in your web browser to access the documentation homepage.

    - On **Mac/Linux**: 
      ```bash
      open /docs/_build/html/index.html
      ```
    - On **Windows**: 
      ```bash
      start /docs/_build/html/index.html
      ```

### Content of the Documentation:
- **Modules and Classes**: Detailed explanations of the project's main classes (e.g., `Student`, `Instructor`, `Course`) and their methods.
- **Usage Instructions**: Documentation on how to use different features of the Tkinter application.
- **Code Reference**: Docstrings and inline comments that explain the purpose of each function and class.

### Understanding reStructuredText (reST):
The documentation is written using **reStructuredText** (reST) syntax, which is similar to Markdown. If you'd like to contribute to or modify the documentation, you can learn more about reST syntax [here](https://docutils.sourceforge.io/rst.html).

```
