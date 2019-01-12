from task_manager import Task_Manager
from doubles import ObjectDouble, allow
from assembly_line import Assembly_Line
from worker import Worker

def randint_comp_A():
    return 1

def randint_comp_B():
    return 2

def randint_comp_none():
    return 3

def test_task_manager_allocates_workers_to_assembly_line():
    tm = Task_Manager()
    assert len(tm.workers) == 3
    assert all([len(pair) == 2 for pair in tm.workers])

def test_task_manager_allocates_component_A_to_worker_a1():
    tm = Task_Manager()
    tm.allocate_resources(randint_comp_A)
    assert 'A' in tm.workers[0][0].components
    assert 'A' not in tm.assembly_line.belt

def test_task_manager_allocates_component_B_to_worker_a1():
    tm = Task_Manager()
    tm.allocate_resources(randint_comp_A)
    tm.allocate_resources(randint_comp_B)
    assert 'A' in tm.workers[0][0].components
    assert 'B' in tm.workers[0][0].components
    assert not tm.workers[0][0].collecting_mode

def test_task_manager_does_not_allocate_identical_components_to_worker():
    tm = Task_Manager()
    tm.allocate_resources(randint_comp_A)
    tm.allocate_resources(randint_comp_A)
    assert tm.workers[0][0].components.count('A') == 1
    assert tm.workers[0][1].components.count('A') == 1

def test_task_manager_instructs_worker_to_place_widget_if_slot_empty():
    tm = Task_Manager()
    tm.allocate_resources(randint_comp_A)
    tm.allocate_resources(randint_comp_B)
    tm.allocate_resources(randint_comp_none)
    tm.allocate_resources(randint_comp_none)
    tm.allocate_resources(randint_comp_none)
    tm.allocate_resources(randint_comp_none)
    tm.allocate_resources(randint_comp_none)
    assert 'X' in tm.assembly_line.belt
