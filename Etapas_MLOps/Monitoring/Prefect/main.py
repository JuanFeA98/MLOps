from prefect import task, Flow

from src import preprocessing

# def main():

with Flow("dataengineer") as flow:
    data = preprocessing.load_data()

    features = preprocessing.get_features(data)
    target = preprocessing.get_target(data)

    X_train, X_test, y_train, y_test = preprocessing.split_date(features, target)
    print('Yey')

    flow.run()
