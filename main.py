import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = "ToDo List"
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)
    warning = ft.Text("", color="red")

    filter_type = "all"

    def load_tasks():
        task_list.controls.clear()
        for task_id, text, completed in main_db.get_tasks(filter_type):
            task_list.controls.append(create_task_row(task_id, text, completed))
        page.update()

    def create_task_row(task_id, text, completed):
        text_field = ft.TextField(value=text, read_only=True, expand=True)
        checkbox = ft.Checkbox(value=bool(completed),on_change=lambda e: toggle_completed(task_id, e.control.value))

        def enable_edit(_):
            text_field.read_only = False
            text_field.update()

        def save_edit(_):
            main_db.update_task_text(task_id, text_field.value)
            text_field.read_only = True
            page.update()

        return ft.Row([
            checkbox,
            text_field,
            ft.IconButton(ft.Icons.EDIT, on_click=enable_edit),
            ft.IconButton(ft.Icons.SAVE, on_click=save_edit),
        ])

    def toggle_completed(task_id, value):
        main_db.update_completed(task_id, int(value))
        load_tasks()

    def check_length(_):
        if len(task_input.value) >= 100:
            warning.value = "Максимальное количество символов: 100!"
        else:
            warning.value = ""
        page.update()

    def add_task(_):
        if not task_input.value:
            warning.value = "Поле пустое!"
            page.update()
            return

        task_id = main_db.add_task(task_input.value)
        task_list.controls.append(
            create_task_row(task_id, task_input.value, 0)
        )
        task_input.value = ""
        warning.value = ""
        page.update()

    task_input = ft.TextField(label="Введите задачу",expand=True,max_length=100,on_change=check_length)

    add_button = ft.IconButton(icon=ft.Icons.SEND, on_click=add_task)

    filter_buttons = ft.Row(
        [
            ft.ElevatedButton("Все", on_click=lambda e: set_filter("all")),
            ft.ElevatedButton("Невыполненные", on_click=lambda e: set_filter("uncompleted")),
            ft.ElevatedButton("Выполненные", on_click=lambda e: set_filter("completed")),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )

    def set_filter(f):
        nonlocal filter_type
        filter_type = f
        load_tasks()

    page.add(ft.Row([task_input, add_button]),warning,filter_buttons,task_list)

    load_tasks()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)
