import pandas as pd

from prefect import task

@task(name='merge_df')
def run(df_1, df_2):

    new_df = pd.merge(
        df_1.reset_index(),
        df_2.reset_index(),
        how='left',
        left_on='index',
        right_on='index'
    )

    return new_df

if __name__ == '__main__':
    run()