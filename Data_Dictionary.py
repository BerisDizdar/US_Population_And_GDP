# Featue 4: Data Dictionary

import pandas as pd 

Data_Dictionary = {'ID':['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17'],
                   'Variable':['Metro_Pop_2020_DF1', 'CBSA', 'City_Metro', 'LSAD', 'Date', 'Population', 'Metro_Pop_2000_DF2', 'Population_2000',
                               'Population_2010', 'GDP_Metro_DF3', 'Description', 'LineCode', 'Merged_Data', 'PopulationDiff', 'DF1_MetPop2020', 'DF2_Metro_Pop2000', 'DF3_Metro_GDP'],
                   'Data_Type':['DataFrame', 'int64', 'object', 'object', 'int64', 'int64', 'DataFrame', 'int64', 'int64', 'DataFrame', 'object', 'int64',
                                'DataFrame', 'int64', 'DataFrame', 'DataFrame', 'DataFrame'],
                   'Description':['DataFrame of 2020 population data', 'Unique metro area code', 'Name of metro area', 'Metro area', 'Date',
                                  'Population of metro area for year 2020', 'DataFrame of 2000 and 2010 population data', 'Population of metro area for year 2000',
                                  'Population of metro area for year 2010', 'DataFrame of 2021 GDP data', 'Current dollar GDP', 'Number from dataset',
                                  'New DataFrame created by merging two others', 'New column created by using two others', 'Subset of Metro_Pop_2020_DF1 DataFrame',
                                  'Subset of Metro_Pop_2000_DF2 DataFrame', 'Subset of GDP_Metro_DF3 DataFrame']} 

Data = pd.DataFrame(Data_Dictionary) 

print(Data) 