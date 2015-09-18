#!/usr/local/bin/python3
import os
import sys
import PatternMatch as p
import FolderManager

threshold = 2
employee_delimiter = [
    'Scan from scanner',
    '2015',
    '001_Batch_April19 - uploaded',
     '002_Batch_April21 - uploaded',
     '003_Batch_April22 - uploaded',
     '004_Batch_April23 - uploaded',
     '005_Batch_April25 - uploaded',
     '006_Batch_April26 - uploaded',
     '007_Batch_May02 - uploaded',
     '008_Batch_May03 - uploaded',
     '009_Batch_May06 - uploaded',
     '010_Batch_May07 - uploaded',
     '011_Batch_May08 - uploaded',
     '012_Batch_May11 - uploaded',
     '013_Batch_May12 - uploaded',
     '014_Batch_May13 - uploaded',
     '015_Batch_May20 - uploaded',
     '016_Batch_May22 - uploaded', '017_Batch_May25 - uploaded',
     '018_Batch_May26 - uploaded', '019_Batch_May27 - uploaded',
     '020_Batch_May28 - uploaded', '021_Batch_May29 - uploaded',
     '022_Batch_June01 - uploaded', '023_Batch_June02 - uploaded',
     '024_Batch_June04 - uploaded', '025_Batch_June05 - uploaded',
     '026_Batch_June06 - uploaded', '027_Batch_June07 - uploaded',
     '028_Batch_June08 - uploaded', '029_Batch_June09 - uploaded',
     '030_Batch_June10 - uploaded', '031_Batch_June11 - uploaded',
     '032_Batch_June12 - uploaded', '033_Batch_June14 - uploaded',
     '034_Batch_June15 - uploaded', '035_Batch_June16 - uploaded',
     '036_Batch_June17 - uploaded', '037_Batch_June18 - uploaded',
     '038_Batch_June19 - uploaded', '039_Batch_June21 - uploaded',
     '040_Batch_June22 - uploaded', '041_Batch_June23 - uploaded',
     '042_Batch_June24 - uploaded', '043_Batch_June25 - uploaded',
     '044_Batch_June26 - uploaded', '045_Batch_June28_29 - uploaded',
     '046_Batch_June30 - uploaded', '047_Batch_July2 - uploaded',
     '048_Batch_July3 - uploaded', '049_Batch_July5 - uploaded',
     '050_Batch_July6 - uploaded', '051_Batch_July7 - uploaded',
     '052_Batch_July8 - uploaded', '053_Batch_July9 - uploaded',
     '054_Batch_July10 - uploaded', '055_Batch_July11 - uploaded',
     '056_Batch_July12 - uploaded', '057_Batch_July28 - uploaded',
     '058_Batch_July29 - uploaded', '059_Batch_Aug01 - uploaded',
     '060_Batch_Aug02 - uploaded', '061_Batch_Aug08 - uploaded',
     '062_Batch_Aug24 - uploaded', '063_Batch_Aug30 - uploaded',
     '064_Batch_Sept06 - uploaded', '15001-Ayotte,Weldon - uploaded',
     'EmployeeData',
     'Progress',
    '(',
    ')',
    '-',
    ',',
    ' ',]
def check_missing(employeeTxt, folder_text, delimiters=employee_delimiter, threshold=2):
    #Load each employee as a pattern from each line of text file.
    employee_list = p.TextRead(employeeTxt, delimiters=employee_delimiter)
    folder_listing = p.TextRead(folder_text, delimiters=employee_delimiter)

    [employee_list.lookup(f, threshold, keep_match=False) for f in folder_listing.patterns]

    return employee_list.patterns
        
missing_employees2 = check_missing('C:\\Payroll\\active_employees.txt', 'C:\\Payroll\\payroll_all_dirnames2.txt', threshold)

missing_employees3 = sorted(missing_employees2, key=lambda patterns: patterns.chunks[1])

length = (len(missing_employees3))

print("***\nMissingEmployees with threshold of %d finished with a length of %d**\n" % (threshold, length))

with open('F:\\Payroll\\EmployeeData\\missing_employees.txt', 'w') as missing_employee:
    for employee in missing_employees3:
        missing_employee.write(employee.text + '\n')
