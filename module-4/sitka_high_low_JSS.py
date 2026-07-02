#Jack Summers
#Module 4.2 Assignment
#7/1/2026

import csv
import sys

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and LOW temperatures from this file.
    #7/1/2026 adding code to get low temperature data
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)


#7/1/2026 Updates: program controller - user inputs values
#once a valid input is given, program will display a graph or exit.
#once a graph is created, you will have to close out of the graph before program prompts you to continue.
while True:
    try:
        userChoice = int(input("Select a Value: \n"                                        
                               "1: View HIGH temperatures throughout the year.\n"          
                               "2: View LOW temperatures throughout the year.\n"           
                               "3: Exit Program: "))
    #catches any non-int input
    except:
        userChoice = int(input("Select a Value from the list this time PLEASE: \n"
                               "1: View HIGH temps.\n"
                               "2: View LOW temps.\n"
                               "3: Quit "))

    if userChoice == 1: #EXISTING
        # Plot the high temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily HIGH temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
        print('-' * 55)

    elif userChoice == 2:
        #7/1/2026 Addition
        #plot the low temperatures
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        #format plot.
        plt.title("Daily LOW temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()
        print('-' * 55)

    elif userChoice == 3:
        #7/1/2026 Addition
        #Exits program (safely)
        print('-' * 55)
        print("Thanks for using! "                                               
              "Exiting Program...")
        sys.exit()

    else:
        #7/1/2026 Addition
        #Catches any int-inputs that are not 1,2,3.
        print("Invalid choice. Please select one of the options below.")
        print("1, 2, 3")
