class Worker:

    def __init__(self, position):
        self.components = []
        self.collecting_mode = True
        self.widgets = None
        self.manufacturing_time = 4
        self.position = position

    def store_component(self, object):
        self.components.append(object)
        if sorted(self.components) == ['A', 'B']:
            self.collecting_mode = False

    def time_pass(self, randint = None):
        if self.manufacturing_time == 0:
            self.widgets = 'X'
        elif not self.collecting_mode:
            self.manufacturing_time -= 1

    def place_widget(self, widget, assembly_line):
        self.widgets = None
        self.manufacturing_time = 4
        self.components = []
        assembly_line.add(widget, self.position)
