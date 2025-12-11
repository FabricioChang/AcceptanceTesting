# todo_list/storage.py
from typing import List, Optional
from .models import Task

# "Base de datos" en memoria
_tasks: List[Task] = []
_next_id: int = 1


def reset() -> None:
    """
    Reinicia la lista de tareas.
    Útil para pruebas o para limpiar todo.
    """
    global _tasks, _next_id
    _tasks = []
    _next_id = 1


def add_task(title: str, description: str) -> Task:
    """
    Crea y agrega una nueva tarea a la lista.
    """
    global _next_id, _tasks
    task = Task(id=_next_id, title=title, description=description)
    _tasks.append(task)
    _next_id += 1
    return task


def get_all_tasks() -> List[Task]:
    """
    Devuelve una copia de la lista de tareas.
    """
    return list(_tasks)


def find_task_by_title(title: str) -> Optional[Task]:
    """
    Busca una tarea por título. (Primera coincidencia)
    """
    for task in _tasks:
        if task.title == title:
            return task
    return None


def mark_task_completed_by_title(title: str) -> bool:
    """
    Marca como completada la tarea con el título dado.
    Devuelve True si la encontró y la marcó, False si no existía.
    """
    task = find_task_by_title(title)
    if task is None:
        return False
    task.mark_completed()
    return True


def delete_task_by_title(title: str) -> bool:
    """
    Elimina la tarea cuyo título coincida.
    Devuelve True si se eliminó algo, False si no existía.
    """
    global _tasks
    before = len(_tasks)
    _tasks = [t for t in _tasks if t.title != title]
    after = len(_tasks)
    return after < before


def clear_all_tasks() -> None:
    """
    Limpia completamente la lista de tareas.
    """
    global _tasks
    _tasks = []
