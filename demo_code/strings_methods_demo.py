def main():
    my_name = "louise"

 #capitilize a strin
    print(f"my name campitilized: {my_name.capitalize()}")
    #make a string uppercase
    print(f"my name uppercase: {my_name.upper()}")

    #make a string lower case
    last_nume = "SCHLOEGEL"
    print(f"My full name lowercase: {my_name.lower()} {last_nume.lower()}")

    #compare two strings
    my_name_title_case = "Louise"
    if my_name == my_name_title_case:
        print("the strings are equal")
    else:
        print("the strings are not equal")
        
    print("\nUsing the Startwith() Method\n-----------------")
    #determine if a string starts with a set of characters 
    print(f"{my_name.startswith("L") or my_name.startswith("l")}")

    if(not my_name.startswith("Lou") and (not my_name.startswith("lou"))):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    if(not my_name.lower().startswith("Lou")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    print("\nUsing the Endswith() Method\n-----------------")
    print(f"{my_name} ends with 'ise': {my_name.endswith('ise')}")


    print("\nUsing the findmethod() Method\n-----------------")
    #lets find the s is louise
    search_letter = "oui"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
        print(f"the '{search_letter}' is at index {index_of_substring} in {my_name}")
    else:
        print(f"there is no '{search_letter}' in {my_name}")

    print("\nLooping through a string\n---------------")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)}")

    # #print the letters in a string along with the index postitions
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")

    print("\nSearch a string\n---------------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #Write code that counts the number of occurences of the word dog in the sentence
    #expected output: 3

    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    while True:
        #start at the beginning of the string
        # search for the occurence of the word "dog" starting at index 0
        dog_index = sentence.find(search_word, start_index)

        # continue searching the string from the next index after the dog we just found
        if dog_index == -1:
            break
        else:
            #number_of_dogs = number_of_dogs + 1
            #if we find find dog, add one to some variable we use to keep track of the number of dogs we find
            number_of_dogs += 1
            
            # update the strating indx by one
            # search until we dont find anymore dogs: when find() returns: -1
            start_index = dog_index + 1
    print(f"There are {number_of_dogs} {search_word}(s) ins the sentence.")
       
    


main()