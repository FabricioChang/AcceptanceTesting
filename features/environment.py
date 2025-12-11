# features/environment.py

from todo_list import storage

def before_scenario(context, scenario):
    """
    Este método se ejecuta automáticamente ANTES de cada escenario.
    Reiniciamos la lista de tareas para garantizar aislamiento.
    """
    storage.reset()
