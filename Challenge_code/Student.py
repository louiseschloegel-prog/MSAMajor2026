class Student():
    def __init__(self, first_name:str, last_name:str, major:str, credit_horus:float, GPA:float, ID_number:float):

        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_horus
        self.__GPA = GPA
        self.__ID_number = ID_number

    def get_First_name(self):
        return self.__first_name
    def set_First_name(self, new_first_name:str):
        self.__first_name = new_first_name
        return
    
    def get_Last_name(self):
        return self.__last_name
    
    def set_Last_name(self, new_last_name:str):
        self.__last_name = new_last_name
        return

    
    def get_major(self):
        return self.__major
    def set_major(self, new_major:str):
        self.__major = new_major
        return

    def get_credit_hours(self):
        return self.__credit_hours
    def set_credit_hours(self, new_credit_hours:float):
        self.__credit_hours = new_credit_hours
        return
    
    def get_GPA(self):
        return self.__GPA
    def set_GPA(self, new_GPA):
        self.__GPA = new_GPA
        return
    
    def get_ID_number(self):
        return self.__ID_number
    

    def get_class_level(self):
        if self.__credit_hours <= 30:
            return "Freshman"
        if self.__credit_hours <= 60:
            return "Sophmore"
        if self.__credit_hours <= 90:
            return "Junior"
        if self.__credit_hours >= 90:
            return "Senior"
    
    def update_credit_hours(self, aditional_hours):
        self.__credit_hours += aditional_hours





    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__GPA}, ID: {self.__ID_number}")



    
        

    