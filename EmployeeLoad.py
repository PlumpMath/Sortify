import os
from sys import argv

class Employee:
    def __init__(self, ID='', first_name='', last_name='', middle_name='', files=[]):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.files = []

    def rewrite(self, destination_path):
        '''rewrites self into destination'''
        for file in self.files:
            new_name = os.path.basename(file)
            final = os.path.join(destination_path, new_name)
            os.rename(file, final)

class ListEmployee:
    def __init__(self, full_path_to_txt, full_list=[]):
        '''Scans a given text file for employee name in ID-Lastname,Firstname format.'''

        self.full_path_to_txt = full_path_to_txt
        self.full_list = full_list

        #Load txt file
        text_list = open(full_path_to_txt, 'r')

        #Now populate data attribute with each line of the txt file.
        for number, line in enumerate(text_list):
            string = str(line)

            #Get rid of the pesky newlines
            string = string.rstrip()

            #Attempt to create employees from a proper naming convention
            string = string.replace('-', '|')
            string = string.replace(',', '|')

            #Now divie up the split names
            split = string.split('|')
            try:
                #initialize an employee instance
                employee = Employee(split[0], split[2], split[1])

                #Add employee instance to the list of employees.
                self.full_list.append(employee)

            except:
                IndexError
                print("***Improper naming convention on line ", number)
                pass

    def match(self, string_x, string_y):
        '''Just a simple string matcher for now, I'll probably extend it later.'''
        x = str(string_x)
        y = str(string_y)

        if (x in y) or (y in x):
            return x

    def search(self, text_process):
        '''Takes in text processor argument'''

        returnList = []

        for employee in self.full_list:
            arg = text_process.name

            if self.match(employee.ID, arg):
                employee.files.append(text_process.input_text)
                returnList.append(employee)

            elif (self.match(employee.last_name, arg)) and (self.match(employee.first_name, arg)):
                employee.files.append(text_process.input_text)
                returnList.append(employee)
            else:
                pass

        return returnList
