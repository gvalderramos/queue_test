"""
queue.py

This module defines a priority-based command queue system with persistence support.

Classes:
    Command: Represents a command with a string and a priority level.
    Queue: Implements a priority queue with persistence using pickle.

Usage:
    Create a `Queue` object to manage commands. Use `add()` to add commands to the queue, and `next()` 
    to retrieve and remove commands in priority order.

    Example::
    
        from queue import Queue
        
        # Create a queue
        q = Queue()

        # Add commands to the queue
        q.add({"cmd": "Start backup", "priority": 2})
        q.add({"cmd": "Restart server", "priority": 1})

        # Process commands in priority order
        for command in q:
            print(command.cmd, command.priority)

Details:
    The queue state is persisted to a file (default: `queue.pkl` in the current directory), allowing the 
    queue to retain its state across program executions. Command priorities must be integers between 1 
    and 10, where 1 represents the highest priority.
"""
import pickle
from pathlib import Path
from dataclasses import dataclass
from typing import Optional


@dataclass
class Command:
    """Represents a command with an associated priority."""

    cmd: str
    priority: int


class Queue:
    """A priority-based queue that supports persistence using pickle."""

    def __init__(self, queue: Optional[Path] = None):
        """Initializes the queue and optionally sets a custom file for persistence.

        Args:
            queue (Optional[Path]): Path to the file used for queue persistence. Defaults to 'queue.pkl' in the current directory.
        """
        self._queue = []
        self._queue_file = queue or Path(__file__).parent.joinpath("queue.pkl")
        self._load()

    def __iter__(self):
        """Allows iteration over the queue by returning commands in order of priority.

        Yields:
            Command: The next command in the queue.
        """
        for _ in range(len(self)):
            yield self.next()

    def __len__(self):
        """Returns the number of commands in the queue.

        Returns:
            int: The number of commands currently in the queue.
        """
        return len(self._queue)

    def _store(self) -> None:
        """Saves the current state of the queue to a file using pickle."""
        with open(self._queue_file, "wb") as db:
            pickle.dump(self._queue, db)

    def _load(self) -> None:
        """Loads the queue state from a file if it exists."""
        if self._queue_file.exists():
            with open(self._queue_file, "rb") as db:
                self._queue = pickle.load(db)

    def add(self, command: dict) -> None:
        """Adds a new command to the queue. Commands are sorted by priority after being added.

        Args:
            command (dict): A dictionary with "cmd" (str) and "priority" (int, 1-10) keys.

        Raises:
            RuntimeError: If the priority is not between 1-10 or if the dictionary structure is incorrect.
        """
        if "cmd" in command and "priority" in command:
            if 1 <= command["priority"] <= 10:
                self._queue.append(Command(command["cmd"], command["priority"]))
                self._queue.sort(key=lambda x: x.priority)
            else:
                raise RuntimeError(f"Command priority out of scale")
        else:
            raise RuntimeError(
                f"It expect a dictionary with 'cmd' and 'priority' keys. Got {command.keys()}"
            )

        self._store()

    def next(self) -> Optional[Command]:
        """Retrieves and removes the next command from the queue.

        Returns:
            Optional[Command]: The next command in the queue, or None if the queue is empty.
        """
        if self._queue:
            item = self._queue.pop(0)
            self._store()
            return item
