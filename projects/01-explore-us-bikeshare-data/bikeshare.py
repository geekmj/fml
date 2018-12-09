import pandas as pd
import stats as st
import utilities as ut

# City & File Mapping
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}
# Cities List Constant
CITIES_LIST = ('chicago', 'new york city', 'washington')
# Months List Constant
MONTHS_LIST = ('january', 'february', 'march', 'april', 'may', 'june')
# Days List Constat
DAYS_LIST = ('monday', 'tuesday', 'wednesday', 'thrusday', 'friday',
             'saturday', 'sunday')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    """
    # get user choice for city data they want to explore
    city = ut.get_user_choice(CITIES_LIST, "City Filter Options:")

    # get user input for month (none, january, february, ... , june)
    month = ut.get_user_choice(["none"] + list(MONTHS_LIST),
                               "Month Filter Options")

    # get user input for day of week (none, monday, tuesday, ... sunday)
    day = ut.get_user_choice(["none"] + list(DAYS_LIST), "Day Filter Options")
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'none':
        # filter by month to create the new dataframe
        df = df[df['month'] == MONTHS_LIST.index(month) + 1]

    # filter by day of week if applicable
    if day != 'none':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == DAYS_LIST.index(day)]

    return df


def raw_data_display(df):
    """
    Displays raw output as long as user want and end of records reached.
    
    Args:
        (dataframe) df - Panda dataframe with bikeshare data
    """

    # Record index counter
    df_index_counter = 0

    # While dataframe size is greater than index counter
    while df.size > df_index_counter:

        optional_str = ""

        # This variable is use to introduce an extra word "more" in
        # user input statement after 1st iteration of data display done.
        if df_index_counter > 0:
            optional_str = " 5 more"

        # Use utility method to get user input to see raw data.
        see_raw_data = ut.get_user_choice(
            ["yes", "no"],
            "Would you like to see{} raw data?".format(optional_str), "No")

        if see_raw_data == "yes":
            # Check if user wants to see the raw data

            # Display pagination information
            print("\nShowing raw data no {} to {}".format(
                df_index_counter + 1, df_index_counter + 5))

            # chunk out dataframe for current batch of raw data display
            df_to_print = df.iloc[df_index_counter:df_index_counter + 5]

            for i, row in df_to_print.iterrows():

                # Iterate on raw data records

                # Display raw data values

                # Display record number
                print("\n\nRaw data no: {}".format(i + 1))

                # Display "User Type" value
                print("\n* User Type: {}".format(row["User Type"]))

                # Display "Start Station" value
                print("\n* Start Station: {}".format(row["Start Station"]))

                # Display "Start Time" value
                print("\n* Start Time: {}".format(row["Start Time"]))

                # Display "End Station" value
                print("\n* End Station: {}".format(row["End Station"]))

                # Display "End Time" value
                print("\n* End Time: {}".format(row["End Time"]))

                # Display "Trip Duration" value as is i.e. seconds
                print("\n* Trip Duration (In seconds): {}".format(
                    row["Trip Duration"]))

                if "Gender" in row.index:
                    # Check if Gender index exist

                    gender = row["Gender"]

                    if pd.isnull(gender):
                        # Check if NaN value
                        gender = "No Data"

                    # Display Gender
                    print("\n* Gender: {}".format(gender))
                else:

                    # Display no data in case Gender column don't exist
                    print("\n* Gender: No Data")

                if "Birth Year" in row.index:
                    # Check if "Birth Year" exist

                    birth_year = row["Birth Year"]

                    if pd.isnull(birth_year):
                        # Check if NaN value
                        birth_year = "No data"

                    # Display "Birth Year"
                    print("\n* Birth Year: {}".format(birth_year))
                else:

                    # Display no data in case "Birth Year" column don't exist
                    print("\n* Birth Year: No Data")
        else:

            # User don't want to see the raw data break loop
            break

        # add 5 in the index counter
        df_index_counter += 5

    print('-' * 40)


def main():
    print('-' * 40)
    print('Explore US bikeshare data statistics!')
    print('-' * 40)
    while True:
        try:
            print('\n\nFirst, provide your filter choices.')
            # Get data filter choices from user
            city, month, day = get_filters()

            # boolean for show or not show month data
            show_month_stat = month == 'none'

            # boolean for show or not show day of week data
            show_day_stat = day == 'none'

            # Load filtered dataframe
            df = load_data(city, month, day)

            # Show time stats
            st.time_stats(df, show_month_stat, show_day_stat, MONTHS_LIST,
                          DAYS_LIST)

            # Show station stats
            st.station_stats(df)

            # Show trip duration stats
            st.trip_duration_stats(df)

            # Show user duration stats
            st.user_stats(df)

            # Show raw output
            raw_data_display(df)

            # Take user input to restart the program or exit
            restart = input(
                '\nThanks for using this app! \n\nWould you like to restart? Enter yes or no.\n'
            )
            if restart.lower() != 'yes':
                break
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()