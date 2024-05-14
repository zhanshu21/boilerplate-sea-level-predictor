import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')
    fig, ax = plt.subplots(figsize = (20,12))
    # Create scatter plot
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original data')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_1 = range(df['Year'].min(), 2051)
    y_1 = res.intercept + res.slope*x_1
    ax.plot(x_1, y_1, 'green', label='First fitted line')
    
    # Create second line of best fit
    df_last = df[df['Year'] >= 2000]
    res_last = linregress(df_last['Year'], df_last['CSIRO Adjusted Sea Level'])
    
    # Add labels and title
    x_2 = range(df_last['Year'].min(), 2051)
    y_2 = res_last.intercept + res_last.slope*x_2
    ax.plot(x_2, y_2, 'r', label='Second fitted line')
    ax.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return fig.gca()