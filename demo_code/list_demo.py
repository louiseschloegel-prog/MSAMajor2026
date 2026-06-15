def main():
    # create a list of stirngs, intergers, and differeing values
    names = ["John", "Mary", "Alice", "Bob"]
    list_of_intergers = [10, 16, 24, 42, 14, 9]
    random_type_lisst = ["Cyd", 15, 22.3, True, "Frank"]
    empty_list = []

    #print a list
    print(list_of_intergers)

    #add vaules to a list
    print("\nAdding Vaules to a List\n-----------------")
    names.append("Johnny")
    list_of_intergers.append(63)
    list_of_intergers.append(5)
    # list_of_intergers += [77]
    print(f"List of Integers: {list_of_intergers}")
    print(f"List of Names: {names}")

    print("\nGet the nember of items in a list\n------------")
    print(f"Items om Interger list: {len(list_of_intergers)}")
    print(f"Items of Names List: {len(names)}")
    print(f"Items in Empty List: {len(empty_list)}")


    print("\nGet values at specific idices in a list\n--------------")
    print(f"First Item in names list: {names[0]}")
    print(f"Fourht Item in names list: {names[3]}")

    # Print all items in a list 
    print("\nPrinting all names\n---------------")
    for name in names:
        print(name)


    print("\nPrinting all names with idex values\n---------------")
    for index in range(len(names)):
        print(f"names [{index}] -> {names[index]}")


    #calculate the sum of all values in a list
    sum_of_all_integers = 0
    for number in list_of_intergers:
        #sum_of_all_integers = sum_of_all_integers + number
        sum_of_all_integers += number
    print(f"Sum of all integers: {sum_of_all_integers}")

    #Calculate the average of all integers in  list
    avg_of_all_integers = sum_of_all_integers / len(list_of_intergers)
    print(f"Average of all integers: {avg_of_all_integers:.2f}")

    #Does the list contain a specific item
    search_name = "Alice"
    if search_name not in names:
        print(f"{search_name} is not in the list.")
    else:
        print(f"{search_name} is in the list.")


    #find the largest value in a list
    #set max value to the value of the first item in the list
    max_value = list_of_intergers[0]
    #loop of the entire list
    for current_value in list_of_intergers:
        #if current value > max_value then set max_value to current)value
        if current_value < max_value:
            max_value = current_value
            
    # after the loop is done, print the largest value
    print(f"\nList of integers: {list_of_intergers}")
    print(f"Smallest value in the list of integers: {max_value}")

main ()

