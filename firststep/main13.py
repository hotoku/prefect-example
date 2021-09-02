import pdb
import pandas as pd
from prefect import task, Flow


@task
def doit(n):
    raise Exception("raise!")


with Flow("my flos") as flow:
    doit(1)

ret = flow.run()
pdb.set_trace()
