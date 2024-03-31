import pandas as pd

from prefect import task

@task(name='create_df')
def run(hora):
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [1, 2, 3],
        'C': [1, 2, 3]
    })

    # df.to_csv(f'./Etapas_MLOps/Data/df_{hora}.csv', index=False)
    return df

if __name__ == '__main__':
    run()