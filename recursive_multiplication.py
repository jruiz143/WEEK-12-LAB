#PROGRAMMING EXERCISE 12-2
#DESIGN A RECURSIVE FUNCTION THAT ACCEPTS TWO ARGUMENTS INTO THE PARAMETERS X AND Y
# THE FUNCTION SHOULD RETURN THE VALUE OF X TIMES Y. REMEMBER, MULTIPLICATION CAN BE PERFORMED AS
#REPEATED ADDITION AS FOLLOWS: 7 x 4 = 4+4+4+4+4+4+4
#TO KEEP THE FUNCTION SIMPLE, ASSUME X AND Y, WILL ALWAYS HOLD POSITIVE NONZERO INTEGERS

def main():
    #GET TWO NUMBERS
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print("Their product is", multiply(num1, num2))#DISPLAY

def multiply(x, y):
    #BASE CASE
    if x == 0 or y == 0:
        return 0
    else:#RECURSIVE CASE
        return x + multiply(x, y-1)

#CALL MAIN
main()