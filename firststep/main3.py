from prefect import Flow, task, Parameter


@task
def add(x, y):
    return x + y

@task
def say_hello(name):
    print(f"Hello {name}!")

flow = Flow("My imperative flow!")

name = Parameter("name")
second_add = add.copy()

flow.add_task(add)
flow.add_task(second_add)
flow.add_task(say_hello)

say_hello.set_upstream(second_add, flow=flow)

add.bind(x=1, y=2, flow=flow)
second_add.bind(x=add, y=100, flow=flow)
say_hello.bind(name=name, flow=flow)

flow.run(name="Hoge")
