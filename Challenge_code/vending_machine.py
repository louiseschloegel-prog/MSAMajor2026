# Display the amount due
# Prompt the user to enter a coin, coins are (1, 5, 10, 25)
# Program should ignore any input that is not a valid input and re prompt the user to input a coin

def main():
    amount_due = 50
    nickel: 5
    dime: 10
    quarter = 25
    penny = 1
    print("Vending Machine\n -----------")
    while (True):
        print(f"Amount due: {amount_due}")
        try:
            input_coins = int(input("\nInsert Coin: "))
        except:
            continue
        input_coins = int(input("\nInsert Coin: "))
        if input_coins == 1 or input_coins == 5 or input_coins == 10 or input_coins == 25:
            amount_due = amount_due - input_coins

            if amount_due <= 0:
                break
        else:
            
            continue

    print(f"\nAmount due: 0\nChange owed: {amount_due * -1}")


main()
# in a function that is called 
#set the amount due to 50 and set how much all the coins will be eqaul to nickle: 5 dime: 10 quarter: 25 penny: 1
# use while loop
# first prompt the user to enter a coin
#validate the coin using if than statement
# if vaild it should then repeat the loop with the updated amount of coins due 

#if the number is vaild then subtract coin amount from the amount due
#if not vaild it should loop and go back to the top of the loop (countine)

# Once the user has inserted enough coins that is is <= 0 then loop should end
# then take the over due amount and display that as the change









# Process the input and display the updated amount due
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed
# End program
