import pdb
from prefect import task, Flow


@task
def f(x, y):
    return x + y


with Flow("my flos") as flow:
    z = f(1, 2)


flow.run()
