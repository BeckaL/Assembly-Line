from lib.worker import Worker
from doubles import ObjectDouble, allow
from lib.assembly_line import Assembly_Line

al = ObjectDouble(Assembly_Line)
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

w2 = Worker()

def test_worker_makes_widget_in_four_time_units():
    w2.store_component('A')
    w2.store_component('B')
    for i in range(5):
        w2.time_pass()
    assert w2.widgets == 'X'

def test_worker_places_widget_on_production_line():
    allow(al).add('X', 0)
    w2.place_widget(al, 0)
    assert w2.widgets == None
    assert w2.manufacturing_time == 4
    assert w2.components == []
