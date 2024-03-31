import pandas as pd

from prefect import task

@task(name='transform_data')
def run(df):

    df['New_column'] = 'Hello prefect!'

    return df

if __name__ == '__main__':
    run()