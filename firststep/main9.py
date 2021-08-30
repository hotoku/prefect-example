import pandas as pd
from prefect import task, Flow

"""
これはエラー。
x.f(1) で、TypeError: missing a required argument: 'val'
"""


class X:
    def __init__(self, n) -> None:
        self.n = n

    @task
    def f(self, val):
        return val + self.n


@task
def doit(n):
    print(n)


with Flow("my flos") as flow:
    x = X(10)
    ret = x.f(1)
    doit(ret)


flow.run()
