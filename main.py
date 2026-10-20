import argparse

from termcolor import colored

from models import User
from storage import load_users, save_users


def find_user(users, name):
    for user in users:
        if user.name.lower() == name.lower():
            return user
    return None


def find_project(users, project_name):
    for user in users:
        for project in user.projects:
            if project.title.lower() == project_name.lower():
                return user, project
    return None, None


def add_user(name):
    users = load_users()
    if find_user(users, name):
        print(colored(f"User '{name}' already exists.", "red"))
        return
    users.append(User(name))
    save_users(users)
    print(colored(f"Added user: {name}", "green"))


def list_users():
    users = load_users()
    if not users:
        print("No users yet.")
        return
    print("Users:")
    for user in users:
        print(f"  - {user.name} ({len(user.projects)} projects)")


def add_project(user_name, title):
    users = load_users()
    user = find_user(users, user_name)
    if not user:
        print(colored(f"User '{user_name}' not found.", "red"))
        return
    user.add_project(title)
    save_users(users)
    print(colored(f"Added project '{title}' for {user_name}.", "green"))


def list_projects(user_name):
    users = load_users()
    user = find_user(users, user_name)
    if not user:
        print(colored(f"User '{user_name}' not found.", "red"))
        return
    if not user.projects:
        print(f"{user_name} has no projects.")
        return
    print(f"Projects for {user_name}:")
    for project in user.projects:
        print(f"  - {project.title} ({len(project.tasks)} tasks)")


def add_task(project_name, title):
    users = load_users()
    owner, project = find_project(users, project_name)
    if not project:
        print(colored(f"Project '{project_name}' not found.", "red"))
        return
    project.add_task(title)
    save_users(users)
    print(colored(f"Added task '{title}' to '{project_name}'.", "green"))


def complete_task(project_name, title):
    users = load_users()
    _, project = find_project(users, project_name)
    if not project:
        print(colored(f"Project '{project_name}' not found.", "red"))
        return
    if project.complete_task(title):
        save_users(users)
        print(colored(f"Task '{title}' marked complete.", "green"))
    else:
        print(colored(f"Task '{title}' not found.", "red"))


def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("add-user", help="Create a user")
    p1.add_argument("--name", required=True)

    sub.add_parser("list-users", help="List all users")

    p2 = sub.add_parser("add-project", help="Add a project to a user")
    p2.add_argument("--user", required=True)
    p2.add_argument("--title", required=True)

    p3 = sub.add_parser("list-projects", help="List projects for a user")
    p3.add_argument("--user", required=True)

    p4 = sub.add_parser("add-task", help="Add a task to a project")
    p4.add_argument("--project", required=True)
    p4.add_argument("--title", required=True)

    p5 = sub.add_parser("complete-task", help="Mark a task complete")
    p5.add_argument("--project", required=True)
    p5.add_argument("--title", required=True)

    args = parser.parse_args()

    if args.command == "add-user":
        add_user(args.name)
    elif args.command == "list-users":
        list_users()
    elif args.command == "add-project":
        add_project(args.user, args.title)
    elif args.command == "list-projects":
        list_projects(args.user)
    elif args.command == "add-task":
        add_task(args.project, args.title)
    elif args.command == "complete-task":
        complete_task(args.project, args.title)


if __name__ == "__main__":
    main()