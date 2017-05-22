from pandas import DataFrame, Series
import pandas as pd
import json

path = '/Users/ckanumolu/Desktop/MachineLearning/DataForGitHub/usagov_bitly_data2013-05-17-1368832207'
records=[json.loads(line) for line in open(path)]
#print(records[0])


frame = DataFrame(records)
print(frame)

# https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#gs.fe4pDjc
