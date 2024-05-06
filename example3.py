# Enter a number of days through the keyboard and the days in hours, minutes and seconds. For example 1 day = 24 hours = 1440 minutes = 86400 seconds

def convert():
    print("add a number of days")
    numOfDays = int(input())
    numOfHours = numOfDays * 24
    numOfMinutes = numOfHours * 60
    numOfSeconds = numOfMinutes * 60
    print(numOfHours, numOfMinutes, numOfSeconds)

convert()
 