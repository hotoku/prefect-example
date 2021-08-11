import pdb
from prefect import Task, Flow


class AddTask(Task):
    def run(self, x, y):
        import pdb
        pdb.set_trace()
        return x + y


a = AddTask()

with Flow("My Flow") as f:
    t1 = a(1, 2)  # t1 != a
    t2 = a(5, t1)  # t2 != a


f.run()

pdb.set_trace()
