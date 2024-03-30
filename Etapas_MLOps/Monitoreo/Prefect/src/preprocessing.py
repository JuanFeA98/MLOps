import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from prefect import task

# @task
def load_data():
    iris_data = load_iris()
    
    return iris_data

@task
def get_features(data):
    features = pd.DataFrame(
            data['data'], 
            columns=data['feature_names']
        )

    return features

@task
def get_target(data):
    target = pd.DataFrame(
            data['target'] 
        )

    target.columns = ['Target']

    return target

@task
def split_date(features, target):
    X_train, X_test, y_train, y_test = train_test_split(
                                            features,
                                            target, 
                                            random_state=13, 
                                            train_size=0.7
                                        )

    return X_train, X_test, y_train, y_test