#12-1 PROGRAMMING EXERCISE
#DESIGN A RECURSIVE FUNCTION THAT ACCEPTS AN INTEGER ARGUMENT, N, AND PRINTS THE NUMBER
#1 UP THROUGH N

def main():
    #GET USER INPUT
    n = int(input("ENTER A NUMBER: "))
    print(f"NUMBERS 1 to {n}:")
    print_numbers(n)

def print_numbers(n):
    #BASE CASE
    if n == 1: #IF N IS 1, PRINT 1
        print(1)
    #RECURSIVE CASE
    else:
        print_numbers(n - 1)  # CALL FUNCTION 
        print(n)  # DISPLAY NUMBER AFTER RECURSIVE CALL

#CALL MAIN
if __name__ == "__main__":
    main()