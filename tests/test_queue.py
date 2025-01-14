#!/usr/bin/env python

"""Tests for `queue_test` package."""
from pathlib import Path
import random
import pytest

from queue_test.queue import Queue


def test_add_content(local_queue):
    right_model = {"cmd": "test cmd", "priority": 1}
    local_queue.add(right_model)
    cmd = local_queue.next()
    assert cmd.cmd == "test cmd"
    assert cmd.priority == 1

    wrong_model = {"cmd1": "test cmd", "prioritydfds": 1}
    with pytest.raises(RuntimeError):
        local_queue.add(wrong_model)


def test_wrong_scale(local_queue):
    wrong_model = {"cmd": "test cmd", "priority": 0}
    with pytest.raises(RuntimeError):
        local_queue.add(wrong_model)

    wrong_model = {"cmd": "test cmd", "priority": 11}
    with pytest.raises(RuntimeError):
        local_queue.add(wrong_model)


def test_priority_test(local_queue):
    cmds = [{"cmd": "test cmd", "priority": random.randint(1, 10)} for _ in range(10)]
    for cmd in cmds:
        local_queue.add(cmd)

    last_prio = None
    for queue_cmd in local_queue:
        if last_prio is None:
            last_prio = queue_cmd.priority
        assert queue_cmd.priority >= last_prio
        last_prio = queue_cmd.priority


def test_load_right_queue():
    path = Path(__file__).parent.joinpath("test_queue.pkl")
    queue_01 = Queue(path)
    queue_01.add({"cmd": "test load right queue", "priority": 1})

    queue_02 = Queue(path)
    cmd = queue_02.next()
    assert cmd
    assert cmd.priority == 1
    assert cmd.cmd == "test load right queue"
