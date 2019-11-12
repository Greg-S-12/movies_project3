"""
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""
import pandas as pd


def search(dataframe, column_to_search, condition, columns):
    
    dataframe=df
    
    new_df=df.loc[df[columns_to_search]condition,columns]
    
    return new_df

def drop_null_rows(dataframe,columns,condition):
    
def drop_nulls(dataframe,column_to_search):
    # The null values in our dataframe are listed as "\N"
    df=dataframe
    df.loc[df[column_to_search]==r"\N"]
    
    
