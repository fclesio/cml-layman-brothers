#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import pandas as pd
from pandas.testing import assert_frame_equal

import sys
sys.path.append('./')

from cml_layman_brothers.src.main.processing.data_extraction import get_raw_from_github
from cml_layman_brothers.src.main.processing.data_extraction import get_y
from cml_layman_brothers.src.main.processing.data_extraction import get_X

# PyTest was failing for logging in all scripts due to out of context calls.
# To solve this in a quick and dirty manner I pass directly the full path in the
# imports and this problem is eliminated. Thanks SO [1].
# [1] - How to import a module given the full path? - https://stackoverflow.com/a/58974141/7024760


url = "https://raw.githubusercontent.com/fclesio/learning-space/master/Datasets/02%20-%20Classification/default_credit_card.csv"


def generate_raw_df_test(url=url):
    raw_df_test = pd.read_csv(url)
    return raw_df_test


def test_check_if_dataset_in_github_remote_is_working():
    import urllib.request

    code = urllib.request.urlopen(url).getcode()
    assert code == 200


def test_get_raw_from_github_if_is_a_dataframe():
    df = get_raw_from_github(url=url)
    assert isinstance(df, pd.DataFrame) == True


def test_get_raw_from_github():
    df = get_raw_from_github(url=url)
    expected_df = generate_raw_df_test()
    assert_frame_equal(df, expected_df)


def test_get_y_check_default_column():
    df = get_raw_from_github(url=url)
    y = get_y(df)
    assert y.columns[0] == "DEFAULT"


def test_get_y_check_default_column_is_dataframe():
    df = get_raw_from_github(url=url)
    y = get_y(df)
    assert isinstance(y, pd.DataFrame) == True


def test_get_X_check_is_dataframe():
    df = get_raw_from_github(url=url)
    X = get_X(df)
    assert isinstance(X, pd.DataFrame) == True


def test_get_X_qty_columns():
    df = get_raw_from_github(url=url)
    X = get_X(df)
    expected_columns = 23
    assert len(X.columns) == expected_columns


def test_get_X_columns_deletion():
    df = get_raw_from_github(url=url)
    X = get_X(df)
    expected_df = generate_raw_df_test()
    del expected_df["DEFAULT"]
    del expected_df["ID"]
    assert_frame_equal(X, expected_df)
