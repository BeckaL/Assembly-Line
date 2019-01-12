from task_manager import Task_Manager
from doubles import ObjectDouble, allow
from assembly_line import Assembly_Line
from worker import Worker

al = ObjectDouble(Assembly_Line)
workers = [ ObjectDouble(Worker) for i in range(6)]


def test_task_manager_initializes_with_assembly_line_and_workers():
    tm = Task_Manager(al, workers)
    pass
