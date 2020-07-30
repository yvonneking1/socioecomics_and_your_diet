#Imports
import pandas as pd
import acquire



# Helper functions

def add_leading_zero_to_zipcodes(x):
    """
    Takes in a number and pads it with 0 up to 5 digits
    """
    return str(x).zfill(5)



# Prep functions
def prep_irs_data():
    """
    This function uses the acquire_irs function and prepares the dataframe by:
    removing unnecessary columns
    updating datatypes
    grouping and aggregationg by zipcode
    creating calulated fields for avg total income and avg gross income per zipcode
    """
    #bring in the data
    irs = acquire.acquire_irs()
    
    #get rid of unneeded columns
    columns_to_keep = ["STATEFIPS", "STATE", "zipcode", "N1", "A00100", "A02650", "N02650"]
    irs_df = irs[columns_to_keep]
    
    #drop the invalid zipcodes 0 and 99999
    not_zip_0_mask = irs_df.zipcode != 0
    not_zip_99999_mask = irs_df.zipcode != 99999

    irs_df = irs_df[not_zip_0_mask]
    irs_df = irs_df[not_zip_99999_mask]
    
    #create aggregated groupby dataframes
    grouped_N1_zip = irs_df.groupby(irs_df.zipcode).N1.sum().reset_index()
    grouped_A00100_zip = irs_df.groupby(irs_df.zipcode).A00100.sum().reset_index()
    grouped_A02650_zip = irs_df.groupby(irs_df.zipcode).A02650.sum().reset_index()
    grouped_N02650_zip = irs_df.groupby(irs_df.zipcode).N02650.sum().reset_index()
    
    #merge dataframes into one
    df1 = grouped_N1_zip.join(grouped_A00100_zip.set_index("zipcode"), on="zipcode")
    df2 = df1.join(grouped_A02650_zip.set_index("zipcode"), on="zipcode")
    df3 = df2.join(grouped_N02650_zip.set_index("zipcode"), on="zipcode")
    
    #create list of zipcodes, state, and FIPS
    cols_to_keep = ["STATEFIPS", "STATE", "zipcode"]
    state_zips = irs_df[cols_to_keep]
    state_zips = state_zips.drop_duplicates(subset="zipcode")
    
    #merge zip, state, fips onto df and organize order of col
    df4 = df3.join(state_zips.set_index("zipcode"), on="zipcode")
    col_order = ["zipcode", "STATE", "STATEFIPS", "N1", "A00100", "A02650", "N02650"]
    irs_df = df4[col_order]
    
    #create calculated field for avg per person
    #gross income
    irs_df["avg_gross_income"] = (irs_df.A00100 / irs_df.N1) * 1000
    #total income
    irs_df["avg_total_income"] = (irs_df.A02650 / irs_df.N1) * 1000
    
    #update data types
    irs_df.zipcode = irs_df.zipcode.astype("str")
    irs_df.STATEFIPS = irs_df.STATEFIPS.astype("str")
    irs_df.N1 = irs_df.N1.astype("int")
    irs_df.N02650 = irs_df.N02650.astype("int")
    
    #Update zipcodes to ensure all are 5 disgits
    irs_df.zipcode = irs_df.zipcode.apply(add_leading_zero_to_zipcodes)
    
    return irs_df