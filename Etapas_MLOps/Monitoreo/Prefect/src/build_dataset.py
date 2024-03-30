import pandas as pd

def run(features, target):

    df = pd.merge(
        features.reset_index(),
        target.reset_index(),
        how='left',
        left_on='index',
        right_on='index'
    )

    df.drop('index', axis=1, inplace=True)

    return df

if __name__ == '__main__':
    run()