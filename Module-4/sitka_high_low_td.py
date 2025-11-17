# Tiffany Davidson
# CSD-325 Module 4.2 - High / Low Temperatures
#
# Program based on sitka_highs.py, updated to:
#   - Load both high and low temperatures from the CSV file
#   - Show a simple menu: Highs, Lows, or Exit
#   - Plot highs in red and lows in blue
#   - Loop until the user chooses to exit
#   - Print an exit message when the program ends

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

FILENAME = "sitka_weather_2018_simple.csv"


def load_weather_data(filename):
    """Load dates, high temps, and low temps from the CSV file."""
    dates, highs, lows = [], [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], "%Y-%m-%d")
                high = int(row[5])   # TMAX
                low = int(row[6])    # TMIN
            except ValueError:
                # Skip rows with missing or bad data
                continue

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


def plot_highs(dates, highs):
    """Plot daily high temperatures in red."""
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red")

    plt.title("Daily high temperatures - 2018", fontsize=20)
    plt.xlabel("", fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis="both", which="major", labelsize=12)

    plt.show()


def plot_lows(dates, lows):
    """Plot daily low temperatures in blue."""
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c="blue")

    plt.title("Daily low temperatures - 2018", fontsize=20)
    plt.xlabel("", fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis="both", which="major", labelsize=12)

    plt.show()


def main():
    print("Sitka Weather Viewer")
    print("This program lets you view graphs of daily high or low")
    print("temperatures for Sitka, Alaska, for the year 2018.\n")

    dates, highs, lows = load_weather_data(FILENAME)

    while True:
        print("Menu:")
        print("  1. Show high temperatures")
        print("  2. Show low temperatures")
        print("  3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ").strip().lower()

        if choice in ("1", "high", "highs", "h"):
            plot_highs(dates, highs)
        elif choice in ("2", "low", "lows", "l"):
            plot_lows(dates, lows)
        elif choice in ("3", "exit", "e", "q"):
            print("\nExiting program. Thanks for using the Sitka Weather Viewer.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
