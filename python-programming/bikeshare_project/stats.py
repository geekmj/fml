import time
import datetime
import utilities as ut


def time_stats(df, show_month_stat, show_day_stat, months_list, days_list):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (dataframe) df - Panda dataframe with bikeshare data
        (boolean) show_month_stat - show or not show month stat
        (boolean) show_day_stat - show or not show day of week stat
        (list) months_list - List of month's title
        (list) days_list - List of day's title
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if show_month_stat:
        # display the most common month

        # Get most popular month
        most_popular_month = df['month'].mode()[0]

        # Get most popular month count
        most_popular_month_count = df['month'].value_counts()[
            most_popular_month]

        print("\n* Most popular Month: {} ({} occurences)".format(
            months_list[most_popular_month - 1].capitalize(),
            most_popular_month_count))
    else:
        print(
            "\n* Most popular month: NA (Looks like you have filter on month)")

    if show_day_stat:
        # display the most popular day of week

        # Get most popular day of week
        most_popular_day_of_week = df['day_of_week'].mode()[0]

        # Get most popular day of week count
        most_popular_day_of_week_count = df['day_of_week'].value_counts()[
            most_popular_day_of_week]

        print("\n* Most popular day of week: {} ({} occurences)".format(
            days_list[most_popular_day_of_week].capitalize(),
            most_popular_day_of_week_count))

    else:
        print(
            "\n* Most popular day of week: NA (Looks like you have filter on day of week)"
        )

    # display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # Get most popular hour
    most_popular_hour = df['hour'].mode()[0]

    # Get most popular hour count
    most_popular_hour_count = df['hour'].value_counts()[most_popular_hour]

    # Use utility function to format hour to pretty format
    most_popular_hour_str = datetime.time(
        hour=most_popular_hour).strftime("%I %p")

    print("\n* Most popular hour to start: {} ({} occurences)".format(
        most_popular_hour_str, most_popular_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        (dataframe) df - Panda dataframe with bikeshare data
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\n* Most commonly used start station: {}".format(
        df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("\n* Most commonly used end station: {}".format(
        df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip

    # Find most popular start and end station group and count
    start_end_station_group_by_count = df.groupby(
        ['Start Station', 'End Station'])['Start Station'].count()

    # Print Start and End station
    print(
        "\n* Most commonly used start & end station combination: '{}' and '{}' ({} occurrences) ".
        format(start_end_station_group_by_count.idxmax()[0],
               start_end_station_group_by_count.idxmax()[1],
               start_end_station_group_by_count.max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
   
    Args:
        (dataframe) df - Panda dataframe with bikeshare data
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("\n* Total travel time: {}".format(
        ut.display_time(df['Trip Duration'].sum())))

    # display mean travel time
    print("\n* Total average (mean) travel time: {}".format(
        ut.display_time(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    
    Args:
        (dataframe) df - Panda dataframe with bikeshare data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nCalculating User Types stats:")

    # Display counts of user types

    # Find user types count
    user_types_count = df['User Type'].value_counts()

    # Print Subscribers
    print("\n* Total Subscribers: {}".format(user_types_count['Subscriber']))

    # Print Customers
    print("\n* Total Customers: {}".format(user_types_count['Customer']))

    # Display counts of gender

    # Check if gender column exist, as few state don't have gender data

    print("\nCalculating Gender stats:")
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()

        # Display Total Male
        print("\n* Total Male users: {}".format(gender_count['Male']))

        # Display Total Female
        print("\n* Total Female users: {}".format(gender_count['Female']))
    else:
        # In case there is no Gennder data, display appropriate message

        print(
            "\n* Total Male users: NA (Looks Like washington don't have Gender Data)"
        )

        print(
            "\n* Total Female users: NA (Looks Like washington don't have Gender Data)"
        )

    # Display earliest, most recent, and most common year of birth

    # Check if gender column exist, In some state it is not available
    print("\nCalculating Birth Year stats:")

    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']

        # Display earliest year of birth
        print("\n* Earliest year of birth: {} ".format(int(birth_year.min())))

        # Display most recent year of birth
        print("\n* Most recent year of birth: {}".format(
            int(birth_year.max())))

        # Display most common year of birth
        print("\n* Most common year of birth: {} ({} occurance)".format(
            int(birth_year.median()),
            birth_year.value_counts()[int(birth_year.median())]))
    else:

        # In case there is no birth data
        print(
            "\n* Earliest year of birth: NA (Looks Like washington don't have Birth Year Data)"
        )

        print(
            "\n* Most recent year of birth: NA (Looks Like washington don't have Birth Year Data)"
        )

        print(
            "\n* Most common year of birth: NA (Looks Like washington don't have Birth Year Data)"
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)