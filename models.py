from abc import ABC, abstractmethod

# 1. ABSTRACTION: Abstract Base Class
class User(ABC):
    def __init__(self, user_id, name):
        self._user_id = user_id  # 2. ENCAPSULATION: Protected attribute
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    def get_details(self):
        return f"ID: {self._user_id}, Name: {self.name}"

# 3. INHERITANCE: Student and Instructor inherit from User
class Student(User):
    def __init__(self, user_id, name, major):
        super().__init__(user_id, name)
        self.major = major
        self.enrolled_courses = []

    def get_role(self):  # 4. POLYMORPHISM: Implementation of abstract method
        return "Student"

    def get_details(self): # Overriding method
        return f"[Student] {super().get_details()}, Major: {self.major}"

class Instructor(User):
    def __init__(self, user_id, name, department):
        super().__init__(user_id, name)
        self.department = department

    def get_role(self):
        return "Instructor"

    def get_details(self):
        return f"[Instructor] {super().get_details()}, Dept: {self.department}"

class Course:
    def __init__(self, course_code, title, instructor):
        self.course_code = course_code
        self.title = title
        self.instructor = instructor # Composition: Course has an Instructor
        self.students = []
