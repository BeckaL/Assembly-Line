import random
import mock
from lib.assembly_line import Assembly_Line

def patched_randints():
    return 1

al = Assembly_Line()

def test_assembly_line_initializes_with_default_size_belt():
    assert len(al.belt) == 3

def test_assembly_line_initializes_with_empty_belt():
    assert all([slot==None for slot in al.belt])

def test_item_generator_generates_components():
    al = Assembly_Line()
    assert al.new_component(randint = patched_randints) == 'A'

def test_time_unit_produces_new_component_in_slot_1():
    al.time_pass(randint = patched_randints)
    assert al.belt[0] == 'A'

def test_time_unit_keeps_belt_length_the_same():
    al.time_pass()
    assert len(al.belt) == 3

def test_widget_count_increases():
    al.belt[2] = 'X'
    al.time_pass()
    assert al.widgets_count == 1

def test_widget_added_to_line():
    al.add('X', 0)
    assert al.belt[0] == 'X'
