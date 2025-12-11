# todo_list/manager.py
from typing import List
from . import storage
from .models import Task


def add_new_task(title: str, description: str) -> Task:
    """
    Agrega una nueva tarea usando el módulo de almacenamiento.
    """
    return storage.add_task(title, description)


def list_tasks() -> List[Task]:
    """
    Devuelve todas las tareas existentes.
    """
    return storage.get_all_tasks()


def mark_task_completed(title: str) -> bool:
    """
    Marca una tarea como completada.
    Devuelve True si se encontró, False en caso contrario.
    """
    return storage.mark_task_completed_by_title(title)


def delete_task(title: str) -> bool:
    """
    Elimina una tarea por título.
    Devuelve True si se eliminó, False si no existe.
    """
    return storage.delete_task_by_title(title)


def clear_tasks() -> None:
    """
    Borra todas las tareas.
    """
    storage.clear_all_tasks()


def format_tasks_for_display(tasks: List[Task]) -> str:
    """
    Devuelve un string ‘bonito’ para mostrar las tareas por consola.
    """
    if not tasks:
        return "No hay tareas en la lista."

    lines = ["Tasks:"]
    for task in tasks:
        lines.append(
            f"[{task.id}] {task.title} - {task.status} "
            f"(creada: {task.created_at:%Y-%m-%d %H:%M})"
        )
        if task.description:
            lines.append(f"    Descripción: {task.description}")
    return "\n".join(lines)
