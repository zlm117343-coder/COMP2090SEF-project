from models import Student, Instructor, Course
from engine import ManagementSystem

def run_demo():
    sys = ManagementSystem()

    # Create Users
    prof_smith = Instructor("I001", "Dr. Smith", "Computer Science")
    alice = Student("S101", "Alice Wong", "IT")
    bob = Student("S102", "Bob Chen", "Data Science")

    # Create Courses
    c1 = Course("COMP2090", "Data Structures", prof_smith)
    c2 = Course("COMP1001", "Python Programming", prof_smith)

    # Setup System
    sys.add_student(alice)
    sys.add_student(bob)
    sys.add_course(c1)
    sys.add_course(c2)

    # Enrollment
    sys.enroll_student_in_course("S101", "COMP2090")
    sys.enroll_student_in_course("S102", "COMP2090")

    print("\n--- Course List ---")
    print(sys.get_all_course_titles())

    print("\n--- User Details (Polymorphism) ---")
    users = [prof_smith, alice]
    for u in users:
        # Calls the specific get_details() based on object type
        print(u.get_details())

if __name__ == "__main__":
    run_demo()
