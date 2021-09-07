import pdb
import pandas as pd
from prefect import task, Flow


"""
動作はするが、意図とは違う。
まず、
{0: <Task: doit>, 1: <Task: doit>, 2: <Task: doit>}
が表示され、そのあとに、doitが3つ走る
"""


@task
def doit(n):
    return n + 1


@task
def myprint(d):
    for k, v in d.items():
        print("{}, {}".format(k, v))


with Flow("my flos") as flow:
    dic = {
        i: doit(i) for i in range(3)
    }
    print(dic)

ret = flow.run()
print(ret.__class__)
