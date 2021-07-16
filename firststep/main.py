from prefect import task, Flow


@task
def add(x, y=1):
    return x + y

with Flow("My First Flow") as flow:
    ret1 = add(1, 2)
    ret2 = add(ret1, 100)


state = flow.run()

assert state.is_successful()

first_task_state = state.result[ret1]
assert first_task_state.is_successful()
assert first_task_state.result == 3

second_task_state = state.result[ret2]
assert second_task_state.is_successful()
assert second_task_state.result == 103
