#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

url = \
    "https://raw.githubusercontent.com/fclesio/learning-space/master/Datasets/02%20-%20Classification/default_credit_card.csv"

seed = 42

dict_data_path = {
    "X_train": "data/train_features.csv",
    "X_test": "data/test_features.csv",
    "y_train": "data/train_labels.csv",
    "y_test": "data/test_labels.csv",
}


def get_raw_from_github(url):
    df = pd.read_csv(url)
    return df


def get_y(df):
    y = df.iloc[:, -1:]
    return y


def get_X(df):
    del df["DEFAULT"]
    del df["ID"]
    X = df
    return X


def delete_files(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


if __name__ == "__main__":
    df = get_raw_from_github(url=url)
    y = get_y(df)
    X = get_X(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=seed)

    if not os.path.isdir("data"):
        os.mkdir("data")

    for key, value in dict_data_path.items():
        delete_files(filepath=value)

    np.savetxt(dict_data_path["X_train"], X_train)
    np.savetxt(dict_data_path["X_test"], X_test)
    np.savetxt(dict_data_path["y_train"], y_train)
    np.savetxt(dict_data_path["y_test"], y_test)
