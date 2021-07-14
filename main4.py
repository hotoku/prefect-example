from prefect import task, Flow, Parameter

@task
def say_hello(name):
    print(f"Hello {name}!")


with Flow("Say Hi!") as flow:
    name = Parameter("name")
    say_hello(name)


# state = flow.run(name="hoge")
flow.register(project_name="myproject")
