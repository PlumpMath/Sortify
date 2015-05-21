#!/usr/local/bin/python3
import os
import PatternMatch
import FolderManager

#First, establish source files
#Scan a folder of imported pdfs to categorize
source = '/Users/mikahl/Dev/imported_pdfs/'
destination = '/Users/mikahl/Dev/Write'
employeeTxt = '/Users/mikahl/Dev/Test/employee_list.txt'
extension = '.pdf'
delimiters = ['-', ',',' ']
threshold = 0

#Load each employee as a pattern from each line of text file.
employee_list = PatternMatch.TextRead(employeeTxt, delimiters=delimiters)

#Now examine files with a FolderManager instance.
src_folder = FolderManager.RootDirectory(source, destination)

#Search for all available PDFs
src_folder.recursive_search(extension, path=None)

for file in src_folder.files:
    #Create a pattern object('query') based on the filenames in source directroy.
    query = str(file.file_name)
    query = PatternMatch.Pattern(query)

    #Breaks up name into meaningful chunks to match with.
    query.chunkify(delimiters)

    #Create a variable for a potential match in chunks between file names and
    #the input text file.
    name_match = employee_list.lookup(query, threshold)

    #As soon as the variable contains matches, that means we have a hit, and
    #now begin to move files over to their own directory.
    if name_match:
        print("*** match {0} to {1} *** ".format(name_match, query.chunks))
        #Create a new name for the file, based on the convention
        new_name = name_match

        #Create new directory for employee, then move its file there.
        src_folder.create_dir(new_name)

        #Rename file itself to match directory, and number it if there's more
        #than one.
        file.new_file_name = new_name
        print(file.new_file_name)

        #Finally move the file to the new path.
        file.destination_path = os.path.join(src_folder.dest_path, file.new_file_name)
        print(file.destination_path)
        file.move()
    else:
        pass
