import time
import pandas as pd
import numpy as np

pd.set_option('display.width', None)

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    #                   CITY
    # ask user to enter a chosen city and store this data in a variable
    print('\n' + '*' * 35 + ' CITY ' + '*' * 35)
    city = input('\nEnter a city name (Chicago, New york city, Washington) to analyze:\n').lower()

    # check if user entered correct city and if not ask him to choose the correct one one more time
    while city not in ['chicago', 'new york city', 'washington']:
        print(f'\nYou have chosen "{city.capitalize()}" which is not in a list for analyzing')
        city = input('\nEnter a city name (Chicago, New york city, Washington) to analyze:\n').lower()

    # show chosen data start from capital letter
    print(f'\n\tYou have chosen "{city.capitalize()}"')

    #                   MONTH

    print('\n' + '*' * 35 + ' MONTH ' + '*' * 35)
    # ask user to specify a month
    month = input('\nEnter a month (all, january, february, march, april, may, june) to analyze:\n').lower()

    # check if writen word is a month and the month is in a list of months to analyze
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print(f'\nYou have chosen "{month.capitalize()}" which is not in a list for analyzing')
        month = input('\nEnter a month (all, january, february, ... , june) to analyze:\n').lower()

    # show chosen data start from capital letter
    print(f'\n\tYou have chosen "{month.capitalize()}"')

    #                   DAY

    print('\n' + '*' * 35 + ' DAY ' + '*' * 35)
    # ask user to specify a day
    day = input('\nEnter a day (all, monday, tuesday, ... sunday) to analyze:\n').lower()

    # check if writen word is a day of a week and the day is in a list of days to analyze
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print(f'\nYou have chosen "{day.capitalize()}" which is not in a list for analyzing')
        day = input('\nEnter a day (all, monday, tuesday, ... sunday) to analyze:\n').lower()

    # show chosen data start from capital letter
    print(f'\n\tYou have chosen "{day.capitalize()}"')

    print('-' * 40)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start time'].dt.month
    df['day_of_week'] = df['Start time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']  # months start from small letter
        month = months.index(month) + 1

    # filter by month to create the new dataframe
    df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    #               FREQUENT MONTH

    # calculate the most frequent month according to entered data
    month_max_item = df['month'].value_counts().idxmax()
    print(f'\n\tthe most common month is month - {month_max_item}')

    #               FREQUENT DAY OF WEEK

    # calculate the most frequent dat ot week according to entered data
    week_day_max_item = df['day_of_week'].value_counts().idxmax()
    print(f'\n\tthe most common day of week is day - {week_day_max_item}')

    #               MOST COMMON START HOUR

    # calculate the most common 'start hour' according to entered data
    start_time_max_item = df['Start time'].value_counts().idxmax()
    print(f'\n\tthe most common "start hour" is - {start_time_max_item}')

    print("\n\tThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # TO DO: display most commonly used start station (Start Station)

    # count all different names of start stations and get the one which was used the most
    most_com_st_station = df['Start Station'].value_counts().idxmax()
    print(f'\n\tthe most commonly used start station is - {most_com_st_station}')

    # TO DO: display most commonly used end station (End Station)

    # count all different names of end stations and get the one which was used the most
    most_com_end_station = df['End Station'].value_counts().idxmax()
    print(f'\n\tthe most commonly used end station is - {most_com_end_station}')

    # TO DO: display most frequent combination of start station and end station trip

    # finding the most frequent start station and end station
    freq_comb = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print(f'\n\tthe most frequent combination of start station and end station is\n\t {freq_comb}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # count the total travel time
    print('\tthe total travel time for all period is - {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time

    # count the mean travel time
    print('\n\tthe mean value of time is - {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # count all user types
    print('\tcounts of user types are next:\n\n{}\n\n'.format(df['User Type'].value_counts()))

    # check if a particular column is in dataframe.
    if 'Gender' not in df.columns:
        print('the dataframe does not contain "Gender" column')
    else:
        # if in it count amount of people different gender
        print('\tcounts of genders are next:\n\n{}\n\n'.format(df['Gender'].value_counts()))

    # the same checking as above but for "Birt Year" column
    if 'Birth Year' not in df.columns:
        print('the dataframe does not contain "Birth Year" column')
    else:
        int_type_column = df['Birth Year'].dropna().astype(int)

        # remove Nan values in "Birth Year", changing the data type to "int", count value and find most recent client
        # birth year and earliest client birth year
        print(f'\tthe most recent client birth is in {int_type_column.max()}\n\n')
        print(f'\tthe earliest client birth is in {int_type_column.min()}\n\n')

        # remove Nan values in "Birth Year", changing the data type to "int", count value and find the most common one
        print('\tthe most common year of birth is - {} year\n\n'.format(int_type_column.value_counts().idxmax()))
    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def raw_data(df):
    """Displays by five raw rows one by one on bikeshare users till user wants."""

    #  ask what type of data user prefers
    get_raw_info = input('You prefer to see raw info? Enter "y" to continue/"n"(or any) for exit to main menu:\n')

    # check if user wants to see raw data
    while get_raw_info.lower() == 'y':
        #  print out five rows
        five_at_time = df.head()
        print(f'\n{five_at_time}')
        get_raw_info = input('Would you prefer to see next five rows? Enter "y" to continue/"n"(or any) for exit to '
                             'main menu:\n')
        #  give you a new df without the first five rows.
        df = df.iloc[5:]


def checking_type(df):
    type_of_data = input('Enter what type of data you prefer to see. Enter "r" for "raw data" or "s" for '
                         '"statistic data"\n')
    while type_of_data.lower() != 'r' or type_of_data.lower() != 's':
        if type_of_data.lower() == 'r':
            raw_data(df)
            break
        elif type_of_data.lower() == 's':
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            break
        type_of_data = input('To continue please enter correct option (r/s)\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        checking_type(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
