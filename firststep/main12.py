import pandas as pd
from prefect import task, Flow

"""
エラーにはならないけど、何も表示されない
"""


@task
def g(df):
    print(len(df))


with Flow("main12") as flow:
    df = pd.DataFrame(dict(x=range(10)))
    g(df)
