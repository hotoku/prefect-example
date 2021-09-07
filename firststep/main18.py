import time
from prefect import task, Flow
from prefect.executors.dask import LocalDaskExecutor


"""
LocalDaskExecutorで並列処理になる
worker数の指定方法が不明
"""


@task
def doit(n):
    time.sleep(1)
    return n + 1


@task
def myprint(k, v):
    time.sleep(1)
    print("{}, {}".format(k, v))


with Flow("my flow",
          executor=LocalDaskExecutor(n_workers=2)) as flow:
    dic = {
        i: doit(i) for i in range(100)
    }
    for k, v in dic.items():
        myprint(k, v)


ret = flow.run()
print(ret.__class__)
