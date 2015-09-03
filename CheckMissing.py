#!/usr/local/bin/python3
import os
import sys
import PatternMatch
import FolderManager

def check_missing(employeeTxt, folder, extension='.pdf', delimiters=['-', ',',' '], threshold=2):

    #First, establish source files
    #Scan a folder of imported pdfs to categorize

    #Load each employee as a pattern from each line of text file.
    employee_list = PatternMatch.TextRead(employeeTxt)

    #Now examine files with a FolderManager instance.
    src_folder = FolderManager.RootDirectory(folder, folder)

    #Search for all available PDFs
    src_folder.recursive_search(extension, path=None)

    #Make a list of found, and not found folders
    found = []
    not_found = []

    for name in employee_list.patterns:
        #go through each pattern,and then compare that to the name of each source folder.

        for every_folder in src_folder.dirs:
            if str(every_folder) in name.text:
                print("Found matching folder ", every_folder)
                found.append(name.text)
            else:
                not_found.append(name.text)

    #Because the last iteration creates doubles, I'll just turn the list into a set to get the unique ones
    not_found = set(not_found)
    found = set(found)

    missing_folders = not_found.difference(found)

    for missing in missing_folders:
        print("No match found for ", missing)

    print("A total of %d are missing" % len(missing_folders))


check_missing("F:\\Payroll\\EmployeeData\\active_employees.txt", "F:\\Payroll\\")


##def description():
##    '''Just describes procedure of script if invoked improperly.'''
##    print("\nThis script needs arguments\n")
##    print("Example usage: ")
##    print("EmployeeSorter /dir/text_file.txt [extension] [file-type] [delimiters] [threshold]")
##    print("\n")
##
##
##if __name__ == '__main__':
##
##    length = len(sys.argv)
##
##    #If there's no args at all
##    if length == 1:
##        description()
##
##    #This clause works with something like Python SortByEmployee somefile.txt /made-up-dir/
##    elif length == 3:
##
##        #Get all relevant arguments
##        txt_file = sys.argv[1]
##        source = os.getcwd()
##        destination = os.path.join(source, sys.argv[2])
##
##        #check to make sure txt file exists
##        if os.path.exists(txt_file):
##            print("Txt file found")
##
##        elif os.path.exists(txt_file) == False:
##            print("\n**Missing text file, this won't continue")
##            sys.exit()
##
##        try:
##            os.mkdir(destination)
##            print("created output directory ", destination)
##        except:
##            pass
##
##        #Now invoke the actual sorting function
##        employee_sorter(txt_file, source, destination)
##
##    else:
##        description()
