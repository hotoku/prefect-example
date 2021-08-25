from prefect import task, Flow


@task
def f(x, y):
    return x + y


def g(x, y):
    return x + y


@task
def h(x):
    print(x)


with Flow("my flos") as flow:
    z = f(1, 2)
    w = g(z, 1)
    h(w)

flow.run()
