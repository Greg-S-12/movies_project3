"""
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd




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
    
# def drop_nulls(dataframe,column_to_search):
#     # The null values in our dataframe are listed as "\N"
#     df=dataframe
#     df.loc[df[column_to_search]==r"\N"]
    
    
# def search(dataframe, column_to_search, condition, columns):
    
#     dataframe=df
    
#     new_df=df.loc[df[columns_to_search]condition,columns]
    
#     return new_df