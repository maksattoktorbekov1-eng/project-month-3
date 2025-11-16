
CREATE_TASKS = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    created_at TEXT
)
"""

INSERT_TASK = "INSERT INTO tasks (task, created_at) VALUES (?, ?)"


SELECT_TASKS = "SELECT id, task, created_at FROM tasks"


UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"


DELETE_TASK = "DELETE FROM tasks WHERE id = ?"
