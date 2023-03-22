from prefect import task, flow
from prefect_dask import DaskTaskRunner


def fib(n: int) -> int:
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


@task
def task1(_: int) -> int:
    return fib(40)


@task
def task_sum(ls: list[int]) -> int:
    ret = 0
    for x in ls:
        ret += x
    return ret


@flow(task_runner=DaskTaskRunner())
def main():
    xs = []
    for i in range(3):
        xs.append(task1(i))
    print(task_sum(xs))


def run():
    fib(40)


if __name__ == "__main__":
    main()
