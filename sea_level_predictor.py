import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Sea level data', marker='.')

    # Create first line of best fit
    first_line_fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    m1 = first_line_fit.slope
    b1 = first_line_fit.intercept
    years = np.array([x for x in range(df['Year'].min(), 2051)]) # Since 1880 to 2050
    sea_level_lf1 = np.array([m1*x+b1 for x in years])
    ax.plot(years, sea_level_lf1, color='red', label=f"1st Line of best fit: sea_level = {round(m1,2)}*year {round(b1,2)}")
    
    # Create second line of best fit
    df_v2 = df.loc[df['Year']>=2000, ['Year', 'CSIRO Adjusted Sea Level']] # Filtering data from since 2000
    second_line_fit = linregress(df_v2['Year'], df_v2['CSIRO Adjusted Sea Level'])
    m2 = second_line_fit.slope
    b2 = second_line_fit.intercept
    years = np.array([x for x in range(df_v2['Year'].min(), 2051)]) # Since 2000 to 2050
    sea_level_lf2 = np.array([m2*x+b2 for x in years])
    ax.plot(years, sea_level_lf2, color='green', label=f"2nd Line of best fit: sea_level = {round(m2,2)}*year {round(b2,2)}")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.grid(True)
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()