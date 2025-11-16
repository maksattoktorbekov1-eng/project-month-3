from db import main_db
import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'ToDo List'
    page.theme_mode = ft.ThemeMode.LIGHT  
    task_list = ft.Column(spacing=10)

    
    def load_task():
        task_list.controls.clear()
        for task_id, task_text, created_at in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id, task_text, created_at))
        page.update()

    def create_task_row(task_id, task_text, created_at):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        def enable_edit(_):
            task_field.read_only = False
            task_field.update()

        enable_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            task_field.update()
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        task_display = ft.Text(f"({created_at})")

        return ft.Row([task_field, enable_button, save_button, task_display])

   
    def add_task(_):
        text = task_input.value.strip()
        if not text:
            page.snack_bar = ft.SnackBar(ft.Text("Введите текст задачи!"))
            page.snack_bar.open = True
            page.update()
            return

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_id = main_db.add_task(task=text, created_at=created_at)
        task_list.controls.append(create_task_row(task_id, text, created_at))
        task_input.value = ""
        page.update()

  
    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.icon = ft.Icons.BRIGHTNESS_2  
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.icon = ft.Icons.WB_SUNNY  
        page.update()

    task_input = ft.TextField(label="Введите новую задачу", expand=True, on_submit=add_task)
    add_button = ft.IconButton(icon=ft.Icons.SEND, on_click=add_task)
    theme_button = ft.IconButton(icon=ft.Icons.WB_SUNNY, on_click=toggle_theme)

    page.add(
        ft.Row([theme_button, task_input, add_button], alignment=ft.MainAxisAlignment.START),
        task_list
    )

    load_task()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)
