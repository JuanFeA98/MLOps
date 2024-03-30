import pandas as pd

from sklearn.datasets import load_iris

def run():

    iris_data = load_iris()

    target = pd.DataFrame(
            iris_data['target'] 
        )

    target.columns = ['Target']

    return target

if __name__ == '__main__':
    run()