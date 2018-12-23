'''
    MAIS 202 coding challenge.
'''
import pandas as pd

# import csv file as a dataframe
df_original = pd.read_csv('data.csv', index_col=0)

# keep only the relevant columns from the original dataframe
df = df_original[['int_rate', 'purpose']]

# group data by purpose and calculate mean interest rate for each loan purpose
df = df.groupby(['purpose']).mean()
df = df.rename(columns={'int_rate':'mean(int_rate)'})

# plot graph
ax = df.plot(y='mean(int_rate)', kind='bar', legend=False)
ax.set_xlabel('')
ax.set_ylabel('Average interest rate (%)')
ax.set_title('Average interest rate per loan')