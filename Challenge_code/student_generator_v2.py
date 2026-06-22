from Student import Student

def main():
    #open students.csv in read mode 
   
    data_file = open("students.csv", "r")



    #create an empty list
    
    #use a for loop to read all the data starting at the seccond line then going line by line
    line_number = 0
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
        credits = int(student_info[3])
        try:
            gpa = float(student_info[4])
            student_ID = student_info[5]
        except:
            print(f"Error on line {line_of_data} of this file")
            continue
        student_ID = student_info[5].strip()
        
  



        # create a student object
    
    
        student_data = []
        student = Student(First_name, last_name, major, credits, gpa, student_ID)
        student_data.append(student)

        for student in student_data:
            student.print_student_data()
        
    data_file.close
    



    
    
    #print the data
main()