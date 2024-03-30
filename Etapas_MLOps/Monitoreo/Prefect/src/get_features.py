import pandas as pd

from sklearn.datasets import load_iris

def run():

    iris_data = load_iris()

    features = pd.DataFrame(
            iris_data['data'], 
            columns=iris_data['feature_names']
        )

    return features

if __name__ == '__main__':
    run()