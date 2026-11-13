# Project 76: Student Course Registration System
# First Semester B.Tech Computer Science and Engineering
# Concepts: OOP, Dictionaries, CRUD Operations, File Handling

# Class representing a course
class Course:
    def __init__(self, code, name, capacity):
        self.code = code
        self.name = name
        self.capacity = capacity
        self.enrolled_students = []

    def get_seats_left(self):
        return self.capacity - len(self.enrolled_students)

    def is_full(self):
        return len(self.enrolled_students) >= self.capacity

    def add_student(self, student_id):
        if not self.is_full() and student_id not in self.enrolled_students:
            self.enrolled_students.append(student_id)
            return True
        return False

    def remove_student(self, student_id):
        if student_id in self.enrolled_students:
            self.enrolled_students.remove(student_id)
            return True
        return False


# Class representing a student
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.registered_courses = []

    def enroll(self, course_code):
        if course_code not in self.registered_courses:
            self.registered_courses.append(course_code)

    def drop(self, course_code):
        if course_code in self.registered_courses:
            self.registered_courses.remove(course_code)


# Function to save registrations into file
def save_to_file(students, courses, filename="registrations.txt"):
    with open(filename, "w") as file:
        for s_id, student in students.items():
            for c_code in student.registered_courses:
                course_name = courses[c_code].name if c_code in courses else "Unknown"
                file.write(f"{student.student_id},{student.name},{c_code},{course_name}\n")


# 1. Register Operation (Create)
def register_student(students, courses):
    student_id = input("Student ID: ").strip()
    name = input("Name: ").strip()
    course_code = input("Course: ").strip().upper()

    # Reject unknown courses
    if course_code not in courses:
        print(f"Course {course_code} does not exist.")
        return

    # Check or create student profile
    if student_id not in students:
        students[student_id] = Student(student_id, name)
    else:
        if name and not students[student_id].name:
            students[student_id].name = name

    student = students[student_id]
    course = courses[course_code]

    # Reject duplicates
    if course_code in student.registered_courses:
        print(f"Student {student_id} is already registered in {course_code}.")
        return

    # Reject more than 3 courses per student
    if len(student.registered_courses) >= 3:
        print(f"Student {student_id} has already registered for maximum 3 courses.")
        return

    # Reject full courses
    if course.is_full():
        print(f"Course {course_code} is full.")
        return

    # Enroll student in course
    student.enroll(course_code)
    course.add_student(student_id)
    save_to_file(students, courses)

    print(f"Registered: {student.name} ({student.student_id}) in {course.code} - {course.name}.")
    print(f"Seats left: {course.get_seats_left()}")


# 2. Drop Course Operation (Delete)
def drop_course(students, courses):
    student_id = input("Student ID: ").strip()
    course_code = input("Course: ").strip().upper()

    if student_id not in students:
        print(f"Student {student_id} does not exist.")
        return

    if course_code not in courses:
        print(f"Course {course_code} does not exist.")
        return

    student = students[student_id]
    course = courses[course_code]

    if course_code not in student.registered_courses:
        print(f"Student {student_id} is not registered in {course_code}.")
        return

    student.drop(course_code)
    course.remove_student(student_id)
    save_to_file(students, courses)

    print(f"{student.name} ({student.student_id}) dropped {course.code}. Seats left: {course.get_seats_left()}")


# 3. View Student Operation (Read)
def view_student(students, courses):
    student_id = input("Student ID: ").strip()

    if student_id not in students:
        print(f"Student {student_id} not found.")
        return

    student = students[student_id]

    if len(student.registered_courses) == 0:
        print(f"{student.name} ({student.student_id}) has no registered courses.")
    else:
        print(f"Courses registered by {student.name} ({student.student_id}):")
        for c_code in student.registered_courses:
            course = courses.get(c_code)
            course_name = course.name if course else "Unknown"
            print(f"- {c_code}: {course_name}")


# 4. View Course List Operation (Read)
def view_courses(courses):
    print("\n--- Course List ---")
    for code, course in courses.items():
        print(f"{course.code} - {course.name} | Capacity: {course.capacity} | Enrolled: {len(course.enrolled_students)} | Seats Left: {course.get_seats_left()}")


# Main Function
def main():
    # Initial Courses given in Problem Statement
    courses = {
        "CS101": Course("CS101", "Programming", 2),
        "MA101": Course("MA101", "Mathematics", 30),
        "PH101": Course("PH101", "Physics", 30)
    }

    students = {}

    # Initialize empty registrations.txt file at start
    with open("registrations.txt", "w") as f:
        pass

    while True:
        print("\n=== Student Course Registration System ===")
        print("1. Register")
        print("2. Drop course")
        print("3. View student")
        print("4. View course list")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            register_student(students, courses)
        elif choice == "2":
            drop_course(students, courses)
        elif choice == "3":
            view_student(students, courses)
        elif choice == "4":
            view_courses(courses)
        elif choice == "5":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1 to 5.")


if __name__ == "__main__":
    main()