from Student import Student

def main():
    #open students.csv in read mode 
    data_file = open("students.csv", "r")



    #create an empty list
    student_info = []
    #use a for loop to read all the data starting at the seccond line then going line by line
    for line_of_data in range(1 + data_file):
        Student_major_credits_gpa_ID = line_of_data.split(",")
        print(Student_major_credits_gpa_ID)
    #split items at comma

    #print the data
main()