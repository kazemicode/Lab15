# Lab 15

import random
import calendar
import datetime

##################################
# Problem 1: Craps

# A die is defined as by number of sides and can roll a random number between 1 and number of sides
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

# Create two six-sided dice
die1 = Die(6)
die2 = Die(6)
# Keep track of "point" in our game of Craps
point = 0
# Keep track of number of rolls
count = 0

# Win and lose conditions of the first roll
craps_dict = {
    2: False,
    3: False,
    12: False,
    7: True,
    11: True

}


# play_craps function takes two dice objects and calculates their rolled sums
# Gets called recursively if neither the win or lose conditions are met
def play_craps(die1, die2):

    global count
    global point
    roll = die1.roll() + die2.roll()    # sum of the two rolled dice
    count = count + 1                   # Just rolled, so update count by one
    print("Roll #", count, ":", roll)

    if count == 1 and roll in craps_dict: # Game ends on first roll if we land on a winning or losing combination
        return craps_dict[roll]           # True = win; False = loss

    elif roll == point:                   # On rolls other than the first, if you roll the same as the last roll,
        return True                       # you win.

    elif roll == 7:                       # On rolls other than the first, if you roll a 7, you lose.
        return False

    else:
        point = roll                      # Store the roll as the current "point" and roll again
        return play_craps(die1, die2)     # only if none of the above conditions are met.


##################################
#   Problem 2: Calendars and Dates

# Prints out a calendar of the month you were born, given the month and year
def print_bday_month(month, year):
    print(calendar.month(year, month))

# Returns how many days it is until your next birthday
def days_til_bday(today, bday):
    if(today.month > bday.month or (today.month == bday.month and today.day > bday.day)):
        next_bday = datetime.datetime(today.year + 1, bday.month, bday.day)
    else:
        next_bday = datetime.datetime(today.year, bday.month, bday.day)
    difference = next_bday - today
    days = difference.total_seconds()/86400
    return days

# Prints the day of the week, month, day, and year
def print_date(month, day, year):
    date = datetime.datetime(year, month, day)
    print(date.strftime("%A, %B %d, %Y"))


def main():
    print("Problem 1: Craps\n***************\n")
    result = play_craps(die1, die2)
    if result:
        print("You win!")
    else:
        print("You lose.")
    print("\nProblem 2: Calendars and Dates\n***************\n")
    year = 1983
    month = 11
    day = 1
    print_bday_month(month,year)
    birthday = datetime.datetime(year, month, day)
    today = datetime.datetime.now()
    print("Days until next birthday: ", round(days_til_bday(today, birthday)))
    print("***********************************\n\n")
    print("The Declaration of Independence was ratified on:")
    print_date(7, 4, 1776)


main()












