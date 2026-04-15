 from models import Student, Instructor, Course
from engine import ManagementSystem

def run_demo():
    sys = ManagementSystem()
    print("Welcome to the Course Management System!\n")

    # Adding Instructors
    instructors = []
    print("\n--- Please enter instructor data ---")
    while True:
        ins_id = input("Instructor ID (type 'finish' to finish entering instuctor(s) data): ")
        if ins_id.lower() == "finish":
            break
        ins_name = input("Instructor Name: ")
        ins_dept = input("Department: ")
        prof = Instructor(ins_id, ins_name, ins_dept)
        instructors.append(prof)
        print(f"Added instructor: {ins_name}\n")
    
    if not instructors:
        print("There is no instructor added, exciting...")
        return

    # Adding Courses
    course = []
    print("\n--- Please enter course data ---")
    while True:
        c_code = input("Course Code (type 'finish' to finish): ")
        if c_code.lower() == 'finish':
            break
        c_title = input("Course Title: ")
        print("Available Instructors: ")
        for i, inst in enumerate(instructors):
            print(f"{i+1}. {inst.name} (ID: {inst._user_id})")
        choice = int(input("Enter number: ")) - 1
        chosen_in = instructors[choice]

        cour = Course(c_code, c_title, chosen_in)
        course.append(cour)
        sys.add_course(cour)
        print(f"Added course: {c_code} taught by {chosen_in.name}\n")
    # Adding Students
    print("\n--- Enter Student Data ---")
    while True:
        student_id = input("Enter Student ID (or 'finish' to finish): ")
        if student_id.lower() == 'finish':
            break
        name = input("Enter Student Name: ")
        major = input("Enter Student Major: ")
        student = Student(student_id, name, major)
        sys.add_student(student)
        print(f"Added student: {name}\n")

    # Enrollment
    print("\n--- Enrolling Students into Courses ---")
    if not sys.courses:
        print("No courses available for enrollment.")
    else:
        for student in sys.students:
            print(f"\nEnrolling {student.name} (ID: {student._user_id})")
            print("Available courses:")
            for idx, course in enumerate(sys.courses):
                print(f"  {idx+1}. {course.course_code}: {course.title}")
            
            print("Enter course numbers to enroll (separate by spaces, or type 'done' to skip):")
            choices = input("Your choice(s): ")
            if choices.lower() == 'done':
                continue
            
            # Parse input (e.g., "1 3 4")
            for token in choices.split():
                try:
                    course_index = int(token) - 1
                    if 0 <= course_index < len(sys.courses):
                        chosen_course = sys.courses[course_index]
                        sys.enroll_student_in_course(student._user_id, chosen_course.course_code)
                    else:
                        print(f"Invalid course number: {token}, skipping.")
                except ValueError:
                    print(f"Invalid input '{token}', skipping.")

    print("\n--- Course List ---")
    print(sys.get_all_course_titles())

    print("\n--- User Details (Polymorphism) ---")
    users = instructors + sys.students
    for u in users:
        # Calls the specific get_details() based on object type
        print(u.get_details())

    #Check couse details
    print("\n--- Course Details ---")
    while True:
        choice = input("Do you want to check the course details? (1 for yes, 2 for no): ")
        if choice == "1":
            course_code = input("Enter course code: ")
            sys.print_course_details(course_code)
        elif choice == "2":
            print("Exiting the course details check.")
            break
        else:
            print("Invalid enter, please try again.")
    print("\nThank you for using the Course Management System! Goodbye!")
if __name__ == "__main__":
    run_demo()
