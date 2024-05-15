import pytest

# TODO: add necessary import
import pandas as pd
import numpy as np





data = pd.read_csv("data/census.csv")

# TODO: implement the first test. Change the function name and input as needed
def test_row_count():
    """
    # test row count
    """
    # Your code here
    data = pd.read_csv("data/census.csv")
    assert 32000 < data.shape[0] < 32600
    #pass


# TODO: implement the second test. Change the function name and input as needed
def test_data_columns():
    """
    # Test the column names are correct
    """
    # Your code here
    data = pd.read_csv("data/census.csv")
    correct_columns = ["age", "workclass", "fnlgt","education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"]
     
    columns=data.columns.values

    assert list(correct_columns) ==list(columns)
    #pass


# TODO: implement the third test. Change the function name and input as needed
def test_salary():
    """
    # testing the salary options
    """
    # Your code here
    data = pd.read_csv("data/census.csv")
    known_salary = ["<=50K", ">50K"]


    assert set(known_salary) == set(data['salary'].unique())
    #pass
