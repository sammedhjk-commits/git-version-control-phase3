"""A small task tracker used for Git version-control practice."""
from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Task:
    task_id: int
    title: str
    completed: bool = False


class TaskTracker:
    """In-memory task tracker with simple input validation."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        task = Task(self._next_id, title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> List[dict]:
        return [asdict(task) for task in self._tasks]

    def complete_task(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.task_id == task_id:
                task.completed = True
                return task
        raise KeyError(f"No task found with id {task_id}.")

    def remove_task(self, task_id: int) -> None:
        for index, task in enumerate(self._tasks):
            if task.task_id == task_id:
                del self._tasks[index]
                return
        raise KeyError(f"No task found with id {task_id}.")
