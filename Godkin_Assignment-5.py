# ! /usr/bin/env python3

# Assignment 5 - Data Visualization
# Author: Ralph Godkin

'''
General Comments: This Assignment retrieves data from a database and uses
some Python modules to plot the selected data in a line chart.
The log file 'data_visualization.log' tracks the application progress.
 '''

# Imports
import logging as log                 # FOR LOGGING
import os                             # USED FOR SOME PATH MANAGEMENT
import sqlite3                        # USED FOR DATABASE FUNCTIONS
import matplotlib.pyplot as plt       # USED FOR PLOTTING THE DATA
import pandas as pd                   # USED TO PREP THE DATA FOR PLOTTING

# Configure the logging module
log.basicConfig(filename="data_visualization.log", level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
log.getLogger('matplotlib.font_manager').disabled = True

# Update log 
log.info('+++   Starting App   +++') 


def get_database_path(file_name):
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Create the full path to the database file
    database_path = os.path.join(current_directory, file_name)
    
    log.info(f'Current Directory: {current_directory} + Database Path: {database_path}') 
              
    return database_path

database_file = 'degrees2.db'
db_path = get_database_path(database_file)

def get_the_data():
    # Open the database connection
    # Ensure the database exists prior to continueing. Thereby preventing a database being created by this application
    if os.path.exists(database_file):
        conn = sqlite3.connect(db_path)
    else:
        print(f"Database file '{db_path}' was not found.")    
        return

    # Create a cursor object to execute SQL statements
    cursor = conn.cursor()

    # Update log
    log.info('Successfully: (1)connected to database  (2)created cursor') 

    # # Perform database queries
    cursor.execute("SELECT Year, Business, Architecture, ComputerScience, SocialSciencesandHistory FROM degrees ;")
    results = cursor.fetchall()
    # Convert the fetched data into a DataFrame
    df = pd.DataFrame(results, columns=["Year", "Business", "Architecture", "ComputerScience", "SocialSciencesandHistory"])
    
    # Update log
    log.debug('Data loaded successfully.') 

    return df

def plot_the_data(results):

    # Update log
    log.info('Starting code to plot the data.') 

    # Set title
    plt.title('USA Female degree counts by major (1970-2011)', fontsize=20)

    # Set x and y axis labels
    plt.xlabel('Year')
    plt.ylabel('Female Graduates')

     # Define plot
    plt.plot(results["Year"], results["Business"], label='Business')
    plt.plot(results["Year"], results["Architecture"], label='Architecture')
    plt.plot(results["Year"], results["ComputerScience"], label='ComputerScience')
    plt.plot(results["Year"], results["SocialSciencesandHistory"], label='Social Sciences & History')
    
    # Set legend
    plt.legend()

    # Save the image
    # plt.savefig("Female_Degree_linechart.png")

    # Show the image
    plt.show()

    # Update log
    log.info('Plot drawn successfully.') 



def main():
    results = get_the_data()

    plot_the_data(results)  

    # Update log
    log.info('*** App completed ***') 


if __name__ == "__main__":
    main()