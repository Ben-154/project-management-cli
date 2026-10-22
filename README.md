# Project Management CLI

A Python command-line application for managing a small team workflow: **users**, **projects**, and **tasks**.  
All data is saved locally in a JSON file so your work persists between sessions.

This project was built for the **Summative Lab: Python Project Management CLI Tool** (Moringa School).

---

## Features

- Create and list **users**
- Add **projects** to a specific user
- Add **tasks** to a project
- Mark tasks as **complete**
- List projects for a user
- **Persist** data using JSON file I/O (`data/database.json`)
- **Unit tests** with pytest
- External package **`termcolor`** for clear terminal messages

---

## Requirements

- **Python** 3.10 or newer
- **pip** (Python package installer)
- **Git** (optional, for cloning the repository)

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Ben-154/project-management-cli.git
   cd project-management-cli
   ```

2. (Recommended) Create a virtual environment:

   ```bash
   python -m venv venv
   ```

   **Windows:**

   ```bash
   venv\Scripts\activate
   ```

   **macOS / Linux:**

   ```bash
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Show all commands:

```bash
python main.py --help
```

### Example workflow

```bash
python main.py add-user --name "Alex"
python main.py list-users
python main.py add-project --user "Alex" --title "CLI Tool"
python main.py list-projects --user "Alex"
python main.py add-task --project "CLI Tool" --title "Implement add-task"
python main.py complete-task --project "CLI Tool" --title "Implement add-task"
```

After you run commands, open `data/database.json` to confirm data was saved.

---

## Running tests

```bash
python -m pytest
```

Tests cover basic model behavior and JSON save/load logic.

---

## Project structure

```text
project-management-cli/
├── main.py              # CLI entry point (argparse)
├── models.py            # User, Project, Task classes
├── storage.py           # Load/save JSON data
├── data/
│   └── database.json    # Stored users, projects, tasks
├── tests/
│   └── test_basic.py    # Pytest unit tests
├── requirements.txt     # Python dependencies
├── Pipfile              # Pipenv dependency list
└── README.md            # Project documentation
```

---

## Dependencies

| Package   | Purpose                            |
|-----------|------------------------------------|
| termcolor | Colored success/error messages     |
| pytest    | Running unit tests (development)   |

Install via:

```bash
pip install -r requirements.txt
```

---

## Data format

Data is stored in `data/database.json` under a top-level `"users"` array. Each user has `"projects"`, and each project has `"tasks"` with `"title"` and `"complete"` fields.

---

## Troubleshooting

| Problem | What to try |
|--------|-------------|
| `python` not found | Use `py main.py ...` on Windows |
| Module not found (`termcolor`) | Run `pip install -r requirements.txt` |
| Project/user not found | Create the user before adding a project; create the project before adding a task |
| Tests fail | Run from the project root folder (where `main.py` is) |

---

## Author

- **Name:** Benedict Mutuku
- **Email:** benedict.mutuku@student.moringaschool.com
- **GitHub:** [Ben-154](https://github.com/Ben-154)
- **Repository:** https://github.com/Ben-154/project-management-cli

---

## License

This project is submitted for educational purposes as part of coursework.
