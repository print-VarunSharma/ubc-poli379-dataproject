import pandas as pd
''' 
Author Varun D. Sharma
Main code for poli data science project working with Chinese trade data.

Follow documentation as follows: 

Insert copied CSV file path in pd.read 
'''
# df = pd.read_csv (r'Path where the CSV file is stored\File name.csv')
df = pd.read_csv(r'C:\Users\Varun\Documents\ubc-poli379-dataproject\China_aggregate_provincial_trade_data\China_Exports_by_Provinces_Oct_2020.csv') 
print(df)

'''
Use Pandas to Calculate Stats from an Imported CSV File
Using the pandas package, we can calculate the following statistics:

Mean Trade Value
Total sum of Trade Values
Maximum Trade Value
Minimum Trade Value
Count of Trade Values
Median Trade Value
Standard deviation of Trade Values
Variance of of Trade Values
'''


# block 1 - simple stats

mean1 = df['Trade Value'].mean()
sum1 = df['Trade Value'].sum()
max1 = df['Trade Value'].max()
min1 = df['Trade Value'].min()
count1 = df['Trade Value'].count()
median1 = df['Trade Value'].median() 
std1 = df['Trade Value'].std() 
var1 = df['Trade Value'].var() 

def main_statistics(): 
    mean1
    sum1
    max1
    min1
    count1
    median1
    std1
    var1
    return main_statistics()
# block 2 - group by

''' replace Country with Subnat Geography if working with the aggregated data sets '''
groupby_sum1 = df.groupby(['Subnat Geography']).sum()
groupby_count1 = df.groupby(['Subnat Geography']).count()


# print block 1
print ('Mean Trade Value: ' + str(mean1))
print ('Sum of Trade Values: ' + str(sum1))
print ('Max Trade Value: ' + str(max1))
print ('Min Trade Value: ' + str(min1))
print ('Count of Trade Values: ' + str(count1))
print ('Median Trade Value: ' + str(median1))
print ('Std of Trade Values: ' + str(std1))
print ('Var of Trade Values: ' + str(var1))

# print block 2
print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
print ('Count of values, grouped by the Country: ' + str(groupby_count1))

def data_stats_output():
    print ('Mean Trade Value: ' + str(mean1))
    print ('Sum of Trade Values: ' + str(sum1))
    print ('Max Trade Value: ' + str(max1))
    print ('Min Trade Value: ' + str(min1))
    print ('Count of Trade Values: ' + str(count1))
    print ('Median Trade Value: ' + str(median1))
    print ('Std of Trade Values: ' + str(std1))
    print ('Var of Trade Values: ' + str(var1))

    # print block 2
    print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
    print ('Count of values, grouped by the Country: ' + str(groupby_count1))
    return data_stats_output()