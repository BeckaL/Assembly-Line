from worker import Worker

w = Worker()

def test_worker_initializes_with_no_components():
    assert w.components == []

def test_worker_initializes_in_collecting_mode():
    assert w.collecting_mode

def test_worker_initializes_without_a_completed_widget():
    assert w.widgets == None

def test_worker_stores_new_component():
    w.store_component('A')
    assert w.components == ['A']

def test_worker_with_two_components_not_in_collecting_mode():
    w.store_component('B')
    assert not w.collecting_mode

def test_worker_does_not_accept_two_identical_components():
    assert w.store_component('A') == False
    assert len(w.components) == 2

def test_worker_makes_widget_in_four_time_units():
    w2 = Worker()
    w2.store_component('A')
    w2.store_component('B')
    w2.time_pass()
    assert not w2.collecting_mode
    for i in range(4):
        w2.time_pass()
    assert w2.widgets == 'X'
