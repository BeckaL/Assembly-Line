from assembly_line import Assembly_Line

def test_assembly_line_initializes_with_default_size_belt():
    al = Assembly_Line()
    assert len(al.belt) == 3

def test_assembly_line_initializes_with_empty_belt():
    al = Assembly_Line()
    assert all([slot==None for slot in al.belt])
