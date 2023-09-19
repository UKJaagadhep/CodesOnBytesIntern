#Codes On Bytes
#Phase 1 projects
#Task 1:  Call this public Api and create a csv dataset using python and pandas
#https://data.binance.com/api/v3/ticker/24hr
import requests     #used to work with http and also api
import pandas as pd     #used to create and work with datasets in the form of dataframes
#assigning given api url to a variable
api='https://data.binance.com/api/v3/ticker/24hr'
get_api=requests.get(api)     #gets access to the url
data=get_api.json()     #converts it into json (like python dictionary) format
df=pd.DataFrame(data)     #creates a dataframe using the data 
df.to_csv('result.csv',index=False)     #save the dataframe to a csv file named 'result.csv' without the indices in the dataframe
print("CSV dataset saved to result.csv")
