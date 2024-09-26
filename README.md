# Lab4-Joseph_Abi_Rizk_Nadim_Succar
A project combining Tkinter and PyQt documented implementations
PyQT: Joseph
Tkinter: Nadim


for the PYQT (Joseph):


### Features:
- Add students, instructors, and courses.
- Register students in courses.
- Assign instructors to courses.
- View, edit, and delete records.
- Save and load data using CSV files.
- Search functionality to filter records.

---

### Prerequisites
Before running the application, ensure you have the following installed:

1. **Python 3.x**: Download from [Python's official website](https://www.python.org/).
2. **PyQt5**: Install using pip if you don't have it already.

```bash
pip install PyQt5
```

3. **Other Modules**: Ensure you have the following standard Python libraries (which should already be installed):
   - `csv`
   - `json`
   - `re`
   - `sys`

---

### How to Run the Application

1. **Clone the Repository**:
   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/YourUsername/SchoolManagementSystem.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd SchoolManagementSystem
   ```

3. **Run the Application**:
   Execute the main Python script that launches the PyQt interface:

   ```bash
   python main.py
   ```

   This will open the **School Management System** interface.

---

### How to Use the Application

1. **Main Interface**:
   The main interface allows you to manage students, instructors, and courses. It consists of input forms and buttons for the following operations:
   
   - **Add Student**: Input the student's name and age, then click "Add Student" to add them to the system.
   - **Add Instructor**: Input the instructor's name and age, then click "Add Instructor" to add them to the system.
   - **Add Course**: Enter the course name and click "Add Course" to add it.

2. **Register Students to Courses**:
   Use the dropdown menus to select a student and a course, then click "Register Student to Course" to enroll the student in the selected course.

3. **Search Functionality**:
   You can search for records by typing a keyword (student, instructor, or course) in the search bar and clicking "Search." The system will filter the records accordingly.

4. **Edit and Delete Records**:
   - To edit a record, select it from the table and click the "Edit Record" button. Enter the new values for the student or course name.
   - To delete a record, select it from the table and click the "Delete Record" button.

5. **Saving and Loading Data**:
   - Click "Save to CSV" to save the current state of the system to a CSV file.
   - Click "Load from CSV" to load data from a previously saved CSV file.


### How to Read the Documentation

This project includes documentation generated using **Sphinx**, which provides a detailed overview of the codebase, including class methods, functions, and other important information.

#### Steps to View the Documentation:

   - Navigate to the `/_build/html/` directory.
   - Open the `index.html` file in your web browser to access the documentation home page.

     You can do this either by:
     - Double-clicking the `index.html` file, or
     - Running the following command in your terminal:

       ```bash
       open /_build/html/index.html   # On Mac/Linux
       start /_build/html/index.html  # On Windows
       ```

#### Content of the Documentation:

- **Modules and Classes**: The documentation contains details about the main classes like `Person`, `Student`, `Instructor`, and `Course`. It explains their properties and methods, along with how they interact with each other.
- **Usage Instructions**: There are explanations on how each class and function can be used within the application.
- **Code Reference**: The code is explained with its docstrings, giving clear examples and describing the purpose of each function and class.

#### Understanding reStructuredText (reST):

The documentation was created using **reStructuredText** (reST) syntax, which is similar to Markdown. If you want to contribute to the documentation or edit it, you can learn more about reST syntax from the [official reStructuredText documentation](https://docutils.sourceforge.io/rst.html).

---

### Documentation Sections:
- **API Documentation**: Describes each module, class, and method in the project.
- **Usage Examples**: Demonstrates how the project can be used.
- **Contributing to the Documentation**: If you'd like to contribute, you can add or edit docstrings in the code and re-run the Sphinx build process.

---
