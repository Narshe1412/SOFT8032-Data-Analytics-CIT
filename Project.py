# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:50:36 2017

@author: Manuel Colorado
@studentid: R00156054

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movie_data.csv') 


##1
def topgross(df, work_column, amount, colname):
    # Number formatting to add thousands separator
    pd.options.display.float_format = '${:,.0f} USD'.format
    
    # Aggregating and filtering dataset
    groupeddf = df.groupby(work_column)
    # We sum the desired column gross' value, sorting them descending and only 
    # grabbing the top X, based on amount parameter
    top10 = groupeddf['gross'].sum().sort_values(ascending = False).head(amount)

    # Plot
    top10.plot.bar(title = "Top "+ str(amount) + " gross earners")
    plt.xlabel(colname)
    plt.xticks(rotation='90')
    plt.ylabel('Gross earnings in millions')
    plt.show()

##2  
def grossDistribution(df, startyear, stopyear):
    # Number formatting to add thousands separator and remove decimals
    pd.options.display.float_format = '{:,.0f}'.format
    
    # Filtering dataset based on the range of years
    yearfilter = (df['title_year'] >= startyear) & (df['title_year'] <= stopyear)
    # Remove rows where 'gross' is non-existant
    filtereddf = df[yearfilter].dropna(subset=['gross'])
    # Create a dataframe with min, max and average values from gross data
    groupeddf = filtereddf.groupby('title_year')
    summarizeddf = groupeddf['gross'].agg(['min', 'max', 'mean'])
    
    # Plot
    summarizeddf.plot()
    plt.title("Summary of gross earnings in movies per year")
    # To make it look nicer, we make sure that we display at least 5 years
    if (stopyear - startyear) < 5:
        labels = range(startyear, stopyear+1)
    else:
        labels = range(startyear, stopyear+1, (stopyear-startyear) // 5)
    plt.xticks(labels)
    plt.xlabel("Year of production")
    plt.ylabel("Gross earnings")
    plt.show()
 
##3
def imdbscores(df):
    # We create buckets based on range of 0.5 scores
    # 0-0.5, 0.5-1, 1-1.5.....9.5-10
    rangefilter = np.arange(0, 10.1, 0.5)
    dffilter = pd.cut(df['imdb_score'], rangefilter)
    # We group by 
    groupeddf = df.groupby(dffilter)
    summarizeddf = groupeddf['gross'].mean()
    
    # Plot
    summarizeddf.plot.bar(title = "IMDB Score to Average earnings")
    plt.axis([0, 10, 0, 2*10**8])
    # Change X axis to not display range of values and just values
    labels = np.arange(0, 10.5, 0.5)
    plt.xticks(range(0,21), labels, ha='center')
    plt.xlabel("IMDB Score")
    plt.ylabel("Average earnings in thousand of millions")
    plt.show()    
    
##4
def getuniquegenres(df):
    # Get a series of strings with genrse for each movie
    splitted = df['genres'].str.split('|')
    # Unpivot series into a single column
    stacked = pd.DataFrame(splitted.tolist()).stack()
    # Get unique values from the unpivoted column
    return pd.unique(stacked)
    
def genreanalysis(df, genre):
    # Filter dataset to only show movies with the genre passed as argument
    genrefilter = df['genres'].str.contains(genre)
    filtereddf = df[genrefilter]
    # Group and average imdb score from the filtered dataset
    average = filtereddf['imdb_score'].mean()
    
    # Show average if it exists, otherwise specify the error message
    if (average > 0):
        print("The average score for the '" + genre + "' genre is " + str(round(average, 3)))
    else:
        print("There's no data for the selected genre.")
##5
def profitable(df, workcolumn, amount, name):
    # Formatting long values to display as money format
    pd.options.display.float_format = '${:,.0f} USD'.format
    
    # Create a new column on the dataset, based on the profit obtained from the movie
    df['profit'] = df['gross'] - df['budget']
    # Filter those with positive profit values
    profitable = df['profit'] > 0
    filtereddf = df[profitable]
    # Group by selected column (directors, but can be changed later) and calculate
    # the top X amount based on profitability
    groupeddf = filtereddf.groupby(workcolumn)
    summary = groupeddf['profit'].mean().sort_values(ascending= False).head(amount)
    
    # Plot
    summary.plot.bar(title = "Top "+ str(amount) + name)
    plt.xlabel(name)
    plt.xticks(rotation='90')
    plt.ylabel('Profit in millions')
    plt.show()

##Menu
def menu():
    choice = ""
    while (choice != "0"):
        print("Please select one of the following options: \n\
        1. Most successful directors or actors \n\
        2. Analyse the distribution of gross earnings \n\
        3. Earnings and IMDB scores \n\
        4. Genre Analysis \n\
        5. Most profitable directors\n\
        0. Exit")
        choice = input("Choose an option: ")
        if (choice == "1"):
            topamount = input("Please enter the amount of results you want to view: ")
            selection = input("Do you want to see top (D)irectors or (A)ctors? ")
            if (selection == "D" or selection == "d"):
                topgross(df, 'director_name', int(topamount), 'Top earning directors')
            elif (selection == "A" or selection == "a"):
                actors_selectdf = df[['actor_3_name', 'actor_2_name', 'actor_1_name', 'gross']]
                actors_unpivotdf = pd.melt(actors_selectdf, id_vars=['gross'], var_name='actor', value_name='actor_name')
                topgross(actors_unpivotdf, 'actor_name', int(topamount), 'Top earning actors')
        elif (choice == "2"):
            startyear = input("Please select the starting year: ")
            stopyear = input("Please select the finish year: ")
            grossDistribution(df, int(startyear), int(stopyear))
        elif (choice == "3"):
            imdbscores(df)
        elif (choice == "4"):
            print("Selecte one of the following genres:")
            print(getuniquegenres(df))
            genre = input("Please enter your genre: ")
            genreanalysis(df,genre)
        elif (choice == "5"):
            profitable(df, 'director_name', 10, ' Most profitable directors')
        elif (choice == "0"):
            print("Thanks for using our app")
        else:
            print("Wrong option selected.")
        print("\n*************************\n")
            

menu()
