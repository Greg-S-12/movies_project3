"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
from scipy import stats
import math



def welch_t(a, b):
    
    # Calculate Welch's t-statistic

    numerator = a.mean() - b.mean()
    
    # “ddof = Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof, 
    #  where N represents the number of elements. By default ddof is zero.
    
    denominator = np.sqrt(a.var(ddof=1)/a.size + b.var(ddof=1)/b.size)
    
    return np.abs(numerator/denominator)

def welch_df(a, b):
    
    # Calculate the effective degrees of freedom
    
    s1 = a.var(ddof=1) 
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size
    
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)
    
    return numerator/denominator




def create_sample_dists(cleaned_data, y_var=None, categories=[]):
    """
    Each hypothesis test will require you to create a sample distribution from your data
    Best make a repeatable function

    :param cleaned_data:
    :param y_var: The numeric variable you are comparing
    :param categories: the categories whose means you are comparing
    :return: a list of sample distributions to be used in subsequent t-tests

    """
    htest_dfs = []

    # Main chunk of code using t-tests or z-tests
    return htest_dfs

def compare_pval_alpha(p_val, alpha):
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status


def hypothesis_test_one(alpha = None, cleaned_data):
    """
    Describe the purpose of your hypothesis test in the docstring
    These functions should be able to test different levels of alpha for the hypothesis test.
    If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

    :param alpha: the critical value of choice
    :param cleaned_data:
    :return:
    """
    # Get data for tests
    comparison_groups = create_sample_dists(cleaned_data=None, y_var=None, categories=[])

    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    ###

    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference between NONE')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status

def hypothesis_test_two():
    pass

def hypothesis_test_three():
    pass

def hypothesis_test_four():
    pass
