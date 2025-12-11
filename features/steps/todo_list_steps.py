# features/steps/todo_list_steps.py

from behave import given, when, then
from todo_list import manager, storage


# ========= Helpers internos =========

def _task_titles():
    """Devuelve la lista de títulos de todas las tareas actuales."""
    return [t.title for t in manager.list_tasks()]


# ========= GIVEN =========

@given("the to-do list is empty")
def step_given_todo_list_empty(context):
    # Reiniciamos el almacenamiento y dejamos todo vacío
    storage.reset()


@given("the to-do list contains tasks:")
def step_given_todo_list_contains_tasks(context):
    """
    Tabla esperada (puede ser con o sin columna Status):

    | Task          |
    | Buy groceries |
    | Pay bills     |

    o

    | Task          | Status  |
    | Buy groceries | Pending |
    """
    storage.reset()

    # Detectar columnas presentes
    has_status = "Status" in context.table.headings

    for row in context.table:
        title = row["Task"]
        # Puedes poner una descripción simple o vacía
        description = f"Auto-generated description for {title}"
        task = manager.add_new_task(title, description)

        if has_status:
            status = row["Status"]
            if status.lower() == "completed":
                task.mark_completed()


# ========= WHEN =========

@when('the user adds a task "{title}"')
def step_when_user_adds_task(context, title):
    # Descripción vacía o genérica
    manager.add_new_task(title, description=f"Description for {title}")


@when("the user lists all tasks")
def step_when_user_lists_all_tasks(context):
    # Guardamos el output formateado en context
    tasks = manager.list_tasks()
    context.output = manager.format_tasks_for_display(tasks)


@when('the user marks task "{title}" as completed')
def step_when_user_marks_task_completed(context, title):
    manager.mark_task_completed(title)


@when("the user clears the to-do list")
def step_when_user_clears_list(context):
    manager.clear_tasks()


@when('the user deletes the task "{title}"')
def step_when_user_deletes_task(context, title):
    manager.delete_task(title)


# ========= THEN =========

@then('the to-do list should contain "{title}"')
def step_then_list_should_contain_task(context, title):
    titles = _task_titles()
    assert title in titles, f'Expected "{title}" in {titles}, but it was not found.'


@then("the output should contain:")
def step_then_output_should_contain(context):
    """
    En el feature pusimos algo como:

      Then the output should contain:
        \"\"\"
        Tasks:
        - Buy groceries
        - Pay bills
        \"\"\"

    Aquí validamos que cada ítem de la lista aparezca en el string output,
    ignorando el formato exacto de guiones, etc.
    """
    expected_block = context.text
    # Por seguridad, si no se ejecutó el step de listar antes:
    if not hasattr(context, "output"):
        tasks = manager.list_tasks()
        context.output = manager.format_tasks_for_display(tasks)

    output = context.output

    # Recorremos cada línea "útil" del bloque esperado
    for line in expected_block.splitlines():
        line = line.strip()
        if not line:
            continue

        # Si la línea empieza con '- ', nos quedamos solo con el título
        if line.startswith("- "):
            expected_text = line[2:].strip()
        else:
            expected_text = line

        assert expected_text in output, (
            f'Expected "{expected_text}" to be in:\n{output}'
        )


@then('the to-do list should show task "{title}" as completed')
def step_then_task_should_be_completed(context, title):
    tasks = manager.list_tasks()
    target = None
    for t in tasks:
        if t.title == title:
            target = t
            break

    assert target is not None, f'Task "{title}" not found in {tasks}'
    assert target.status == "Completed", (
        f'Task "{title}" is not completed. Current status: {target.status}'
    )


@then("the to-do list should be empty")
def step_then_list_should_be_empty(context):
    tasks = manager.list_tasks()
    assert len(tasks) == 0, f"Expected empty list, but found {len(tasks)} tasks."


@then('the to-do list should not contain "{title}"')
def step_then_list_should_not_contain_task(context, title):
    titles = _task_titles()
    assert title not in titles, f'Expected "{title}" to be removed, but it is still in {titles}'
