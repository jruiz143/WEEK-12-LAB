#12-4 LARGEST LIST ITEM

#DESIGN A FUNCTION THAT ACCEPTS A LIST AS AN ARGUMENT AND RETURNS THE LARGEST
#VALUE IN THE LIST. THE FUNCTION SHOULD USE RECURSION TO FIND THE LARGEST ITEM

def main():
    numbers = [8, 3, 2, 6] #CREATE LIST OF NUMBERS
    print(f"LIST:{numbers}")
    largest = find_largest(numbers)#CALL RECURSIVE FUNCTION
    print("THE LARGEST VALUE IS", largest) #DISPLAY RESULT

def find_largest(n):#n = list
    # VASE CASE
    if len(n) == 1:#IF IT ONLY HAS ONE ELEMENT, RETURN
        return n[0]
    # RECURSIVE CASE
    else:
        largest_number = find_largest(n[1:])
        if n[0] > largest_number:
            return n[0]
        else:
            return largest_number

# CALL MAIN
if __name__ == "__main__":
    main()
