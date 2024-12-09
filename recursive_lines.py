#12-3 PROGRAMMING EXERCISE

#WRITE A RECURSIVE FUNCTION THAT ACCEPTS AN INTEGER ARGUMENT, N. THE FUNCTION SHOULD 
#DISPLAY N LINES OF ASTERISKS ON THE SCREEN, WITH THE FIRST LINE SHOWING 1 ASTERIK
#THE SECOND LINE SHOWING 2 ASTERISKS, UP TO THE NTH LINE WHICH SHOWS N ASTERISKS.

def display_asterisks(n):
    if n == 0:
        return
    display_asterisks(n - 1)  # RECURSIVE CASE
    print('*' * n)  # DISPLAY ASTERISKS

def main():
    display_asterisks(8)  # DISPLAY 8 LINES

# RUN MAIN
if __name__ == "__main__":
    main()

