import csv
import pandas as pd
import itertools

with open('C:/Users/cvikas10/Desktop/sampleData.txt','r') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    csvData = [row for row in csvReader]
    
csvData_df = pd.DataFrame(csvData[1:],columns = csvData[0])
new = csvData_df['month_year'].str.split('_',n = 1,expand=True)
csvData_df['month'] = new[0]
csvData_df['year'] = new[1]
csvData_df.drop('month_year',axis=1,inplace=True)

csvData_df['salary'] = csvData_df['salary'].astype(int)
csvData_df['year'] = csvData_df['year'].astype(int)

#csvData_df.assign(rn=csvData_df.sort_values(['salary'], ascending=False).groupby(['city','employee']).cumcount() + 1).query('rn <= 5').sort_values(['city','employee','rn'])

cities = list(set(csvData_df['city']))
years = list(set(csvData_df['year']))
for p,q in list(itertools.product(cities,years)):
    sub_df = csvData_df[(csvData_df['city'] == p) & (csvData_df['year'] == q)]
    X = sorted(sub_df['salary'],reverse=True)
    if len(X) >= 5:
        print (p,q,X[4])
    elif len(X) < 5 and len(X) > 0:
        print (p,q,X[len(X)-1])
    elif len(X) == 0:
        print (p,q,None)