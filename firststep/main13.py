import pandas as pd
from prefect import task, Flow


@task
def doit(n):
    raise Exception("raise!")


with Flow("my flos") as flow:
    doit(1)

flow.run()
