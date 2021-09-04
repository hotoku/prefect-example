import pdb
import pandas as pd
from prefect import task, Flow


@task
def doit(n):
    return 1


with Flow("my flos") as flow:
    doit(1)

ret = flow.run()
print(ret.__class__)
