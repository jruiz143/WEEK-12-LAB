#12-5 RECURSIVE LIST SUM

#DESIGN A FUNCTION THAT ACCEPTS A LIST OF NUMBERS AS AN ARGUMENT
#THE FUNCTION SHOULD RECURSIVELY CALCULATE THE SUM OF ALL THE NUMBERS
#IN THE LIST AND RETURN THAT VALUE

#CREATE A LIST OF NUMBERS
def main():
    numbers = [2, 4, 6, 8]
    my_sum = sum_list(numbers) #CALL RECURSIVE FUNCTION
    print("THE SUM OF THE LIST IS",my_sum) #DISPLAY RESULT

def sum_list(num_list):
    if not num_list:#IF LIST IS EMPTY, RETURN 0
        return 0
    return num_list[0] + sum_list(num_list[1:]) #SUM THE FIRST NUMBER AND THE SUM OF THE REST

# CALL MAIN
main()

    
