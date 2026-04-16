class ManagementSystem:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def enroll_student_in_course(self, student_id, course_code):
        # ADVANCED PYTHON: Using Lambda and filter to find objects
        student = next(filter(lambda s: s._user_id == student_id, self.students), None)
        course = next(filter(lambda c: c.course_code == course_code, self.courses), None)

        if student and course:
            course.students.append(student)
            student.enrolled_courses.append(course)
            print(f"Success: {student.name} enrolled in {course.course_code}")
        else:
            print("Error: Student or Course not found.")

    def get_students_in_course(self, course_code):
        course = next(filter(lambda c: c.course_code == course_code, self.courses), None)
        if not course:
            print(f"Course {course_code} not found.")
            return None
        return course.students
    
    def print_course_details(self, course_code):
        course = next(filter(lambda c: c.course_code == course_code, self.courses), None)
        if not course:
            print(f"Course {course_code} not found.")
            return
        
        print(f"\n--- Course Details for {course.course_code} ---")
        print(f"Instructor: {course.instructor.name}")
        print("\nEnrolled Students:")
        if not course.students:
            print("No students enrolled yet.")
        else:
            for s in course.students:
                print(f"  {s._user_id}: {s.name} (Major: {s.major})")

    def get_all_course_titles(self):
        # ADVANCED PYTHON: List Comprehension
        return [f"{c.course_code}: {c.title}" for c in self.courses]
