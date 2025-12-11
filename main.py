# main.py
from todo_list import manager


def print_menu() -> None:
    print("\n==== TO-DO LIST MANAGER ====")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Limpiar todas las tareas")
    print("0. Salir")


def handle_add_task() -> None:
    title = input("Título de la tarea: ").strip()
    description = input("Descripción de la tarea: ").strip()
    task = manager.add_new_task(title, description)
    print(f"\nTarea agregada correctamente con id {task.id}.")


def handle_list_tasks() -> None:
    tasks = manager.list_tasks()
    print()
    print(manager.format_tasks_for_display(tasks))


def handle_mark_completed() -> None:
    title = input("Título de la tarea a marcar como completada: ").strip()
    if manager.mark_task_completed(title):
        print(f'\nLa tarea "{title}" fue marcada como completada.')
    else:
        print(f'\nNo se encontró ninguna tarea con el título "{title}".')


def handle_delete_task() -> None:
    title = input("Título de la tarea a eliminar: ").strip()
    if manager.delete_task(title):
        print(f'\nLa tarea "{title}" fue eliminada.')
    else:
        print(f'\nNo se encontró ninguna tarea con el título "{title}".')


def handle_clear_tasks() -> None:
    confirm = input("¿Estás seguro de limpiar todas las tareas? (s/n): ").lower()
    if confirm == "s":
        manager.clear_tasks()
        print("\nTodas las tareas han sido eliminadas.")
    else:
        print("\nOperación cancelada.")


def main() -> None:
    while True:
        print_menu()
        option = input("Selecciona una opción: ").strip()

        if option == "1":
            handle_add_task()
        elif option == "2":
            handle_list_tasks()
        elif option == "3":
            handle_mark_completed()
        elif option == "4":
            handle_delete_task()
        elif option == "5":
            handle_clear_tasks()
        elif option == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
