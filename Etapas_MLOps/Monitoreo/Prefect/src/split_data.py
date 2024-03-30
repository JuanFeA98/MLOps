import pandas as pd

from sklearn.model_selection import train_test_split

def run(features, target):

    X_train, X_test, y_train, y_test = train_test_split(
                                            features,
                                            target, 
                                            random_state=13, 
                                            train_size=0.7
                                        )

    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    run()