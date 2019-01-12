class Worker:

    def __init__(self):
        self.components = []
        self.collecting_mode = True
        self.widgets = None
        self.manufacturing_time = 4

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
