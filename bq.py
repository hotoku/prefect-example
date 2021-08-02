from prefect import task, Flow
from prefect.tasks.gcp.bigquery import BigQueryTask

sql1 = """
create or replace table `dor-ds-sandbox.paralelo_test.sample1` as select 1 as x
"""

task1 = BigQueryTask(
    sql1,
    location="asia-northeast1"
)

flow = Flow("bq flow")
flow.add_task(task1)

flow.run()
