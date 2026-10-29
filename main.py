"""Command-line entry point for the Git practice project."""
from src.task_tracker import TaskTracker


def main() -> None:
    tracker = TaskTracker()
    print("Gitflow Practice — Task Tracker")
    print("Add a sample task and show it:")
    tracker.add_task("Create a feature branch")
    for task in tracker.list_tasks():
        status = "done" if task["completed"] else "open"
        print(f'#{task["task_id"]}: {task["title"]} [{status}]')


if __name__ == "__main__":
    main()
