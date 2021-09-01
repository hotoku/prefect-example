import pandas as pd
from prefect import task


"""
g(df)の呼び出しでエラー。
ValueError: Could not infer an active Flow context while creating edge to <Task: g>. This often means you called a task outside a `with Flow(...)` block. If you're trying to run this task outside of a Flow context, you need to call `g.run(...)`
"""


@task
def g(df):
    print(len(df))


df = pd.DataFrame(dict(x=range(10)))
g(df)
