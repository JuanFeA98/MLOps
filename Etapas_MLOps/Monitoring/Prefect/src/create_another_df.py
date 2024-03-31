import pandas as pd

from prefect import task

@task(name='create_another_df')
def run():
    df = pd.DataFrame({
        'D': [4, 5],
        'E': [4, 5],
    })

    return df

if __name__ == '__main__':
    run()