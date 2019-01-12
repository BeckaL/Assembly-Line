class Worker:

    def __init__(self):
        self.components = []
        self.collecting_mode = True
        self.widgets = None
        self.manufacturing_time = 4

    def store_component(self, object):
        self.components.append(object)
        if sorted(self.components) == ['A', 'B']:
            self.collecting_mode = False

    def time_pass(self, randint = None):
        if self.manufacturing_time == 0:
            self.widgets = 'X'
        elif not self.collecting_mode:
            self.manufacturing_time -= 1

    def place_widget(self, assembly_line, position):
        assembly_line.add(self.widgets, position)
        self.widgets = None
        self.manufacturing_time = 4
        self.components = []
