from assembly_line import Assembly_Line
from worker import Worker

class Task_Manager():

    def __init__(self, assembly_line = Assembly_Line(), worker = Worker):
         self.assembly_line = assembly_line
         self.worker = worker
         self.workers = self.assign_workers()

    def assign_workers(self):
        return [[self.worker(i), self.worker(i)] for i in range(len(self.assembly_line.belt))]

    def try_worker_with_component(self, type, worker, idx):
        if not type in worker.components:
            worker.store_component(type)
            print("worker {} of pair {} takes element {}".format(idx[1], idx[0], type))
            self.assembly_line.remove(idx[0])
            return True

    def attempt_component_allocation(self, type, pair, idx):
        for ind_index, worker in enumerate(pair):
            if self.try_worker_with_component(type, worker, [idx, ind_index]):
                return

    def attempt_widget_placement(self, pair, idx):
        for worker in pair:
            if worker.widgets:
                worker.place_widget(worker.widgets, self.assembly_line)
                return

    def time_pass(self, randint):
        all_workers = [worker for pair in self.workers for worker in pair]
        for element in [self.assembly_line] + all_workers:
            element.time_pass(randint)

    def allocate_resources(self, randint=None):
        self.time_pass(randint)
        for idx, slot in enumerate(self.assembly_line.belt):
            if slot == 'A' or slot == 'B':
                self.attempt_component_allocation(slot, self.workers[idx], idx)
            if slot == None:
                self.attempt_widget_placement(self.workers[idx], idx)
