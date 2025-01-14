"""Console script for managing the command queue.

This script provides a command-line interface (CLI) to interact with the
`queue_test.queue` module. Users can add commands to the queue and run
all queued commands in priority order.

Commands:
    add: Adds a new command to the queue.
    run: Processes and displays all commands in the queue.

Usage:
    Add a command:
        python cli.py add '{"cmd": "Task description", "priority": 1}'

    Run the queue:
        python cli.py run
"""
import json
import time
from typing import Optional

import typer
from rich.console import Console

import queue_test.queue

app = typer.Typer()
console = Console()


@app.command()
def add(value: Optional[str] = typer.Argument(default=None)):
    """
    Adds a new command to the queue.

    Args:
        value (Optional[str]): A JSON string containing the command data.
                               Example: '{"cmd": "Task description", "priority": 1}'
    """
    data = json.loads(value)
    queue = queue_test.queue.Queue()
    queue.add(data)


@app.command()
def run():
    """
    Processes and displays all commands in the queue in priority order.

    This function retrieves commands from the queue, prints their details,
    and processes them with a small delay to simulate execution.
    """
    queue = queue_test.queue.Queue()
    console.print(f"Queue size: {len(queue)}")

    for cmd in queue:
        txt = f"- Command: {cmd.cmd}"
        cmd_txt = f"{txt:{'.'}<40}"
        console.print(f"{cmd_txt}priority: {cmd.priority}")
        time.sleep(0.1)

    console.print("The whole queue was ran sucessifully.", style="bold green")


if __name__ == "__main__":
    app()
