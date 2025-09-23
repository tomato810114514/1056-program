import json
from app.student import StudentUser
# Corrected Import: TeacherUser and Course now come from the same file.
from app.teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        self.next_lesson_id = 1
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # The logic here remains the same, but the source of the Course class has changed.
                # TODO: For each dictionary in data['students'], create a StudentUser object and append to self.students.
                # TODO: Do the same for teachers (creating TeacherUser objects).
                # TODO: Do the same for courses (creating Course objects).
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")

    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        data_to_save = {
            "students": [s.to_dict() for s in self.students],
            "teachers": [t.to_dict() for t in self.teachers],
            "courses": [c.to_dict() for c in self.courses],
        }

        try:
            with open(self.data_path, 'w') as f:
                json.dump(data_to_save, f, indent=4)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def register_new_student(self, reg_name, reg_instrument):
        """Registers a new student if possible and saves data."""
    
    # Generate a unique ID like "S1", "S2", etc.
        new_id = f"S{len(self.students) + 1}"

        new_student = StudentUser(user_id=new_id, name=reg_name, instrument=reg_instrument)

        self.students.append(new_student)
        self._save_data()

        return new_student