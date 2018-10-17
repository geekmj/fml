names =  input("Enter names seperated by commans: ").split(",")# get and process input for a list of names
assignments = input("Enter assignments counts seperated by commans: ").split(",") # get and process input for a list of the number of assignments
grades =  input("Enter grades counts seperated by commans: ").split(",")# get and process input for a list of grades
# message string to be used for each student
# HINT: use .format() with this string in your for loop

for name, assignment, grade in zip(names, assignments, grades):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n".format(name, assignment, grade, int(grade) + int(assignment)*2)
    print(message)

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message