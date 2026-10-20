class Task:
    def __init__(self, title):
        self.title = title
        self.complete = False

    def to_dict(self):
        return {"title": self.title, "complete": self.complete}

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"])
        task.complete = data.get("complete", False)
        return task


class Project:
    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Task(title))

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete = True
                return True
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "tasks": [t.to_dict() for t in self.tasks],
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data["title"])
        project.tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return project


class User:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, title):
        self.projects.append(Project(title))

    def find_project(self, title):
        for project in self.projects:
            if project.title.lower() == title.lower():
                return project
        return None

    def to_dict(self):
        return {
            "name": self.name,
            "projects": [p.to_dict() for p in self.projects],
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"])
        user.projects = [Project.from_dict(p) for p in data.get("projects", [])]
        return user