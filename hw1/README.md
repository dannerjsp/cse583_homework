This file contains a description of the hw1.py assignment.

# 8. Describe your process for doing this homework. (If you used an AI assist, please tell us so here. It will not affect your grade as long as you tell us.) Answer this question by editing the README.md file. (1pt)

1. Work started in hw1.py. By importing pandas as pd, which I've been told is standard practice.
Followed by reading the .csv file into a pandas dataframe.

2. Slowly started getting overwhelmed with running commands in the terminal. And looked into opening a notebook. I get the purpose of having us not rely on notebooks to write all our code in it, which was the only way I was taught. Ultimately, I just needed something familiar to work in so that I didn't have to restart the kernel every time I walked away.
After opening a new notebook. I looked at some old assignments which had some data analysis code chunks that I used to start looking at the data, like .info() and .describe(). 
I noticed that some of the columns were in float64, which I had to ask Claude what the difference between float64 and a plain old float. I also thought I should change it to an integer, Claude suggested Int64. As for the date column being a string datatype, I'm familiar with datetime from a previous time series project. I tried figuring out the code via the datetime documentation (https://docs.python.org/3/library/datetime.html) and GeeksforGeeks. After a bit, I had to give my code to Claude to help me iron out the kinks. 

3. I added new columns 'East' and 'West' to replace 'Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk' and 'Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk', respectively. Which also allowed me to change the datatypes to Int64 via chaining. I calculated a 'Total (East + West) bicycle count' column from the sum of the 'East' and 'West' columns. I was going to double check to see if the 'Total (East + West) bicycle count' was equal to the original 'Fremont Bridge Sidewalks, south of N 34th St Total' column, but that wasn't asked of me so I thought it would be overkill. 
I added the 'Hour' and 'Year' columns and changed their datatypes to Int64. 

4. Created a subset dataframe where 'Year' was 2016. Claude was insistent that I make a copy so that it functioned as an independent dataframe so as not to impact the original. And I double-checked to ensure that only 2016 entries where in the new subset. 

5. I pulled this one from a quick google search on how to count missing by columns. There was only one row that was missing data, I assumed it was the same row. Trying to figure out which hour was missing data was a bit difficult. I took a first crack at it, but got tripped up by the syntax and turned to Claude for help. Claude suggested turning it into a variable and print the Date column. Which printed out a single row... '30181   2016-03-13 02:00:00'

6. I knew I was going to have trouble with this one, usually I just have Claude write it for me. This time, I tried to do it myself using the documentation for matplotlib. I ended up with a line plot of all the totals with the appropriate labels. I struggled with the syntax for it, which Claude painstakingly walked me through. The first part was grouping and summing by hour. This was done using .groupby()[].sum(). 
I didn't like the line plot so much, so then I looked at how I could do this with a histogram so it was easier to read. This had a slightly different syntax which Claude helped me work out.

7. This one I took a guess at and tried altering the groupby() code from 6, just switching .sum() out for .mean(). Definitely surprised it worked. I felt proud of that. At first, I thought it would be as easy as just tacking on .max(). But it wasn't that simple, I only got the largest average, which didn't give me the corresponding hour. So turned to Claude who explained that we need to reference the busiest hour and save it in it's own variable using .idxmax(). I feel like I could have just shortened this to print(hourly_avg_2016.idxmax(), hourly_avg_2016.max()). This worked btw, instead of making a whole new variable. 
