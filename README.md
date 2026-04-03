# COMP2090SEF-project
# University Course Management System
**HKMU COMP2090SEF/8090SEF Group Project**

## 📌 Project Overview
This project is a terminal-based Management System designed to handle university courses, instructors, and student enrollments. The project is divided into two main tasks:
1. **Task 1:** An OOP-based application using Inheritance, Abstraction, and Polymorphism.
2. **Task 2:** A self-study implementation of a **Graph Data Structure** and the **Breadth-First Search (BFS)** algorithm.

## 📂 File Structure
To comply with the modular programming requirement, the code is split into:
- `models.py`: Contains the Data Models (Classes, Inheritance, Abstraction).
- `engine.py`: Contains the system logic (Enrollment, Filtering, List Comprehensions).
- `main.py`: The entry point to run the demonstration.
- `task2_graph.py`: Implementation of the Graph and BFS algorithm.

## 🛠️ OOP Concepts Applied
- **Abstraction:** Used `ABC` for the base `User` class.
- **Inheritance:** `Student` and `Instructor` classes inherit from `User`.
- **Encapsulation:** Used protected attributes (e.g., `_user_id`) to manage data access.
- **Polymorphism:** The `get_details()` method is overridden in subclasses to provide specific information.

## 🚀 How to Run
1. Ensure you have **Python 3.x** installed.
2. Clone this repository or download the files.
3. Open your terminal/command prompt.
4. Navigate to the project folder and run:
   ```bash
   python main.py
