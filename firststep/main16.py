import pdb
import pandas as pd
from prefect import task, Flow


"""
ok
"""


@task
def doit(n):
    return n + 1


@task
def myprint(k, v):
    print("{}, {}".format(k, v))


with Flow("my flos") as flow:
    dic = {
        i: doit(i) for i in range(3)
    }
    for k, v in dic.items():
        myprint(k, v)


ret = flow.run()
print(ret.__class__)
