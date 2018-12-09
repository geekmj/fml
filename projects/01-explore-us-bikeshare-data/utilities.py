# Constants tuple for display time calculation
INTERVALS = (
    ('Weeks', 604800),  # 60 * 60 * 24 * 7
    ('Days', 86400),  # 60 * 60 * 24
    ('Hours', 3600),  # 60 * 60
    ('Minutes', 60),
    ('Seconds', 1),
)


def get_user_choice(choices, choice_type, default_value=""):
    """
    A common method to take user choice from a list of choices

    Args:
        (list) choices - list of choices
        (str) choice_type - Type of choice
        (boolean) default_value - Return default value in case wrong input
    Returns:
        (str) - User selected choice
    """

    print("\n\n{}\n".format(choice_type))

    # Display the choices to user
    for i in range(len(choices)):
        print("{}. {}".format(i + 1, choices[i].capitalize()))

    # User input for number for choice selection
    while True:
        try:

            # Input prompt for Choice
            choice = input("\nEnter your choice: ")

            # Convert input text in lowercase
            choice_lower = choice.lower()

            # Check if choice text match in list
            if choice_lower in choices:

                # Display corrected selection
                print("\nYou selected: {}".format(choice_lower.capitalize()))

                return choice_lower
            elif choice_lower.isdigit():
                # Check if user used number for selection

                # Check if number choice has value in list
                choice_value = choices[int(choice_lower) - 1]

                # Display corrected selection
                print("\nYou selected: {}".format(choice_value.capitalize()))

                return choice_value
            else:

                if len(default_value) > 0:

                    # Check for default value, if yes return that in wrong input event
                    return default_value
                else:
                    # Display input error message
                    print("\nPlease enter a valid choice (text or number).")

        except KeyboardInterrupt:

            # Keyboard Interrupt need to handled so program can exit properly
            print("Exiting..")

            # Make sure we are passing the exception to chain
            raise
        except:

            if len(default_value) > 0:

                # Check for default value, if yes return that in wrong input event
                return default_value
            else:
                print("\nPlease enter a valid choice (1,2,3,...) or text.")


def display_time(seconds, granularity=2):
    """
    A common method to take time in seconds and convert
    that into Week, Day, Hour, Minutes and Seconds.
    
    Args:
        (int) seconds - time value in seconds
        (str) granularity - granularity
   
    Returns:
        (str) - Formatted time in Week, Day, Hour, Minutes and Seconds
    """

    result = []

    for name, count in INTERVALS:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(int(value), name))
    return ', '.join(result[:granularity])