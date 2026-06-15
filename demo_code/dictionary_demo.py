def main():
    #the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    #print the names of the students with their scores
    print("Students and scores using the lists\n-----------------------")
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")

    #create a dictionary of names and scores
    students_scores = {
        "Alice": 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91
     }
    #print bob and james scores
    print("\nPrint Bob and Jane's Scores\n-----------------")
    print(students_scores["Bob"])
    print(students_scores["Jane"])
    #print all the data in the student scores dictionary
    print("\nPrint all students data\n------------------")
    for student in students_scores:
        print(f"{student}: {students_scores[student]}")
          
          
main()