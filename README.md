# PS 76: Student Course Registration System

**Institution:** Rungta International Skills University  
**Department:** School of Computer Science and Engineering  
**Course:** B.Tech Computer Science and Engineering (First Semester)  

---

## 1. Problem Statement
The objective of this project is to develop a console-based course registration system in Python 3. The program manages course registration, dropping of courses, and viewing student details while enforcing capacity limits, preventing duplicate registrations, rejecting non-existent courses, and restricting students to a maximum of 3 courses.

## 2. Concepts Used
- **Object-Oriented Programming (OOP):** Implementation of `Student` and `Course` classes with member functions.
- **Dictionaries:** Fast course lookup and mapping of course capacity and student details.
- **CRUD Operations:**
  - **Create:** Registering a student to a course.
  - **Read:** Viewing enrolled courses for a student and listing available courses.
  - **Delete/Update:** Dropping a course from a student's profile.
- **File Handling:** Persisting active registration records to `registrations.txt`.

## 3. Pre-defined Courses
| Course Code | Course Name | Capacity |
|---|---|---|
| CS101 | Programming | 2 |
| MA101 | Mathematics | 30 |
| PH101 | Physics | 30 |

## 4. How to Run the Project
```bash
python main.py
```

## 5. Test Cases Verification
All 4 test cases specified in the problem statement are verified and screenshots are available inside the `testcases/` folder:
- `testcases/testcase_1.png` - Normal registration
- `testcases/testcase_2.png` - Capacity boundary test
- `testcases/testcase_3.png` - Invalid inputs (Course full, Duplicate entry, Unknown course)
- `testcases/testcase_4.png` - Drop course and View empty student profile