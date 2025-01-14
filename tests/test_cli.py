from typer.testing import CliRunner
import json


from pathlib import Path
import pytest
from unittest import mock

from queue_test.queue import Queue
from queue_test.cli import app


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(local_queue, runner):
    with mock.patch("queue_test.queue.Queue", lambda: local_queue):
        cmd = {"cmd": "test cmd", "priority": 1}
        result = runner.invoke(app, ["add", json.dumps(cmd)])
        assert result.exit_code == 0

        result = runner.invoke(app, ["run"])
        assert result.exit_code == 0
        assert "priority: 1" in result.stdout
        assert "test cmd" in result.stdout
