from task_manager import Task_Manager
from doubles import ObjectDouble, allow
from assembly_line import Assembly_Line
from worker import Worker
import pytest

#Setup

def randint_comp_A():
    return 1

def randint_comp_B():
    return 2

def randint_comp_none():
    return 3

def generate_two_components(tm, identical = False):
    tm.allocate_resources(randint_comp_A)
    if identical:
        tm.allocate_resources(randint_comp_A)
    else:
        tm.allocate_resources(randint_comp_B)

@pytest.fixture(autouse=True)
def new_tm():
    return Task_Manager()

#Tests

def test_task_manager_allocates_workers_to_assembly_line(new_tm):
    assert len(new_tm.workers) == 3
    assert all([len(pair) == 2 for pair in new_tm.workers])

def test_task_manager_allocates_component_A_to_worker_a1(new_tm):
    new_tm.allocate_resources(randint_comp_A)
    first_worker = new_tm.workers[0][0]
    assert 'A' in first_worker.components
    assert 'A' not in new_tm.assembly_line.belt

def test_task_manager_allocates_component_B_to_worker_a1(new_tm):
    generate_two_components(new_tm, identical = False)
    first_worker = new_tm.workers[0][0]
    assert 'A' in first_worker.components
    assert 'B' in first_worker.components
    assert not first_worker.collecting_mode

def test_task_manager_does_not_allocate_identical_components_to_worker(new_tm):
    generate_two_components(new_tm, identical = True)
    first_worker = new_tm.workers[0][0]
    second_worker = new_tm.workers[0][1]
    assert first_worker.components.count('A') == 1
    assert second_worker.components.count('A') == 1

def test_task_manager_instructs_worker_to_place_widget_if_slot_empty(new_tm):
    generate_two_components(new_tm, identical = False)
    for i in range(5):
        new_tm.allocate_resources(randint_comp_none)
    assert 'X' in new_tm.assembly_line.belt
