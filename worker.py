class Worker:

    def __init__(self, position, assembly_line):
        self.components = []
        self.collecting_mode = True
        self.widgets = None
        self.manufacturing_time = 4
        self.assembly_line = assembly_line
        self.position = position

    def store_component(self, object):
        if object not in self.components:
            self.components.append(object)
            if sorted(self.components) == ['A', 'B']:
                self.collecting_mode = False
            return True
        else:
            return False

    def time_pass(self):
        if self.manufacturing_time == 0:
            self.widgets = 'X'
        elif not self.collecting_mode:
            self.manufacturing_time -= 1

    def place_widget(self, widget):
        self.widgets = None
        self.manufacturing_time = 4
        self.components = []
        self.assembly_line.add(widget, self.position)
