# todo_list/models.py
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """
    Representa una tarea del To-Do List.
    """
    id: int
    title: str
    description: str
    status: str = "Pending"  # "Pending" o "Completed"
    created_at: datetime = field(default_factory=datetime.now)

    def mark_completed(self) -> None:
        """Marca la tarea como completada."""
        self.status = "Completed"
