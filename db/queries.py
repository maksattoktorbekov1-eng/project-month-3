CREATE_TASKS = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_text TEXT NOT NULL,
    created_at TEXT NOT NULL,
    completed INTEGER DEFAULT 0)
"""

INSERT_TASK = """INSERT INTO tasks (task_text, created_at) VALUES (?, ?)"""

SELECT_TASKS = """SELECT id, task_text, completed FROM tasks ORDER BY id DESC"""

SELECT_COMPLETED = """SELECT id, task_text, completed FROM tasks WHERE completed = 1 ORDER BY id DESC"""

SELECT_UNCOMPLETED = """SELECT id, task_text, completed FROM tasks WHERE completed = 0 ORDER BY id DESC"""

UPDATE_TASK_TEXT = """UPDATE tasks SET task_text = ?WHERE id = ?"""
 
 
UPDATE_TASK_COMPLETED = """UPDATE tasks SET completed = ?WHERE id = ?"""

DELETE_TASK = """DELETE FROM tasks WHERE id = ?"""

DELETE_COMPLETED = """DELETE FROM tasksWHERE completed = 1"""
