#while loop
def main():
    while True:
        # INPUT
        # Prompt the user to enter an expression in the format: (X y Z) where x and z are int and y is the sign
        user_input = print(input("Enter an expression in (X y Z) format: "))
        user_numbers = user_input.split(" ")
        # validate the expression format 
        # use the split method to split the xpression at the space
        # if the length of the resulting list is not 3 then: invaild format
        if len(user_input) != 3:
            print("ERROR: Incorrect format")
            continue
    # validate that x and z and integers
        #Convert to int.
        #if conversion causes an exception then: incorrect format
        X = user_numbers[0]
        y = user_numbers[1]
        Z = user_numbers[3]

    # validate that y is an acceptale operator (+, -, /, *)
        # use an if statement to determine if y == +,-,/,*
        # invaild Fomrat is not

    # Validate that when Y is / Z is not 0
        #if y = / and z = 0 then print divide by zero error
    # Do the math
        #

    #OUTPUT
    #Print the output to the user

main()