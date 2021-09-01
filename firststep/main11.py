import pandas as pd
from prefect import task


@task
def g(df):
    print(len(df))


df = pd.DataFrame(dict(x=range(10)))
g(df)
