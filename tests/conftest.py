import pytest
from pathlib import Path

from queue_test.queue import Queue


@pytest.fixture(scope="session")
def local_queue(request):
    path = Path(__file__).parent.joinpath("test_queue.pkl")
    local_queue = Queue(path)

    def teardown():
        if path.exists():
            path.unlink()

    request.addfinalizer(teardown)
    return local_queue
