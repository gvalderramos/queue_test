Usage
=====

This guide explains how to use the queue management system provided by the `queue.py` module and interact with it via the command-line interface (CLI) defined in `cli.py`.

Queue Module
------------

The `queue.py` module provides a priority-based queue system with persistence support. 

Features:
---------
- Add commands with a priority (1-10).
- Automatically sorts commands based on priority.
- Stores and loads the queue state using a file (`queue.pkl`).

Example Usage:
--------------

..  code-block:: python

    from queue_test.queue import Queue

    # Initialize a queue
    queue = Queue()

    # Add commands to the queue
    queue.add({"cmd": "Start backup", "priority": 2})
    queue.add({"cmd": "Restart server", "priority": 1})

    # Process commands
    for command in queue:
        print(f"Command: {command.cmd}, Priority: {command.priority}")


Command-Line Interface (CLI)
-----------------------------

The `cli.py` script provides a simple CLI for interacting with the queue system.

Installation:
-------------
Ensure `queue_test` is in your Python path, and install required dependencies:

.. code-block:: bash

    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements_dev.txt
    pip install .

Commands:
---------
``add``
~~~~~~~

Adds a new command to the queue.

**Usage**:

.. code-block:: bash

    python cli.py add '{"cmd": "Task description", "priority": 1}'

**Example**:

.. code-block:: bash

    python cli.py add '{"cmd": "Run diagnostics", "priority": 5}'

This will add the command "Run diagnostics" with a priority of 5 to the queue.

``run``
~~~~~~~

Processes all commands in the queue in priority order.

**Usage**:

.. code-block:: bash

    python cli.py run

**Example Output**:

.. code-block::

    Queue size: 2
    - Command: Task description...............priority: 1
    - Command: Run diagnostics................priority: 5
    The whole queue was ran successfully.

How It Works:
-------------
- The `run` command retrieves and removes each command from the queue, printing details to the console in priority order.
- After processing, the queue is emptied.

Notes:
------
- Command priorities must be integers between 1 and 10. Lower numbers indicate higher priority.
- The queue state is persisted in a file (`queue.pkl`) to maintain data across runs.

Feel free to reach out for more information or enhancements.
