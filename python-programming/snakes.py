how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""

print(snake_string * how_many_snakes)

# Common Method To Display Year On Year Growth Line Chart for various columns
# like budget, revenue, gross_profit etc.


def year_on_year_line_chart(df, what_trend):

    # Figure size and dpi
    plt.figure(figsize=(15, 7), dpi=150)

    # Defining tick labels
    plt_xtick_labels = range(1960, 2020, 5)

    # Setting tick labels
    plt.xticks(
        np.arange(0,
                  len(df.values) + 1, 5), plt_xtick_labels, rotation=45)

    # Setting Plot title
    plt.title('Yearwise {} Trends'.format(what_trend))
    # Setting X axis label
    plt.xlabel('Release Year')

    # Setting Y axis label, value is coming as parameter
    plt.ylabel(what_trend)

    # Generate plot with values
    plt.plot(
        df.values, 'r-', label=what_trend)
    plt.legend()
