from worker import Worker

def test_worker_initializes_with_no_components():
    w = Worker()
    assert w.components == []

def test_worker_initializes_in_collecting_mode():
    w = Worker()
    assert w.collecting_mode
