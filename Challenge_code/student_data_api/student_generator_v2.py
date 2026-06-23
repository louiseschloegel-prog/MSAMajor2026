from Student import Student

"""
Function to retun a list of student objects 
Input: none
Output: llist of student objects
"""
def load_students() -> list[Student]:
    #open students.csv in read mode 
   
    data_file = open("students.csv", "r")



    #create an empty list
   
    #use a for loop to read all the data starting at the seccond line then going line by line
    line_number = 0
    student_data = []
    for line_of_data in (data_file):
        line_number = line_number + 1
        if line_number == 1:
            continue

        #split items at comma
        student_info = line_of_data.split(",")
        # handle errors in data format. line_of_data should have 6 items
        # if error in format then write to a log file
        try:
            if len(student_info) != 6:
                raise Exception(f"Error on line {line_number} of the file. Data has {len(student_info)} items but should have 6.\n")
        except Exception as error:
            continue

        # get student data
       
        First_name = student_info[0]
        last_name = student_info[1]
        major = student_info[2]
        
        student_ID = student_info[5].strip()
        try:
            gpa = float(student_info[4])
            credits = int(student_info[3])
        except:
            print(f"Error on line {line_of_data} of this file")
            continue
        
        student = Student(First_name, last_name, major, credits, gpa, student_ID)
        student_data.append(student)

        
    data_file.close()
    

    #print the data
    return student_data


"""
Function to convert student objects into studnet dictionaries
Input: list of student objects
Output: list of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    # create an empty list to store the dictionaries
    student_dictionary_list = []

    # loop through the list of students and write each students data to a dictionary
    for student in list_of_students:
        #create am empty dictionary
        student_dictionary = {}

        #make entries into the dictionary using the student properties

        # firstname, lastname, major, gpa, class, id
        student_dictionary['first_name'] = student.get_First_name()
        student_dictionary['last_name'] = student.get_Last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_GPA()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_ID_number()

        #append the dictionary to the list of dictionaries 
        student_dictionary_list.append(student_dictionary)
    
    # return the list of dictionaries
    return student_dictionary_list

"""
Function to get student dictionaries
Input: none
Output: a list of student dictionaries
"""
def get_student_dictionaries():
    # get a list of students
    student_data = load_students()

    # get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_data)
    return student_dictionaries
   