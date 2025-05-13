import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

   
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task, reminder_time=None):
        if task.strip():
            self.tasks.append({"task": task.strip(), "is_completed": False, "reminder_time": reminder_time, "reminded": False})
            self.save_tasks()  

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["is_completed"] = not self.tasks[index]["is_completed"]
            self.save_tasks()  

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()  

    def get_tasks(self):
        return self.tasks

    def get_remaining_count(self):
        return len([t for t in self.tasks if not t["is_completed"]])

    def get_filtered_tasks(self, filter_type):
        if filter_type == "all":
            return self.tasks
        elif filter_type == "active":
            return [task for task in self.tasks if not task["is_completed"]]
        elif filter_type == "completed":
            return [task for task in self.tasks if task["is_completed"]]
        else:
            return []
