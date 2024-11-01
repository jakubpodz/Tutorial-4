"""These questions use data from the Fama and French data library on stock market returns:
 http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/index.html
 Note that these questions are designed to test your understanding of the material covered on the course to date.
 We will learn faster and more efficient ways of doing some of these tasks in future lectures.

a.	Load the data from the ‘ff_monthly.csv’ file into a variable 'monthly_returns',
    use the first column as an index (this contains the year and month of the data as a string)
b.	Create a new column ‘Mkt’ as ‘Mkt-RF’ + ‘RF’
c.	Create two new columns in the loaded DataFrame, ‘Month’ and ‘Year’ to contain the year and month
    of the dataset extracted from the index column.
d.	Create a new DataFrame 'summary_stats' with columns ‘Mean’ and ‘Standard Deviation’ and the full set of years from (b) above as an index.
e.	Write a function which accepts (r_m,s_m) the monthy mean and standard deviation of a return series and
    returns a tuple (r_a,s_a), the annualised mean and standard deviation.
    Use the formulae: r_a = (1+r_m)**12 -1, and s_a = s_m * 12**0.5.
f.	Loop through each year in the data, and calculate the annualised mean and standard deviation of the new ‘Mkt’ column,
    storing each in the newly created DataFrame.
    Note that the values in the input file are % returns, and need to be divided by 100 to return decimals
    (i.e the value for August 2022 represents a return of -3.78%).
g.	Print the DataFrame and output it to a csv file 'summary_stats.csv'.

    Harder...

h.	The ‘Great Moderation’ (GM) period is often defined as the period between the January 2004 and June 2007 (inclusive).
    Using a list comprehensions, build a dictionary with keys (‘GM’,’PreGM’,’PostGM’) and set each value set to be a list
    of months in the index which are counted in each period (for the list use the syntax [i for i in collection if condition])
i.	Construct a series 'GMS' containing the (monthly) standard deviation of returns in each period.
    Print the series, and output the series to ‘Moderation.csv’.

j.	Was monthly US stock market volatility lower in the GM period than before / after?
"""

import pandas as pd

monthly_returns = pd.read_csv('ff_monthly.csv')

monthly_returns['Mkt'] = monthly_returns['Mkt-RF'] + monthly_returns['RF']

monthly_returns['Unnamed: 0'] = monthly_returns['Unnamed: 0'].astype(str)
monthly_returns['Year'] = monthly_returns['Unnamed: 0'].str[:4]
monthly_returns['Month'] = monthly_returns['Unnamed: 0'].str[-2:]

monthly_returns.drop(columns=['Unnamed: 0'], inplace=True)


def summary(r_m,s_m):
    """
    This function accepts the monthly mean and standard deviation of a return series 
    and returns the annualised mean and standard deviation.
    """
    r_a = (1+r_m)**12 -1
    s_a = s_m * 12**0.5

    return r_a,s_a

grouped_by_year = monthly_returns.groupby('Year')




annual_means = []
annual_stds = []


for year, group in grouped_by_year:
    
    mean = group['Mkt'].mean() / 100  
    std = group['Mkt'].std() / 100    
    
    
    annual_mean, annual_std = summary(mean, std)
    
    
    annual_means.append(annual_mean)
    annual_stds.append(annual_std)


summary_stats = pd.DataFrame({
    'Year': grouped_by_year.groups.keys(),   
    'Annualized Mean': annual_means,         
    'Annualized Standard Deviation': annual_stds  
})

summary_stats.to_csv('summary_stats.csv')

#GM = "2001-01: 2007-06"
#PreGM period: Any date before January 2004.
#PostGM period: Any date after June 2007

GM_periods = {'PreGM': [i for i in monthly_returns.index if int(monthly_returns.loc[i, 'Year']) < 2004 ],
              'GM': [i for i in monthly_returns.index if (
                  (int(monthly_returns.loc[i, 'Year']) == 2004 and int(monthly_returns.loc[i, 'Month']) >= 1) or
                  (int(monthly_returns.loc[i, 'Year']) > 2004 and int(monthly_returns.loc[i, 'Year']) < 2007) or
                  (int(monthly_returns.loc[i, 'Year']) == 2007 and int(monthly_returns.loc[i, 'Month']) <= 6)
                )],
              'PostGM': [i for i in monthly_returns.index if (
                (int(monthly_returns.loc[i, 'Year']) == 2007 and int(monthly_returns.loc[i, 'Month']) > 6) or 
                int(monthly_returns.loc[i, 'Year']) > 2007)]
            }

print("Number of PreGM months:", len(GM_periods['PreGM']))
print("Number of GM months:", len(GM_periods['GM']))
print("Number of PostGM months:", len(GM_periods['PostGM']))

std_dev = {}

for period, indecies in GM_periods.items():
    period_data = monthly_returns.loc[indecies,'Mkt']/100
    std_dev[period] = period_data.std()

GMS = pd.Series(std_dev)

print(GMS)

#Market volatility was lowest during the GM period compared to other periods with a standard deviation of 0.0.022226, while the Pre-GM period had the highest volaitlity of 0.055433.