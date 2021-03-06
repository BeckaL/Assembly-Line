import random
class Assembly_Line:

    def __init__(self, length = 3):
        self.belt = [None] * length
        self.widgets_count = 0

    def new_component(self, randint = None):
        components = {1: 'A', 2: 'B', 3: None}
        if randint is None:
            random_n = random.randint(1, 3)
        else:
            random_n = randint()
        return components[random_n]

    def time_pass(self, randint = None):
        self.belt.insert(0, self.new_component(randint))
        self._widget_check(self.belt.pop())

    def _widget_check(self, item):
        if item == 'X':
            self.widgets_count += 1

    def add(self, item, position):
        self.belt[position] = item

    def remove(self, position):
        self.belt[position] = None
