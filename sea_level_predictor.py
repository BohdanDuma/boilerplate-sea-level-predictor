import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax = plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    years_extended = np.arange(df['Year'].min(), 2051)
    pred = date.intercept + date.slope * years_extended
    ax = plt.plot(years_extended, pred, color='red', label='Best Fit Line')
    

    # Create second line of best fit
    df_group = df[df['Year'] >= 2000]
    data_group = linregress(df_group['Year'], df_group['CSIRO Adjusted Sea Level'])
    years_extended_gr = np.arange(df_group['Year'].min(), 2051)
    predict = data_group.intercept + data_group.slope * years_extended_gr
    ax = plt.plot(years_extended_gr, predict, color='red', label='Best Fit Line')
    # Add labels and title
    ax = plt.title('Rise in Sea Level')
    ax = plt.xlabel('Year')
    ax = plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()