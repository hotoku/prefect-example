import pandas as pd
from prefect import task, Flow

"""
エラー。
def f で、
TypeError: `fn` must be callable
"""


class X:
    def __init__(self, n):
        self.n = n

    @task
    @staticmethod
    def f(x, val):
        return x.n + val


@task
def doit(n):
    print(n)


with Flow("my flos") as flow:
    x = X(10)
    ret = X.f(x, 1)
    doit(ret)


flow.run()
