# function to load data fram a file and return a dictionary
#input: filename: string
#output: dictionary
def load_menu_items(filename:str) -> dict:
     #open menu.txt: create a file handler to open file in read mode
    data_file = open(filename, "r")
    # create an empty dictionary
    menu_items = {}
    #use a loop to read the content of the file line by line
    for line_of_data in data_file:
        #split the line at the comma
        item_name_and_price = line_of_data.split(",")
        #get the item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price

       
    #close the file
    data_file.close()

    # return the dictionary of menu items 
    return menu_items






def main():
    menu_items = load_menu_items("menu.txt")
# define the dictionary of all the food items 
    menu = load_menu_items("menu.txt")
    total = 0
    
# inside a while loop
    while True:
        #prompt the user for an input 
        user_order = input("Item:\n").title()
        # this will contuine until user says end, END, End, enD, etc then the loop will break
        if user_order.lower() == "end":
           break


        #check to see if the input is present in dictionary
        if user_order not in menu.keys():
            continue
            # if correct then it will update total and print new total
        total = total + menu[user_order]
        print(f"Total: ${total: .2f}")
        #if incorrect then it will contuine and re-prompt the user
        

main()