#!/usr/local/bin/python3

import TextProcessor
import FolderManager
import EmployeeLoad
import os

#Create a new instance of an employee load for this file
e = EmployeeLoad.ListEmployee('/Users/mikahl/Dev/Test/employee_list.txt')

#Scan a folder of imported pdfs to categorize
src_folder = FolderManager.RootDirectory('/Users/mikahl/Dev/imported_pdfs/', search_results=[])
extension = '.pdf'
src_folder.recursive_search(extension, path=None)

#Copy over these search results in case I want to make another search later.
unprocessed_pdfs = src_folder.search_results[:]

# print(unprocessed_pdfs)
#Now we're going to examine the pdf filenames for any resembelence to our list of
#employees

#Now create a list to add the processed text to.
processed_files = []

for pdf in unprocessed_pdfs:
    raw_pdf = str(pdf)
    raw_pdf = TextProcessor.TextProcess(raw_pdf, extension=None, name=None)
    processed_files.append(raw_pdf)
    #print(raw_pdf.input_text)

#loop through each employee thing, compare it too the employee list to see
#if there's a match.  If there there's a match, append to found_list

filtered_list = []

#Compare the filenames to listed employee names, and add which ones overlap.
for text in processed_files:
    sub_list = e.search(text)
    filtered_list += sub_list

print("Found a total of {0} employees".format(len(filtered_list)))

#Establish a destination folder
dest = os.path.join('/Users/mikahl/Dev/Test/Dest')

if os.path.exists(dest):
    pass
else:
    os.mkdir(dest)

#Print off employee names to be sure.
for i in filtered_list:
    print(i.last_name)
    dir_name = '{0}-{1},{2}'.format(i.ID, i.last_name, i.first_name)

    #Check to see if directory already exists
    employee_dir = os.path.join(dest, dir_name)
    if os.path.exists(employee_dir):
        i.rewrite(employee_dir)
    else:
        os.mkdir(employee_dir)
        i.rewrite(employee_dir)
