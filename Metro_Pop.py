# US Metro Population Data

import pandas as pd 

Metro_Pop2020_df = pd.read_csv('Project_2_Data/US_Pop_2020_CSV.csv', usecols= ['CBSA', 'NAME', 'LSAD', 'DATE', 'POPESTIMATE', 'POPEST_MALE', 'POPEST_FEMALE', 'MEDIAN_AGE_TOTAL', 'MEDIAN_AGE_MALE', 'MEDIAN_AGE_FEMALE'])   

Metro_Pop2020_df.rename(columns={'NAME': 'City/Metro', 'POPESTIMATE': 'Estimated_Population', 'POPESTIMATE': 'Population', 'DATE': 'Date', 'POPEST_MALE': 'Male_Population', 'POPEST_FEMALE': 'Female_Population', 'MEDIAN_AGE_TOTAL': 'Median_Age_Total', 'MEDIAN_AGE_MALE': 'Median_Age_Male', 'MEDIAN_AGE_FEMALE': 'Median_Age_Female'}, inplace= True) 


Cinci_Metro = Metro_Pop2020_df.loc[Metro_Pop2020_df['City/Metro']== 'Cincinnati, OH-KY-IN'] 

