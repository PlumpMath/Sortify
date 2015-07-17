#!/usr/local/bin/python3
import os
import sys
import PatternMatch
import FolderManager

def employee_sorter(source, destination, employeeTxtDir, extension='.pdf', delimiters=[], threshold=2):
    #First, establish source files
    #Scan a folder of imported pdfs to categorize

    #Now examine files with a FolderManager instance.
    src_folder = FolderManager.RootDirectory(source, destination)

    #Search for all available PDFs
    src_folder.recursive_search(extension, path=None)

    #Create an instance of TextReadDir on all text file names for a directory
    employee_list = PatternMatch.TextReadDir(employeeTxtDir, delimiters=delimiters)

    #Now loop through to create subdirectories based on all the text files.
    text_file_list = employee_list.get_text_file_names()

    for text_files in text_file_list:
        folder = str(text_files)
        folder_name = os.path.join(destination, folder)
        src_folder.create_dir(folder_name)


        #Create a pattern object('query') based on the filenames in source directroy.
        for file in src_folder.files:
            query = str(file.file_name)
            query = PatternMatch.Pattern(query)

            #Breaks up name into meaningful chunks to match with.
            query.chunkify(delimiters)

            #Create a variable for a potential match in chunks between file names and
            #the input text file.
            name_match = employee_list.lookup_pattern(query, threshold)

            #As soon as the variable contains matches, that means we have a hit, and
            #now begin to move files over to their own directory.
            if name_match:
                #Create a new name for the file, based on the convention
                new_name = name_match

                #Rename file itself to match directory, and number it if there's more
                #than one.
                file.new_file_name = new_name

                #Define and create destination path
                file.destination_path = os.path.join(folder_name, file.new_file_name)
                os.mkdir(file.destination_path)

                print("Destination: ", file.destination_path)
                print("New file name: ", file.new_file_name)
                file.move()

            #If no matching pattern is found, put in an unknown folder.
            else:
                unknown_folder = os.path.join(src_folder.dest_path, file.file_name)

                if os.path.exists(unknown_folder):
                    pass
                else:
                    os.mkdir(unknown_folder)

                file.destination_path = unknown_folder
                file.new_file_name = file.file_name

                #Finally move the file over.
                file.move()

def description():
    '''Just describes procedure of script if invoked improperly.'''
    print("\nThis script needs arguments\n")
    print("Example usage: ")
    print("EmployeeSorter /dir/text_file.txt [extension] [file-type] [delimiters] [threshold]")
    print("\n")


if __name__ == '__main__':

    length = len(sys.argv)

    #If there's no args at all
    if length == 1:
        description()

    #This clause works with something like Python SortByEmployee somefile.txt /made-up-dir/
    elif length == 3:

        #Get all relevant arguments
        txt_file_dir = sys.argv[1]
        source = os.getcwd()
        destination = os.path.join(source, sys.argv[2])

        #check to make sure txt file exists
        if os.path.exists(txt_file_dir):
            print("Txt file directory found")

        elif os.path.exists(txt_file_dir) == False:
            print("\n**Missing text file directory, this won't continue")
            sys.exit()

        try:
            os.mkdir(destination)
            print("created output directory ", destination)
        except:
            pass

        employee_sorter(source, destination, txt_file_dir, delimiters=['-', ',',' '])

    else:
        description()
