#12-6 PROGRAMMING EXERCISE
#Design a function that accepts an integer argument and returns the sum
# of all integers from 1 up to the number passed as an argument. For example, if 50
#is passed as an argument, the function will return the sum of 1,2,3,4...
#Use recursion to calculate the total

#THE SUM OF INTEGER FUNCTION USES RECURSION TO CALC THE SUM OF ITS ARGUMENT
def sum_of_integers(num):
    #BASE CASE
    if num == 1:
        return 1
    # RECURSIVE CASE
    else:
        return num + sum_of_integers(num - 1) #ADDS THE NUM (ARGUMENT) TO THE SUM OF INTEGERS

# Example usage
result = sum_of_integers(50)
print(result)
