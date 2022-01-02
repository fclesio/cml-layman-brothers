#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

sys.path.append("./")

import os
from cml_layman_brothers.src.main.utils import logger

logger = logger.setup_custom_logger("root")

logger.info("[DATA-EXTRACTION]- Start data extraction")
url = "https://raw.githubusercontent.com/fclesio/learning-space/master/Datasets/02%20-%20Classification/default_credit_card.csv"

logger.info(f"[DATA-EXTRACTION]- Data URL: {url}")

seed = 42
logger.info(f"[DATA-EXTRACTION]- Random seed for data split: {seed}")

dict_data_path = {
    "X_train": "cml_layman_brothers/data/train_features.csv",
    "X_test": "cml_layman_brothers/data/test_features.csv",
    "y_train": "cml_layman_brothers/data/train_labels.csv",
    "y_test": "cml_layman_brothers/data/test_labels.csv",
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

    logger.info(f"[DATA-EXTRACTION]- Get data from Github")
    df = get_raw_from_github(url=url)
    logger.info(
        f"[DATA-EXTRACTION]- Dataframe with {df.shape[0]} rows and {df.shape[1]} columns"
    )

    y = get_y(df)
    X = get_X(df)

    test_size = 0.10
    logger.info(
        f"[DATA-EXTRACTION]- Split train and test sets. Test size with {test_size}%"
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=seed, test_size=test_size
    )

    logger.info(
        f"[DATA-EXTRACTION]- Training set with {X_train.shape[0]} samples - Test set with {X_test.shape[0]} samples"
    )

    logger.info("[DATA-EXTRACTION]- Create folder")
    if not os.path.isdir("cml_layman_brothers/data"):
        os.mkdir("cml_layman_brothers/data")

    for key, value in dict_data_path.items():
        delete_files(filepath=value)

    logger.info("[DATA-EXTRACTION]- Saving files in folder")
    np.savetxt(dict_data_path["X_train"], X_train)
    np.savetxt(dict_data_path["X_test"], X_test)
    np.savetxt(dict_data_path["y_train"], y_train)
    np.savetxt(dict_data_path["y_test"], y_test)

    logger.info("[DATA-EXTRACTION]- Data extraction finished")
