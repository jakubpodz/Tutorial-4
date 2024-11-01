
"""The dataset contains data for 344 penguins. 
There are 3 different species of penguins in this dataset, collected from 3 islands in the Palmer Archipelago, Antarctica.

Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER,
a member of the Long Term Ecological Research Network. 
(Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer Archipelago (Antarctica) penguin data. 
R package version 0.1.0. https://allisonhorst.github.io/palmerpenguins/.doi:10.5281/zenodo.3960218.) 
Accessed via the Seaborn datasets package. 

1.	Create a Python script to do the following:
a.	Load the Penguins data set from ‘penguins.csv’ file in to a dataframe 'penguins'.
b.	Split the data by ‘species’ and ‘island’ (The syntax for combining criteria with a logical ‘and’ in pandas is:
     “my_df[(my_df[my_col]==y)&( penguins[my_2nd_col]==x)]” 
    where my_df is a DataFrame, my_col and my_2nd_col are valid columns names in my_df, and x and y are variables).
c.	Write each subset of data to a .csv file named 'species_island.csv' where species and island 
    denote the appropriate split of the data
d.	Display a summary of each subset of the data using .describe().
e.	Create a DataFrame 'body_mass', with index equal to the species, and columns equal to the isalnd and populate with
    the mean body mass (in grams) for each subset of penguins
f.	The command ‘df.max()’ gives the maximum value in a DataFrame. 
    Assign a tuple 'heaviest' equal to the (species, island) where the penguins are on average heaviest.
g. Output a sentence to indicate which subset of penguins are on average the heaviest.
"""

import pandas as pd

#1
#a.
file_path = '/mnt/data/Penguins.csv'
penguins = pd.read_csv(file_path)

# Step b: Split the data by 'species' and 'island'
species_island_groups = penguins.groupby(['species', 'island'])

# Step c: Write each subset of data to a .csv file named 'species_island.csv'
for (species, island), group in species_island_groups:
    file_name = f'{species}_{island}.csv'.replace(" ", "_")
    group.to_csv(f'/mnt/data/{file_name}', index=False)

# Step d: Display a summary of each subset of data using .describe()
group_summaries = {f'{species}_{island}': group.describe() for (species, island), group in species_island_groups}






