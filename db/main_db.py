import sqlite3
from datetime import datetime
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TASKS)
    conn.commit()
    conn.close()


def add_task(task_text):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(queries.INSERT_TASK, (task_text, created_at))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def get_tasks(filter_type="all"):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == "completed":
        cursor.execute(queries.SELECT_COMPLETED)
    elif filter_type == "uncompleted":
        cursor.execute(queries.SELECT_UNCOMPLETED)
    else:
        cursor.execute(queries.SELECT_TASKS)

    tasks = cursor.fetchall()
    conn.close()
    return tasks


def update_task_text(task_id, new_text):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK_TEXT, (new_text, task_id))
    conn.commit()
    conn.close()


def update_completed(task_id, completed):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK_COMPLETED, (completed, task_id))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()


def delete_completed_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_COMPLETED)
    conn.commit()
    conn.close()
