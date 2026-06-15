#while loop
def main():
    while True:
        # INPUT
        # Prompt the user to enter an expression in the format: (X y Z) where x and z are int and y is the sign
        user_input = input("Enter an expression in (X Y Z) format: ")
        numbers_data = user_input.split(" ")
        # validate the expression format 
        # use the split method to split the xpression at the space
        # if the length of the resulting list is not 3 then: invaild format
        if len(numbers_data) != 3:
            print("ERROR: Incorrect format")
            continue
    
    # validate that x and z and integers
        #Convert to int.
        #if conversion causes an exception then: incorrect format
        X = numbers_data[0]
        Y = numbers_data[1]
        Z = numbers_data[2]

        try:
            X = int(X) 
            Z = int(Z)
        except:
            print("ERROR: please enter a number")

        if (Y != "+") and (Y != "-") and (Y != "/") and (Y != "*"):
            print("ERROR: incorrect format")
            continue

        elif Y == '/' and Z == 0:
            print("ERROR: divide by 0 error")
            continue

        elif Y == "+":
           answer = X + Z
           print(f"Answer: {answer}")

        elif Y == "/":
            answer = X / Z
            print(f"Answer: {answer}")

        elif Y == "-":
            answer = X - Z
            print(f"Answer: {answer}")

        elif Y == "*":
            answer = X * Z
            print(f"Answer: {answer}")
        
        reask_input = input("Do you want to evaluate another expression? (Press y to continue): ")

        if reask_input == 'y':
            continue
        else:
            break




       

    



        
        
            

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