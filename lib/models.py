# Task and User classes for the CLI task manager

class Task:
    def __init__(self, title):
        # Store the task's title
        self.title = title
        # Tasks start out incomplete
        self.completed = False

    def complete(self):
        # Mark the task as complete
        self.completed = True
        # Print confirmation
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        # Store the user's name
        self.name = name
        # Each user starts with an empty task list
        self.tasks = []

    def add_task(self, task):
        # Add the task to this user's task list
        self.tasks.append(task)
        # Confirm the task was added
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Search this user's tasks for a matching title
        for task in self.tasks:
            if task.title == title:
                return task
        # No match found
        return None
