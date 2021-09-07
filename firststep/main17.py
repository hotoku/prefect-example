import time
from prefect import task, Flow


"""
デフォルトのままでは並列処理はしない
"""


@task
def doit(n):
    time.sleep(1)
    return n + 1


@task
def myprint(k, v):
    time.sleep(1)
    print("{}, {}".format(k, v))


with Flow("my flos") as flow:
    dic = {
        i: doit(i) for i in range(3)
    }
    for k, v in dic.items():
        myprint(k, v)


ret = flow.run()
print(ret.__class__)
