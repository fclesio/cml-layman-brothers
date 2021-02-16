#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys

sys.path.append("./")

from cml_layman_brothers.src.main.utils import logger

logger = logger.setup_custom_logger("root")

import matplotlib.pyplot as plt
import json
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix

dict_cml_objects_path = {
    "confusion_matrix": "cml_objects/confusion_matrix.png",
    "metrics": "cml_objects/metrics.txt",
}

dict_data_path = {
    "X_train": "cml_layman_brothers/data/train_features.csv",
    "X_test": "cml_layman_brothers/data/test_features.csv",
    "y_train": "cml_layman_brothers/data/train_labels.csv",
    "y_test": "cml_layman_brothers/data/test_labels.csv",
}

depth = 10
logger.info(f"[TRAINING] - Random Forest Trees Depth: {depth}")


def get_cml_objects_folder():
    if not os.path.isdir("cml_objects"):
        os.mkdir("cml_objects")


logger.info("[TRAINING] - Create CML folder")
get_cml_objects_folder()

logger.info("[TRAINING] - Load training and test data")
X_train = np.genfromtxt(dict_data_path["X_train"])
y_train = np.genfromtxt(dict_data_path["y_train"])
X_test = np.genfromtxt(dict_data_path["X_test"])
y_test = np.genfromtxt(dict_data_path["y_test"])

logger.info("[TRAINING] - Algo training")
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test)
acc = (round(acc, 2)) * 100
logger.info(f"[TRAINING] - Model accuracy: {acc}")

with open(dict_cml_objects_path["metrics"], "w") as outfile:
    outfile.write("Accuracy: " + str(acc) + "\n")

disp = plot_confusion_matrix(clf, X_test, y_test, normalize="true", cmap=plt.cm.Blues)
plt.savefig(dict_cml_objects_path["confusion_matrix"])

logger.info("[TRAINING]- Training finished")
