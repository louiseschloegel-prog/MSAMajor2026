def main():
# define the dictionary of all the food items 
    menu = {
    "Baja taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super burrito": 8.50,
    "Super quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla salad": 8.00}
    total = 0
    
# inside a while loop
    while True:
        #prompt the user for an input 
        user_order = input("Item:\n").capitalize()
        # this will contuine until user says end, END, End, enD, etc then the loop will break
        if user_order.lower() == "end":
           break


         #check to see if the input is present in dictionary
        if user_order in menu:
            # if correct then it will update total and print new total
            total = total + menu[user_order]
            print(f"Total: ${total: .2f}")
            continue
         #if incorrect then it will contuine and re-prompt the user
        

main()