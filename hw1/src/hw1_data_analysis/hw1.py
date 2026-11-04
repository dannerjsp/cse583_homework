"""
1. Read the CSV file into a pandas dataframe. (1pt)
2. In a comment, describe the columns in the dataframe and what data types they should be. If the data types in the dataframe do not match what you think they should be, update them. (1pt)
3. Add columns to the dataframe containing:
    - The total (East + West) bicycle count. (1pt)
    - The hour of the day. (1pt)
    - The year. (1pt)
4. Create a new dataframe with the subset of data from the year 2016. (1pt)
5. For the dataframe you created in 4, are there any time points with missing data? If so, do something to make sure missing data does not impact parts 6 and 7. In a comment in the code write out the number of points with missing data. (1pt)
6. For the dataframe you created in 4, use pandas + matplotlib to plot the counts by hour (i.e. hour of the day on the x-axis, total daily counts on the y-axis). Add an appropriate title and name the axes and save the image to a file called counts_by_hour.png. (1pt)
7. For the dataframe you created in 4, use python (and pandas) programming to computationally determine what is (on average) the busiest hour of the day. In a comment in the code write out the busiest hour (1pt)
8. Describe your process for doing this homework. (If you used an AI assist, please tell us so here. It will not affect your grade as long as you tell us.) Answer this question by editing the README.md file. (1pt)
"""

import pandas as pd

# 1. Read the CSV file into a pandas dataframe. (1pt)
df = pd.read_csv('bicycle_data.csv')



# 2. In a comment, describe the columns in the dataframe and what data types they should be. 
#    If the data types in the dataframe do not match what you think they should be, update them. (1pt)
#                                                                                                       Should be
# 0   Date                                                                122675 non-null  str          datetime
# 1   Fremont Bridge Sidewalks, south of N 34th St Total                  122645 non-null  float64      int
# 2   Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk  122645 non-null  float64      int
# 3   Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk  122645 non-null  float64      int

from datetime import datetime

# Change data type in the Date column from str to datetime
df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y %I:%M:%S %p')

print(df['Date'].head(4))



# 3. Add columns to the dataframe containing:
#    - The total (East + West) bicycle count. (1pt)
# Addding new columns and changes data types to Int64
df['East'] = df['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk'].astype('Int64')
df['West'] = df['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'].astype('Int64')

# Adds the new East and West columns to a new Total column
df['Total (East + West) bicycle count'] = df['East'] + df['West']

#    - The hour of the day. (1pt)
# Extract hour into a new column
df['Hour'] = df['Date'].dt.hour
df['Hour'] = df['Hour'].astype('Int64')

#    - The year. (1pt)
# Extract year into a new column
df['Year'] = df['Date'].dt.year
df['Year'] = df['Year'].astype('Int64')



# 4. Create a new dataframe with the subset of data from the year 2016. (1pt)
# Create a subset df with 2016 numbers
df_2016 = df[df['Year'] == 2016].copy()         # adding .copy() makes it an independent df

# Prints the shame of the new df_2016 dataframe
print(df_2016.shape)

# Checks if df_2016 has any other Year entries. It should only be 2016.
print(df_2016['Year'].unique())



# 5. For the dataframe you created in 4, are there any time points with missing data? If so, do something to make sure missing data does not impact parts 6 and 7. In a comment in the code write out the number of points with missing data. (1pt)
# Counts and prints the number of missing variables by column in the 2016 subset
df_2016.isnull().sum()

# Creates variable for missing data in 2016
missing_2016 = df_2016[df_2016['Total (East + West) bicycle count'].isnull()]

# Prints missing date and hour.
missing_2016['Date']

# There's only one missing row from the 2016 subset at `30181   2016-03-13 02:00:00`.



# 6. For the dataframe you created in 4, use pandas + matplotlib to plot the counts by hour (i.e. hour of the day on the x-axis, total daily counts on the y-axis). Add an appropriate title and name the axes and save the image to a file called counts_by_hour.png. (1pt)

import matplotlib.pyplot as plt

# Plots a histogram of the data
plt.hist(
    df_2016['Hour'], 
    bins=24, 
    range=(0, 24), 
    weights=df_2016['Total (East + West) bicycle count'])

# Structural annotations 
plt.title('Total Bike Counts by Hour, 2016')
plt.xlabel('Hour of the Day')
plt.ylabel('Count')



# 7. For the dataframe you created in 4, use python (and pandas) programming to computationally determine what is (on average) the busiest hour of the day. In a comment in the code write out the busiest hour (1pt)
# Groups by hour and takes the average and saves in variable hourly_avg_2016
hourly_avg_2016 = df_2016.groupby('Hour')['Total (East + West) bicycle count'].mean()

# Finds the busiest hour and identifies which index (the hour)
busiest_hour = hourly_avg_2016.idxmax()

print(busiest_hour, hourly_avg_2016.max())
# Using the 2016 subset, the busiest hour of the day on average is 17:00 with 366.03 bicycles.  



# 8. Describe your process for doing this homework. (If you used an AI assist, please tell us so here. It will not affect your grade as long as you tell us.) Answer this question by editing the README.md file. (1pt)


