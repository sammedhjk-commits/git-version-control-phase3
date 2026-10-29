import unittest
from src.task_tracker import TaskTracker


class TaskTrackerTests(unittest.TestCase):
    def setUp(self):
        self.tracker = TaskTracker()

    def test_add_task_trims_title_and_assigns_id(self):
        task = self.tracker.add_task("  Write tests  ")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Write tests")
        self.assertFalse(task.completed)

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            self.tracker.add_task("   ")

    def test_complete_task(self):
        task = self.tracker.add_task("Review pull request")
        completed = self.tracker.complete_task(task.task_id)
        self.assertTrue(completed.completed)

    def test_missing_task_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.tracker.complete_task(999)

    def test_remove_task(self):
        task = self.tracker.add_task("Temporary task")
        self.tracker.remove_task(task.task_id)
        self.assertEqual(self.tracker.list_tasks(), [])


if __name__ == "__main__":
    unittest.main()
