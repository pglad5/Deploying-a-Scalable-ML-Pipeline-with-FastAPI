#  import pytest

#  TODO: add necessary import
import pandas as pd
import numpy as np


data = pd.read_csv("data/census.csv")

# TODO: implement the first test. Change the function name and input as needed


def test_row_count():
    """
    test the row count
    """
    # Your code here
    data = pd.read_csv("data/census.csv")
    assert 32000 < data.shape[0] < 32600
    #pass


#  TODO: implement the second test. Change the function name and input as needed
#  def test_data_columns():
#    """
#    # Test the column names are correct
#   """
#    # Your code here
#    data = pd.read_csv("data/census.csv")
#  correct_columns = ["age", "workclass", 
#  "fnlgt","education", "education-num", "marital-status", "occupation",
#  "relationship", "race", "sex", "capital-gain", "capital-loss",
#  "hours-per-week", "native-country", "salary"]

#  assert list(correct_columns) ==list(data.columns.values)
#  pass


# TODO: implement the third test. Change the function name and input as needed
def test_age_range():
    """
    # testing the all of age range is between 0 and 100
    """
    # Your code here
    ages = pd.read_csv("data/census.csv")['age'].between(0, 100)
    assert np.sum(ages) == 32561

#  pass


def test_salaries():
    """" #test that there are two salary ranges in dataset"""

    salaries = list(pd.read_csv("data/census.csv")['salary'].unique())
    salary = np.count_nonzero(salaries)

    assert salary == 2
