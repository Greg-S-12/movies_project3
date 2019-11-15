"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""
import statistics 
import pandas as pd
import numpy as np
from scipy import stats
import math

def get_sample_mean(sample):
    return sum(sample) / len(sample)

def get_sample(data, n):
    sample = []
    while len(sample) != n:
        x = np.random.choice(data)
        sample.append(x)
    return sample

def create_sample_distribution(data, dist_size=100, n=30):
    sample_dist = []
    while len(sample_dist) != dist_size:
        sample = get_sample(data, n)
        sample_mean = get_sample_mean(sample)
        sample_dist.append(sample_mean)
    return sample_dist 

def compare_pval_alpha(p_val, alpha):
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status

def significance(p_val, alpha):
    
    # Produces an explanation of whether the result is significant for a given alpha. If the number is larger thann 3dp then
    # it will round, otherwise will give full p-value.
    
    status = ''
    if p_val>0.001:
        if p_val > alpha:
            status = f"Fail to reject the null as our p-value ({round(p_val,3)}) is greater than our alpha ({alpha}) so the result is not signifcant."
        else:
            status = f'We reject the null as our p-value ({round(p_val,3)}) is less than our alpha ({alpha}) so we can say this result is signifcant.'
    else:
        if p_val > alpha:
            status = f"Fail to reject the null as our p-value ({p_val}) is greater than our alpha ({alpha}) so the result is not signifcant."
        else:
            status = f'We reject the null as our p-value ({p_val}) is less than our alpha ({alpha}) so we can say this result is signifcant.'
    return status


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


def cohens_d(sample1,sample2):
    
    stdv2 = statistics.pstdev(sample2)
    stdv1 = statistics.stdev(sample1)
    mu2   = statistics.mean(sample2)
    mu1   = statistics.mean(sample1)

    sigma_pooled = ((stdv1**2 + stdv2**2)/2)**0.5

    effect_size = (mu1-mu2)/(sigma_pooled)

    return effect_size

def z_test(sample1,sample2,alpha):
   
    # The calculation for the z score
    
    mu_1  = statistics.mean(sample1)            # Our sample mean
    mu_p = statistics.mean(sample2)             # The population mean (not including our sample)
    sigma = statistics.pstdev(sample2)          # The standard deviation of the population  
    n     = len(sample1)                        # The size of the sample, n being the number of items in the sample
   
    z = (mu_1-mu_p)/(sigma/(n**0.5))            # The size of the sample, n being the number of items in the sample
    z_p = (stats.norm.cdf(z))                   # This calculates the related z-probability    
    p = (1-z_p)
    
    d = cohens_d(sample1,sample2)
    
    status = compare_pval_alpha(p,alpha)
    
    return print(f"The z-statistic is {round(z,3)}, which corresponds to a p-value of {p}.\nThe effect size, cohen's d = {round(d,3)}.\nFrom this we {status} the null hypothesis")
