#Imports
import pandas as pd

#Files to read in
def acquire_irs():
    """
    This function reads in the IRS 2017 data
    """
    irs = pd.read_csv("./Data/17zpallagi.csv")
    return irs