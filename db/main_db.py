import sqlite3
from db import qeries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(qeries.CREATE_TASKS)
    print('База данных подключена!')
    conn.commit()
    conn.close()

def add_task(task, created_at):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(qeries.INSERT_TASK, (task, created_at))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def get_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(qeries.SELECT_TASKS)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(qeries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(qeries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()
