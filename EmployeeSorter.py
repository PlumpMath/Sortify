#!/usr/local/bin/python3
import os
import sys
import PatternMatch
import FolderManager

def employee_sorter(source, destination, *employeeTxt, extension='.pdf', delimiters=['-', ',',' '], threshold=2):
    #First, establish source files
    #Scan a folder of imported pdfs to categorize

    #Now examine files with a FolderManager instance.
    src_folder = FolderManager.RootDirectory(source, destination)

    #Search for all available PDFs
    src_folder.recursive_search(extension, path=None)

    for text_files in employeeTxt:

    #     file_lookup(text_files)
    #
    #     #If not already there, create a subdir based on which text file
    #     #the match is based on.
    #     folder_name = os.path.join(text_file_name, name_match)
    #
    #     src_folder.create_dir(folder_name)
    #
    #     #Create a new name for the file, based on the convention
    #     new_name = name_match
    #
    #     #Rename file itself to match directory, and number it if there's more
    #     #than one.
    #     file.new_file_name = new_name
    #
    #     #Finally move the file to the new path.
    #     file.destination_path = os.path.join(src_folder.dest_path, file.new_file_name)
    #     file.move()
    #
    # #If no matching pattern is found, put in an unknown folder.
    # else:
    #     unknown_folder = (os.path.join(src_folder.dest_path, file.file_name))
    #
    #     if os.path.exists(unknown_folder):
    #         pass
    #     else:
    #         os.mkdir(unknown_folder)
    #
    #     file.destination_path = unknown_folder
    #     file.new_file_name = file.file_name
    #
    #     #Finally move the file over.
    #     file.move()


def file_lookup(text_file):
    '''Loops through a given list of files and determines if there's a pattern in one of them.'''
        #Iterate through all instances of employees txt files
        # for file in src_folder.files:
        #     #Get the name of the text file, and use it to create a subdir based
        #     #on those names.
        #     raw_parent_name = str(employeeTxt)
        #     raw_parent_name = raw_parent_name.split('.')
        #
        #     #Create subdir based on text files's name
        #     text_file_name = raw_parent_name[0]
        #
        #     #Load each employee as a pattern from each line of text file.
        #     employee_list = PatternMatch.TextRead(text_files, delimiters=delimiters)
        #
        #     #Create a pattern object('query') based on the filenames in source directroy.
        #     query = str(file.file_name)
        #     query = PatternMatch.Pattern(query)
        #
        #     #Breaks up name into meaningful chunks to match with.
        #     query.chunkify(delimiters)
        #
        #     #Create a variable for a potential match in chunks between file names and
        #     #the input text file.
        #     name_match = employee_list.lookup(query, threshold)
        #
        #     #As soon as the variable contains matches, that means we have a hit, and
        #     #now begin to move files over to their own directory.
        #     if name_match:
        #         return file
        #
        #     else:
        #         pass

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
        txt_file = sys.argv[1]
        source = os.getcwd()
        destination = os.path.join(source, sys.argv[2])

        #check to make sure txt file exists
        if os.path.exists(txt_file):
            print("Txt file found")

        elif os.path.exists(txt_file) == False:
            print("\n**Missing text file, this won't continue")
            sys.exit()

        try:
            os.mkdir(destination)
            print("created output directory ", destination)
        except:
            pass

        #Now invoke the actual sorting function
        employee_sorter(txt_file, source, destination)

    else:
        description()
