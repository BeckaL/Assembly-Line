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

    def progress_time(self, randint = None):
        self.belt.insert(0, self.new_component(randint))
        last_item = self.belt.pop()
        self.widget_check(last_item)

    def widget_check(self, item):
        if item == 'X':
            self.widgets_count += 1
