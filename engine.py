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
            print(f"Success: {student.name} enrolled in {course.title}")
        else:
            print("Error: Student or Course not found.")

    def get_all_course_titles(self):
        # ADVANCED PYTHON: List Comprehension
        return [f"{c.course_code}: {c.title}" for c in self.courses]
