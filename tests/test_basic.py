from models import User
import storage


def test_user_project_task():
    user = User("Alex")
    user.add_project("CLI Tool")
    project = user.find_project("CLI Tool")
    project.add_task("Implement add-task")
    assert len(user.projects) == 1
    assert project.tasks[0].title == "Implement add-task"


def test_save_and_load(tmp_path, monkeypatch):
    test_file = tmp_path / "database.json"
    monkeypatch.setattr(storage, "DATA_FILE", str(test_file))

    user = User("Alex")
    user.add_project("CLI Tool")
    storage.save_users([user])

    loaded = storage.load_users()
    assert loaded[0].name == "Alex"
    assert loaded[0].projects[0].title == "CLI Tool"