import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Below is the city and their corresponding numbers")
    print("1. chicago")
    print("2. new york city")
    print("3. washington\n")
    
    while True:
        city = input("Please choose a city to analyze from the above (Enter either by name or corresponding number): ")
        city = city.lower()
        if city == "1" or city == "chicago":
            city = "chicago" # re assigning it in case the user chose using the interger string
            print("You chose ", city)
            break
        elif city == "2" or city == "new york city":
            city = "new york city" # re assigning city in case the user chose using the interger string
            print("You chose ", city)
            break
        elif city == "3" or city == "washington":
            city = "washington" # re assigning city in case the user chose using the interger string
            print("You chose ", city)
            break
        else:
            print("Invalid input, Please chose by entering name or corresponding number of the city(1,2,3) \n")
            continue



    # get user input for month (all, january, february, ... , june)
    print(" 1. January\n 2. February\n 3. March \n 4. April\n 5. May \n 6. June\n 7. all")
    while True:
        month = input("Please chose the name of the month to filter data by from above? (Either by name or corresponding number) \n")
        month.lower()
        if month == "1" or month == "january":
            month = "january" # re assigning the month in case the user chose the corresponging integer string
            break
        elif month == "2" or month == "february":
            month = "february" # re assigning the month in case the user chose the corresponging integer string
            break
        elif month == "3" or month == "march":
            month = "march" # re assigning the month in case the user chose the corresponging integer string
            break
        elif month == "4" or month == "april":
            month = "april" # re assigning the month in case the user chose the corresponging integer string
            break
        elif month == "5" or month == "may":
            month = "may" # re assigning the month in case the user chose the corresponging integer string
            break
        elif month == "6" or month == "june":
            month = "june" # re assigning the month in case the user chose the corresponging integer string
            break
        elif month == "7" or month == "all":
            month = "all" # re assigning the month in case the user chose the corresponging integer string
            break
        else: 
            print("Invalid input, please chose by entering name of month or corresponging number(1,2,3,4,5,6,7)")
            continue


    # get user input for day of week (all, monday, tuesday, ... sunday)
    print(" 1. Monday\n 2. Tuesday\n 3. Wednesday \n 4. Friday\n 5. May \n 6. Saturday \n 7. Sunday \n 8. all")
    while True:
        day = input("Please chose the name of the day to filter data by (from above either by name or corresponding number)? \n")
        day = day.lower()
        if day == "1" or day == "monday":
            day = "monday" # re assigning the day in case the user chose the corresponging integer string
            break
        elif day == "2" or day == "tuesday":
            day = "tuesday" # re assigning the day in case the user chose the corresponging integer string
            break
        elif day == "3" or day == "wednesday":
            day = "wednesday" # re assigning the day in case the user chose the corresponging integer string
            break
        elif day == "4" or day == "thursday":
            day = "thursday" # re assigning the day in case the user chose the corresponging integer string
            break
        elif day == "5" or day == "friday":
            day = "friday" # re assigning the day in case the user chose the corresponging integer string
            break
        elif day == "6" or day == "saturday":
            day = "saturday" # re assigning the day in case the user chose the corresponging integer string
            break
        elif day == "7" or day == "sunday":
            day = "sunday" # re assigning the day in case the user chose the corresponging integer string
            break
        elif day == "8" or day == "all":
            day = "all" # re assigning the day in case the user chose the corresponging integer string
            break
        else: 
            print("Invalid input, please chose by entering name of day or corresponging number(1,2,3,4,5,6,7,8)")
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading the data file into a dataframe
    fileName = CITY_DATA[city]
    print ("Accessing data from: " + fileName)
    df = pd.read_csv(fileName)

    # converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

    #filter by month if applicable
    if month != 'all':
        #extracting month and day of week from Start Time to create new columns
        df['month'] = df['Start Time'].dt.month

        #using the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    #filter by day of week if applicable
    if day != 'all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name

        # filtering by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #converting the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

    #creating new columns for month, weekday and hour 
    month = df['Start Time'].dt.month
    weekday_name = df['Start Time'].dt.weekday_name
    hour = df['Start Time'].dt.hour

    # display the most common month
    most_common_month = month.mode()[0]
    print("Most common month: ", most_common_month )

    # display the most common day of week
    most_common_day_of_week = weekday_name.mode()[0]
    print('Most Common Day of the week: ', most_common_day_of_week)

    # display the most common start hour
    most_common_start_hour = hour.mode()[0]
    print('Most Common start hour: ', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station: ', start_station)

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station: ', end_station)

    # display most frequent combination of start station and end station trip 
    print('Most frequent combination of start station and end station string: ', start_station,' and ', end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time/86400, ' Days') #divding by the number of seconds in a day (24 hours = 86400 seconds)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time/60 ,' Minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ', user_types)

    # Display counts of gender
    try: 
        gender_count = df['Gender'].value_counts()
        print('Counts of gender: ', gender_count)
    except:
        print('Sorry !! No gender data available')

    # Display earliest, most recent, and most common year of birth
    try: 
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest year of birth: ', earliest_birth_year)
    except:
        print('Sorry !! No earliest birth year data available for this period')
        
        
    try:
        most_recent_birth_year = df['Birth Year'].max()
        print('\nMost recent year of birth: ', most_recent_birth_year)
    except:
        print('Sorry !! No most recent birth year data available for this period')
        
    try:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common year of birth: ', most_common_birth_year)
    except:
        print('Sorry !! No most common birth year data available for this period')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    #Displays some (five) lines of raw data at a time  

    user_request = input('Would you like to see raw data ? Please enter \'yes\' or \'no\': ')
    #user_request = user_request.lower()
    line_counter = 0

    while True:
        if user_request.lower() == 'no':
            break
        elif user_request.lower() == 'yes':
            print(df.iloc[line_counter : line_counter + 5])
            line_counter = line_counter + 5
            user_request = input('Would you like to see more five lines of raw data? Please enter \'yes\' or \'no\': ')
        else:
            print('\n\n Invalid Input: Please enter \'yes\' or \'no\' ')
            user_request = input('Would you like to see raw data? ')
            continue

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        #if restart.lower() != 'yes':
        #    break
        #letting the user know when the pragram ends because of invalid input
        if restart.lower() == 'yes':
        	continue
        elif restart.lower() == 'no':
        	break
        else:
        	print("\nInvalid input: Sorry please try again ! ")
        	break

if __name__ == "__main__":
	main()
