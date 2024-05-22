# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment this assignment focusing on using functions and classes to organize code
# Change Log: (Who, When, What)
#   Minghsuan Liu,5/20/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json
from io import TextIOWrapper
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
Please Select:'''

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants

#json_data: str ='' 
file: TextIOWrapper = None  
info_data: list = [] 

''' since both "read file" and "write data to file" all needs to
    open file, tried to combine them to only have one class
    named "handle_file" method. Then they share the same try/except
    error handling.
'''

class FileProcessor:
    @staticmethod
    def handle_file(file_name: str, execute_mode: str, json_data: list):
        try: 
            file= open(file_name,execute_mode)
            
            if execute_mode == 'r':
                try:
                    json_data = json.load(file)
                    if not json_data:
                        raise Exception("No Content in the file")
                except Exception as e:
                    print("Please add initial content in the file")
            elif execute_mode == 'w':
                json.dump(json_data,file,indent=2)
                print("Your Info is registered in the system\n")
                
            file.close()

        except FileNotFoundError as e:
            IO.output_error_message("File doesn't exist!",e)
            IO.output_error_message("Try to create a file")
        except json.JSONDecodeError as e:
            IO.output_error_message("JSON data in file isn\'t valide",e)
            IO.output_error_message("Resetting JSON file")
        except Exception as e:
            IO.output_error_message("There was an error open the document",e)
            IO.output_error_message("Unhandled exception")
        return json_data




class IO:
    '''
    methods
    1. output_error_message: handle File Processor
    2. menu_option: display menu and get input (needs to be 1~4 range)
    3. input_data: ask for first/last/course name and append to original data structure
    4. print data: print out existed and new add data
    '''
    
    @staticmethod
    def output_error_message(message: str, exception: Exception = None):
        print(message)
        if exception is not None:
            print(exception,exception.__doc__,type(exception),sep='\n')
    
    @staticmethod
    def user_choice(menu: str):
        menu_choice = input(menu)
        print(menu_choice)
        while menu_choice not in ["1","2","3","4"]:
            IO.output_error_message("Please enter between 1~4")
            menu_choice = input(menu)
            
        return menu_choice
        
    @staticmethod
    def input_data(info_data: list):
        first_name: str = '' 
        last_name: str = ''  
        course_name: str = ''  
        while True:
            try:
                
                first_name = input("Please Enter Student's First Name: ")
                last_name = input("Please Enter Student's Last Name: ")
                
                if not first_name.isalpha() or not last_name.isalpha():
                    raise ValueError("Name can only have alphabetic characters!")
                course_name = input("Please Enter Course Name: ")
                student_data={"FirstName":first_name,"LastName":last_name,"CourseName":course_name}
                info_data.append(student_data)
                return info_data
                input("Press \"Enter\" to continue...")
                break
            except ValueError as e:
                IO.output_error_message("User Entered invalid information! ")
    
    @staticmethod
    def print_data(info_data: list):
        for line in info_data:
            print(f'{line["FirstName"]} {line["LastName"]} is registered for course {line["CourseName"]}\n')
        
        input("Press \"Enter\" to continue...")



# Main body of the program
    
info_data = FileProcessor.handle_file(FILE_NAME,'r',info_data)

while info_data:
    menu_choice = IO.user_choice(MENU)
    if menu_choice =="1":
        IO.input_data(info_data)
    elif menu_choice == "2":
        IO.print_data(info_data)
    elif menu_choice == "3":
        FileProcessor.handle_file(FILE_NAME, 'w', info_data)
    elif menu_choice == "4":
        break


