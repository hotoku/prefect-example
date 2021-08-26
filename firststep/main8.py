import pandas as pd
from prefect import task, Flow

"""
こっちはエラー。
TypeError: object of type 'FunctionTask' has no len()
が出る。

やはり、基本的に、一度Taskの中に入ったら、ずっとTaskの殻はまとったまま生きないとダメ。
"""


@task
def f(n):
    return pd.DataFrame(dict(x=range(n)))


def g(df):
    print(len(df))


with Flow("my flos") as flow:
    df = f(10)
    g(df)

flow.run()
