from worker import Worker
from doubles import ObjectDouble, allow
from assembly_line import Assembly_Line

al = ObjectDouble(Assembly_Line)
w = Worker(0, al)

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

w2 = Worker(0, al)
def test_worker_makes_widget_in_four_time_units():
    w2.store_component('A')
    w2.store_component('B')
    for i in range(5):
        w2.time_pass()
    assert w2.widgets == 'X'

def test_worker_places_widget_on_production_line():
    allow(al).add('X', 0)
    w2.place_widget('X')
    assert w2.widgets == None
    assert w2.manufacturing_time == 4
    assert w2.components == []
