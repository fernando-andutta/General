

# RUN: "C:/Program Files/Python/Pconython38/python.exe" c:/FERNANDO/tutorials/PERSONAL_CODES/PERSONAL_CODES_PYTHON/test1.py

# INITIAL STEPS REQUIRED TO RUN THIS CODE IN VISUAL STUDIO CODE
# 1 - download and install python in your PC
# 2 - install python extenson here
# 3 - install pip extension here to install modules faster
# 4 - update pip in admnistrator-prompt cmd: 'python -m pip install --upgrade pip'
# 5 - install numpy in admnistrator-prompt cmd: 'pip install numpy'  for math module
# 6 - install xlrd in admnistrator-prompt using: 'pip install xlrd'	 to read excel
# 7 - install pandas in admnistrator-prompt using: 'pip install pandas'	 to read excel


# loading needed mobules
import time
#from pathlib import Path as path
import os

import glob
#import importlib # (NOT USED)
import array as array # (NOT USED)
#import numpy as np # (NOT USED)
#import xlrd as xlrd # (NOT USED)
from xlrd import open_workbook
#import pandas as pd # (NOT USED)
#from pandas import read_excel # (NOT USED)
#import sys # (NOT USED)
#import words as words # (NOT USED)
import shutil as shutil # XXX The functions here don't copy the resource fork or other metadata on Mac.

#from cx_Freeze import setup, Executable
import tkinter as tk
from tkinter import *
import threading

from threading import Timer
from time import sleep

# START TIME (to compute processing time)
t0 = time.time()

############################################################
# Section to check module availability (good to check numpy)
############################################################
#import imp as imp
# checking if module is availabe to be loaded
#try:
#    module1 = 'numpy'
#    imp.find_module(module1)
#    found1 = 'True'
#except ImportError:
#    found1 = 'False'
#
#if found1 == 'True':
#    print ("Module ('%s') is available," % module1)
#elif found1 == 'False':
#    print ("Module ('%s') is not available," % module1)
#######################################################
#######################################################

#######################################################
# creating array of strings
#######################################################

#array_str1 = np_zeros((files_this_level_size,), dtype=str) # WORKS FINE
#array_str1 = np_zeros((files_this_level_size,), dtype=object) # perfect for string replacements
#array_str1 = ['']*files_this_level_size # WORKS FINE

#array_str1 = [words.replace('', 'testing') for words in array_str1] # WORKS FINE
#print(array_str1)
#######################################################
#######################################################


def print_progess():
    root = Tk()
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location
    root.geometry("500x100") #Width x Height
    w = Label(root, text="\n \n Please wait process to complete.\n A final message will be displayed when your report-file is ready.")
    w.pack()
    dt = 1 # seconds
    root.after(1000, lambda: root.destroy()) # Destroy the widget after 1 seconds
    root.mainloop()

print_progess()

print("***************************************************")
print("**********                              ***********")
print("********** **      **      **  **       ***********")
print("**********  **    ****    **   **       ***********")
print("**********   **  **  **  **    **       ***********")
print("**********    ****    ****     **       ***********")
print("**********     **      **      *******  ***********")
print("**********                              ***********")
print("***************************************************")


print("#")
print("#")
print("##################################################")
print("# Checking the existence of folders and files to be processed #")
print("##################################################")

# saving path of current directory
path_maindir = os.getcwd()
print ("The current working directory is %s" % path_maindir)

# making folder names to transfer files according to categories
filename_backup = 'FOLDER_BACKUP'
filename_passed = 'FOLDER_PASSED_LEVEL1'
filename_failed = 'FOLDER_FAILED'

# creating folders above mentioned
path_filename_backup = path_maindir + "\\" + filename_backup
if not os.path.exists(path_filename_backup):
    os.makedirs(path_filename_backup)
    print("Directory '%s' created" %filename_backup) 
print("Directory '%s' exists" %filename_backup) 


path_filename_passed = path_maindir + "\\" + filename_passed
if not os.path.exists(path_filename_passed):
    os.makedirs(path_filename_passed)
    print("Directory '%s' created" %filename_passed) 
print("Directory '%s' exists" %filename_passed) 

path_filename_failed = path_maindir + "\\" + filename_failed
if not os.path.exists(path_filename_failed):
    os.makedirs(path_filename_failed)
    print("Directory '%s' created" %filename_failed) 
print("Directory '%s' exists" %filename_failed) 

# checking all excel files (xlsx) in main directory
extension = 'xlsx'
os.chdir(path_maindir)
files_this_level = glob.glob('*.{}'.format(extension))
files_this_level_size = len(files_this_level)
print("Total xslx files in this directory = '%s' " %files_this_level_size) 
print("Current files in this directory = '%s' " %files_this_level) 

value_range = len(files_this_level)
#files_this_level2 = np_zeros((value_range,), dtype=int)
files_this_level2 = ['0'] 
for mm in range(value_range-1): files_this_level2.append('0') 

# checking for files already in the folder PASSED
files_2do = {''} # variable to create array of filenames to be processed
for xx in range(files_this_level_size):
    file_this_level_aux = files_this_level[xx]
    print("File = '%s' " %xx) 
    print(file_this_level_aux)

    file_this_level_passed = path_maindir + "\\" + filename_passed + "\\" + file_this_level_aux

    # defining variables to be upadated in if statements
    file_passed = 0
    file_failed = 0

    # checking existence of files in folders
    # OBS: better to use positive searchers at front, and negatives latter. See examples below!!!
    #if not os.path.exists(file_this_level_passed)  and not os.path.exists(file_this_level_failed):
    #if os.path.exists(file_this_level_passed) and not os.path.exists(file_this_level_failed):

    if not os.path.exists(file_this_level_passed):
        files_this_level2[xx] = 2 #
    else:
        files_this_level2[xx] = 1 #



##########################################################################
# BACKING UP FILES IN FOLDER BACKUP
#########################################################################3

total_files_processed = 0

for xx in range(files_this_level_size):
    file_this_level_aux = files_this_level[xx]

    file_this_level_backup1 = path_maindir + "\\" + file_this_level_aux
    file_this_level_backup2 = path_maindir + "\\" + filename_backup + "\\" + file_this_level_aux
    
    shutil.copy2(file_this_level_backup1, file_this_level_backup2)


print("#")
print("#")
print("##########################################")
print("# Generating array for file locations #")
print("##########################################")

#array_str1 = np_zeros((files_this_level_size,), dtype=object)
array_str1 = ['0'] 
for mm in range(files_this_level_size-1): array_str1.append('0')

print(array_str1)
for xx in range(files_this_level_size):
    files_this_level_aux = files_this_level[xx]
    print(files_this_level_aux)
    array_str2 = path_maindir + "\\" + files_this_level_aux
    print(array_str2)
    array_str1[xx] = array_str2
file_location_array = array_str1


#print("#")
#print("#")
#print("################################################################")
#print("# Filenames to be checked = '%s' (no=1 and yes=2) #" %files_this_level2)
#print("################################################################")

for xx in range(files_this_level_size):

    failed_any = 0 # this var is added 1 if fails any

    #print(xx)
    files_this_level2_aux = files_this_level2[xx] # index to 1 (do not do) 
    files_this_level_aux = files_this_level[xx]
    #print(files_this_level_aux)
    #file_location = path_maindir + "\\" + file_this_level_aux
    file_location = file_location_array[xx]
    #print(file_location)

    print_progess()
    if files_this_level2_aux==2:
        #print_progess()


        total_files_processed = total_files_processed + 1
        print("#")
        print("#")
        print("#")
        print("#######################################################################")
        print("#######################################################################")
        print("#######################################################################")
        print("File = '%s' (to be checked)" %files_this_level_aux)
        #print("Location = '%s'" %file_location)
        data1 = open_workbook(file_location)
        sheet1 = data1.sheet_by_name("MAIN")
        #sheet1 = data1.sheet_by_index(0)
        #sheet1 = read_excel(loc, sheet_name = "MAIN", range = "A1:L18")
        sheet2 = data1.sheet_by_name("CITATIONS")
        sheet3 = data1.sheet_by_name("REFERENCES")

        sheet1_ncols = sheet1.ncols
        sheet1_nrows = sheet1.nrows
        sheet2_ncols = sheet2.ncols
        sheet2_nrows = sheet2.nrows
        sheet3_ncols = sheet3.ncols
        sheet3_nrows = sheet3.nrows
        
        #cell1 = sheet1.cell(17, 2) # works fine!
        #sheet1_row = sheet1.row(6) # works fine!
        #sheet1_col = sheet1.col(6) # works fine!


        ##########################################################################
        # COUNTING TOTAL ROWS IN SHEET-CITATIONS
        ##########################################################################
        citations_total = 0 # start assumin no citation is provided for empty file
        sheet2_row_start = 10
        for yy in range(sheet2_row_start,sheet2_nrows-2):

            #print(yy)
            # GET 3 CONSECUTIVE ROWS
            yy1 = yy
            yy2 = yy+1
            yy3 = yy+2
            sheet2_row_aux1 = sheet2.row(yy1)
            sheet2_row_aux2 = sheet2.row(yy2)
            sheet2_row_aux3 = sheet2.row(yy3)


            # CITATION - PIECE (CHECK 3 CONSECUTIVE PIECES)
            sheet2_row_aux1_col2 = sheet2_row_aux1[1] # columns(citation-piece)
            sheet2_row_aux1_col2_value = sheet2_row_aux1_col2.value

            sheet2_row_aux2_col2 = sheet2_row_aux2[1] # columns(citation-piece)
            sheet2_row_aux2_col2_value = sheet2_row_aux2_col2.value

            sheet2_row_aux3_col2 = sheet2_row_aux3[1] # columns(citation-piece)
            sheet2_row_aux3_col2_value = sheet2_row_aux3_col2.value

            # CITATION - LENGTH
            sheet2_row_aux1_col2_value_size = len(sheet2_row_aux1_col2_value)
            sheet2_row_aux2_col2_value_size = len(sheet2_row_aux2_col2_value)
            sheet2_row_aux3_col2_value_size = len(sheet2_row_aux3_col2_value)

            sheet2_row_aux123_col1_value_size = sheet2_row_aux1_col2_value_size + sheet2_row_aux2_col2_value_size + sheet2_row_aux3_col2_value_size

            if sheet2_row_aux123_col1_value_size>0:
                #print("Total characters in citation-piece = '%s'" %sheet2_row_aux1_col2_value_size)
                #print("Citation-piece = '%s'" %sheet2_row_aux1_col2_value)
                citations_total = citations_total+1

        citations_total_str = str(citations_total)

        print("File = " + files_this_level_aux + " has a total of " + citations_total_str + " pieces of citations")
        #print("#######################################################################")

        #print("#")
        print("#######################################################################")
        print("# Checking classification of CITATIONS #")
        #print("#######################################################################")



        ############################################################################
        # PROCESSING ROWS IN SHEET-CITATIONS
        ############################################################################
        #checking_classification = np_zeros((citations_total,), dtype=object) # perfect for string replacements
        checking_classification = ['0'] 
        for mm in range(citations_total-1): checking_classification.append('0')


        sheet2_row_start = 10
        sheet2_row_end = sheet2_row_start + citations_total
        for yy in range(sheet2_row_start,sheet2_row_end):
            yy1 = yy
            sheet2_row_aux1 = sheet2.row(yy1)
            sheet2_row_aux1_col1 = sheet2_row_aux1[0]
            sheet2_row_aux1_col1_value = sheet2_row_aux1_col1.value
            #print("Citation piece = " + sheet2_row_aux1_col1_value)

            # CITATION CLASSIFICAITON
            sheet2_row_aux1_col2 = sheet2_row_aux1[2]
            sheet2_row_aux1_col3= sheet2_row_aux1[3]
            sheet2_row_aux1_col4 = sheet2_row_aux1[4]


            # It may convert all to small letters using (islower()), then only x would be used.
            # Howoever, speed seems to increase even though less lines
            sheet2_row_aux1_col2_value = sheet2_row_aux1_col2.value
            sheet2_row_aux1_col3_value = sheet2_row_aux1_col3.value
            sheet2_row_aux1_col4_value = sheet2_row_aux1_col4.value

            sheet2_row_aux1_col2_value = sheet2_row_aux1_col2_value.lower()
            sheet2_row_aux1_col3_value = sheet2_row_aux1_col3_value.lower()
            sheet2_row_aux1_col4_value = sheet2_row_aux1_col4_value.lower()

            str1 = "x"
            #str2 = "X"
            col2_total_x = sheet2_row_aux1_col2_value.count(str1)
            col3_total_x = sheet2_row_aux1_col3_value.count(str1)
            col4_total_x = sheet2_row_aux1_col4_value.count(str1)


            #sheet2_row_aux1_col2to4_len = len(sheet2_row_aux1_col2.value) + len(sheet2_row_aux1_col3.value) + len(sheet2_row_aux1_col4.value)
            sheet2_row_aux1_col2to4_len = col2_total_x + col3_total_x + col4_total_x
            #print("total x in classification = " + str(sheet2_row_aux1_col2to4_len))
          
            if sheet2_row_aux1_col2to4_len==1 or sheet2_row_aux1_col2to4_len==2:

                sheet2_row_aux1_col1_value2 = "sheet-CITATION @ " + sheet2_row_aux1_col1_value + ". Indication of citation-classification. PASSED;"
                print(sheet2_row_aux1_col1_value2)
            else:
                failed_any = failed_any + 1
                sheet2_row_aux1_col1_value2 = "sheet-CITATION @ " + sheet2_row_aux1_col1_value + ".You have indicated 0 or 3 classifications. FAILED;"
                print(sheet2_row_aux1_col1_value2)

            yy2 = yy1 - sheet2_row_start # to fill the rows
            checking_classification[yy2] = sheet2_row_aux1_col1_value2


        #print("#")
        print("#######################################################################")
        print("# Checking indication of position for CITATIONS #")
        #print("#######################################################################")
        #print("#")

        #checking_position = np_zeros((citations_total,), dtype=object) # perfect for string replacements
        checking_position = ['0'] 
        for mm in range(citations_total-1): checking_position.append('0')

        sheet2_row_start = 10
        sheet2_row_end = sheet2_row_start + citations_total
        for yy in range(sheet2_row_start,sheet2_row_end):
            yy1 = yy
            sheet2_row_aux1 = sheet2.row(yy1)
            sheet2_row_aux1_col1 = sheet2_row_aux1[0]
            sheet2_row_aux1_col1_value = sheet2_row_aux1_col1.value
            #print("Citation piece = " + sheet2_row_aux1_col1_value)


            # CITATION POSITION            
            sheet2_row_aux1_col6 = sheet2_row_aux1[5]
            sheet2_row_aux1_col7 = sheet2_row_aux1[6]
            sheet2_row_aux1_col8 = sheet2_row_aux1[7]
            sheet2_row_aux1_col9 = sheet2_row_aux1[8]
            sheet2_row_aux1_col10 = sheet2_row_aux1[9]

            #sheet2_row_aux1_col6to10_len = len(sheet2_row_aux1_col6.value) + len(sheet2_row_aux1_col7.value) + len(sheet2_row_aux1_col8.value) + len(sheet2_row_aux1_col9.value) + len(sheet2_row_aux1_col10.value)
            #print("total x in position = " + str(sheet2_row_aux1_col6to10_len))

            
            # It may convert all to small letters using (islower()), then only x would be used.
            # Howoever, speed seems to increase even though less lines
            sheet2_row_aux1_col6_value = sheet2_row_aux1_col6.value 
            sheet2_row_aux1_col7_value = sheet2_row_aux1_col7.value
            sheet2_row_aux1_col8_value = sheet2_row_aux1_col8.value
            sheet2_row_aux1_col9_value = sheet2_row_aux1_col9.value
            sheet2_row_aux1_col10_value = sheet2_row_aux1_col10.value

            sheet2_row_aux1_col6_value = sheet2_row_aux1_col6_value.lower()
            sheet2_row_aux1_col7_value = sheet2_row_aux1_col7_value.lower()
            sheet2_row_aux1_col8_value = sheet2_row_aux1_col8_value.lower()
            sheet2_row_aux1_col9_value = sheet2_row_aux1_col9_value.lower()
            sheet2_row_aux1_col10_value = sheet2_row_aux1_col10_value.lower()

            str1 = "x"
            #str2 = "X"

            col6_total_x = sheet2_row_aux1_col6_value.count(str1)
            col7_total_x = sheet2_row_aux1_col7_value.count(str1)
            col8_total_x = sheet2_row_aux1_col8_value.count(str1)
            col9_total_x = sheet2_row_aux1_col9_value.count(str1)
            col10_total_x = sheet2_row_aux1_col10_value.count(str1)


            sheet2_row_aux1_col6to10_len = col6_total_x + col7_total_x + col8_total_x + col9_total_x + col10_total_x
            #print(str(sheet2_row_aux1_col1_value) + " has total x here =" + str(sheet2_row_aux1_col6to10_len)) 

            if sheet2_row_aux1_col6to10_len==1 or sheet2_row_aux1_col6to10_len==2:
                sheet2_row_aux1_col1_value2 = "sheet-CITATION @ " + sheet2_row_aux1_col1_value + ". Indication of citation position within publication. PASSED;"
                print(sheet2_row_aux1_col1_value2)
            else:
                failed_any = failed_any + 1
                sheet2_row_aux1_col1_value2 = "sheet-CITATION @ " + sheet2_row_aux1_col1_value + ". You have indicated 0, or 3, or 4, or 5 positions. FAILED;"
                print(sheet2_row_aux1_col1_value2)
            
            yy2 = yy1 - sheet2_row_start # to fill the rows
            checking_position[yy2] = sheet2_row_aux1_col1_value2



        ##########################################################################
        # COUNTING TOTAL ROWS IN SHEET-REFERENCES
        ##########################################################################
        references_total = 0 # start assumin no citation is provided for empty file
        sheet3_row_start = 4
        for yy in range(sheet3_row_start,sheet3_nrows-2):

            #print(yy)
            # GET 3 CONSECUTIVE ROWS
            yy1 = yy
            yy2 = yy+1
            yy3 = yy+2
            sheet3_row_aux1 = sheet3.row(yy1)
            sheet3_row_aux2 = sheet3.row(yy2)
            sheet3_row_aux3 = sheet3.row(yy3)


            # REFERENCE - TITLE (CHECK 3 CONSECUTIVE PIECES)
            sheet3_row_aux1_col2 = sheet3_row_aux1[1] # columns(citation-piece)
            sheet3_row_aux1_col2_value = sheet3_row_aux1_col2.value

            sheet3_row_aux2_col2 = sheet3_row_aux2[1] # columns(citation-piece)
            sheet3_row_aux2_col2_value = sheet3_row_aux2_col2.value

            sheet3_row_aux3_col2 = sheet3_row_aux3[1] # columns(citation-piece)
            sheet3_row_aux3_col2_value = sheet3_row_aux3_col2.value

            # REFERENCE - LENGTH
            sheet3_row_aux1_col2_value_size = len(sheet3_row_aux1_col2_value)
            sheet3_row_aux2_col2_value_size = len(sheet3_row_aux2_col2_value)
            sheet3_row_aux3_col2_value_size = len(sheet3_row_aux3_col2_value)

            sheet3_row_aux123_col1_value_size = sheet3_row_aux1_col2_value_size + sheet3_row_aux2_col2_value_size + sheet3_row_aux3_col2_value_size

            if sheet3_row_aux123_col1_value_size>0:
                #print("Total characters in citation-piece = '%s'" %sheet2_row_aux1_col2_value_size)
                #print("Citation-piece = '%s'" %sheet2_row_aux1_col2_value)
                references_total = references_total+1

        references_total_str = str(references_total)

        print("#######################################################################")
        print("File = " + files_this_level_aux + " has a total of " + references_total_str + " references")
        print("#######################################################################")


        ############################################################################
        # PROCESSING ROWS IN SHEET-REFERENCES
        ############################################################################
        #checking_reference = np_zeros((references_total,), dtype=object) # perfect for string replacements
        checking_reference = ['0'] 
        for mm in range(references_total-1): checking_reference.append('0')


        sheet3_row_start = 4
        sheet3_row_end = sheet3_row_start + references_total
        for yy in range(sheet3_row_start,sheet3_row_end):

            yy1 = yy
            sheet3_row_aux1 = sheet3.row(yy1)
            # REFERENCE - INDEX
            sheet3_row_aux1_col1 = sheet3_row_aux1[0] # columns(citation-piece)
            sheet3_row_aux1_col1_value = sheet3_row_aux1_col1.value


            # REFERENCE INFORMATION
            sheet3_row_aux1_col2 = sheet3_row_aux1[1]
            sheet3_row_aux1_col3 = sheet3_row_aux1[2]
            sheet3_row_aux1_col4 = sheet3_row_aux1[3]
            sheet3_row_aux1_col5 = sheet3_row_aux1[4]
            sheet3_row_aux1_col6 = sheet3_row_aux1[5]
            sheet3_row_aux1_col7 = sheet3_row_aux1[6]
            sheet3_row_aux1_col8 = sheet3_row_aux1[7]
            sheet3_row_aux1_col9 = sheet3_row_aux1[8]

            sheet3_row_aux1_col2_value = sheet3_row_aux1_col2.value
            sheet3_row_aux1_col3_value = sheet3_row_aux1_col3.value
            sheet3_row_aux1_col4_value = sheet3_row_aux1_col4.value
            sheet3_row_aux1_col5_value = sheet3_row_aux1_col5.value
            sheet3_row_aux1_col6_value = sheet3_row_aux1_col6.value
            sheet3_row_aux1_col7_value = sheet3_row_aux1_col7.value
            sheet3_row_aux1_col8_value = sheet3_row_aux1_col8.value
            sheet3_row_aux1_col9_value = sheet3_row_aux1_col9.value

            # floats must be changed to strings
            sheet3_row_aux1_col2_value = str(sheet3_row_aux1_col2_value)
            sheet3_row_aux1_col3_value = str(sheet3_row_aux1_col3_value)
            sheet3_row_aux1_col4_value = str(sheet3_row_aux1_col4_value)
            sheet3_row_aux1_col5_value = str(sheet3_row_aux1_col5_value)
            sheet3_row_aux1_col6_value = str(sheet3_row_aux1_col6_value)
            sheet3_row_aux1_col7_value = str(sheet3_row_aux1_col7_value)
            sheet3_row_aux1_col8_value = str(sheet3_row_aux1_col8_value)
            sheet3_row_aux1_col9_value = str(sheet3_row_aux1_col9_value)
            

            sheet3_row_aux1_col2_value_len = len(sheet3_row_aux1_col2_value)
            sheet3_row_aux1_col3_value_len = len(sheet3_row_aux1_col3_value)
            sheet3_row_aux1_col4_value_len = len(sheet3_row_aux1_col4_value)
            sheet3_row_aux1_col5_value_len = len(sheet3_row_aux1_col5_value)
            sheet3_row_aux1_col6_value_len = len(sheet3_row_aux1_col6_value)
            sheet3_row_aux1_col7_value_len = len(sheet3_row_aux1_col7_value)
            sheet3_row_aux1_col8_value_len = len(sheet3_row_aux1_col8_value)
            sheet3_row_aux1_col9_value_len = len(sheet3_row_aux1_col9_value)



         
            if sheet3_row_aux1_col2_value_len>=3 and sheet3_row_aux1_col3_value_len>=3 and sheet3_row_aux1_col4_value_len>=3 and sheet3_row_aux1_col5_value_len>=4 and sheet3_row_aux1_col6_value_len>=3 and sheet3_row_aux1_col7_value_len>=1 and sheet3_row_aux1_col8_value_len>=1 and sheet3_row_aux1_col9_value_len>=1:
                sheet3_row_aux1_col2to9_value2 = "sheet-REFERENCE @ " + sheet3_row_aux1_col1_value + ". Cells have been completed. PASSED;"
                print(sheet3_row_aux1_col2to9_value2)
            else:
                failed_any = failed_any + 1
                sheet3_row_aux1_col2to9_value2 = "sheet REFERENCE @ " + sheet3_row_aux1_col1_value + ". Check possible problem in this row. FAILED;"
                print(sheet3_row_aux1_col2to9_value2)
            
            yy2 = yy1 - sheet3_row_start # to fill the rows
            checking_reference[yy2] = sheet3_row_aux1_col2to9_value2



        ############################################################################
        # PROCESSING - INDEXES FOR CITATIONS AND REFERNCES 
        ############################################################################
        #checking_reference_index = np_zeros((references_total,), dtype=object) # perfect for string replacements
        checking_reference_index = ['0'] 
        for mm in range(references_total-1): checking_reference_index.append('0')
        
        sheet3_row_start = 4
        sheet3_row_end = sheet3_row_start + references_total
        for yy in range(sheet3_row_start,sheet3_row_end):
            yy1 = yy
            sheet3_row_aux1 = sheet3.row(yy1)
            
            # REFERENCE INDEX
            sheet3_row_aux1_col1 = sheet3_row_aux1[0]
            sheet3_row_aux1_col1_value = sheet3_row_aux1_col1.value

            yy2 = yy1 - sheet3_row_start # to fill the rows
            checking_reference_index[yy2] = sheet3_row_aux1_col1_value        
        #print(checking_reference_index)


        #checking_citation_index = np_zeros((citations_total,), dtype=object) # perfect for string replacements
        checking_citation_index = ['0'] 
        for mm in range(citations_total-1): checking_citation_index.append('0')

        #checking_citation_piece = np_zeros((citations_total,), dtype=object) # perfect for string replacements
        checking_citation_piece = ['0'] 
        for mm in range(citations_total-1): checking_citation_piece.append('0')

        checking_citation_piece_all = "STRING_START = "
        sheet2_row_start = 10
        sheet2_row_end = sheet2_row_start + citations_total
        for yy in range(sheet2_row_start,sheet2_row_end):
            yy1 = yy
            sheet2_row_aux1 = sheet2.row(yy1)
            
            # CITATION INDEX
            sheet2_row_aux1_col1 = sheet2_row_aux1[0]
            sheet2_row_aux1_col1_value = sheet2_row_aux1_col1.value

            # CITATION PIECE
            sheet2_row_aux1_col2 = sheet2_row_aux1[1]
            sheet2_row_aux1_col2_value = sheet2_row_aux1_col2.value

            yy2 = yy1 - sheet2_row_start # to fill the rows
            checking_citation_index[yy2] = sheet2_row_aux1_col1_value
            checking_citation_piece[yy2] = sheet2_row_aux1_col2_value  
            checking_citation_piece_all = checking_citation_piece_all +  sheet2_row_aux1_col2_value     
        #print(checking_citation_index)
        #print(checking_citation_piece)


        #checking_reference_index_checked = np_zeros((references_total,), dtype=object) # perfect for string replacements
        checking_reference_index_checked = ['0'] 
        for mm in range(references_total-1): checking_reference_index_checked.append('0')

        for yy in range(references_total):
            yy1 = yy
            checking_reference_index_aux = checking_reference_index[yy1]
            
            #print(checking_reference_index_aux)
            # checking its existence in array of citations
            if checking_reference_index_aux in checking_citation_piece_all:

                checking_reference_index_aux
                checking_reference_index_checked[yy1] = "sheet-CITATIONS includes (" + checking_reference_index_aux + "). PASSED;" 
                print(checking_reference_index_checked [yy1])
            else:
                failed_any = failed_any + 1
                checking_reference_index_checked[yy1] = "sheet-CITATIONS includes (" + checking_reference_index_aux + "). FAILED;" 
                print(checking_reference_index_checked [yy1])

        #print(checking_reference_index)
        #print(checking_citation_piece_all)
        #print(checking_reference_index_checked) 

        #checking_citation_piece_checked = np_zeros((citations_total,), dtype=object) # perfect for string replacements
        checking_citation_piece_checked = ['0'] 
        for mm in range(citations_total-1): checking_citation_piece_checked.append('0')

        for yy in range(citations_total):
            yy1 = yy
            checking_citation_piece_aux = checking_citation_piece[yy1]
            checking_citation_index_aux = checking_citation_index[yy1]

            str1 = "#R"
            str2 = "#%"
            str1_total = checking_citation_piece_aux.count(str1)
            str2_total = checking_citation_piece_aux.count(str2)
            #print("R# = " + str(str1_total) + " and #% = " + str(str2_total))

            str3 = "##%"
            str4 = "##R"
            str3_total = checking_citation_piece_aux.count(str3)
            str4_total = checking_citation_piece_aux.count(str4)

            if str1_total>=1 and str2_total>=1 and str1_total == str2_total and str3_total==0 and str4_total==0:
                checking_citation_piece_checked[yy1] = "sheet-CITATION @ " + checking_citation_index_aux + ". Total number of (#R) equals to number of (#%). PASSED;"
            else:
                failed_any = failed_any + 1
                if str3_total==0 and str4_total==0:
                    checking_citation_piece_checked[yy1] = "sheet-CITATION @ " + checking_citation_index_aux + ". Total number of (#R) equals to number of (#%), and not ZERO. FAILED;"
                else:
                    checking_citation_piece_checked[yy1] = "sheet-CITATION @ " + checking_citation_index_aux + ". Please remove (##R) or (##%). FAILED;"
           
        #print(checking_citation_piece_checked) 



        ############################################################################
        # PROCESSING SHEET-MAIN
        ############################################################################
        sheet1_row_aux1 = sheet1.row(11) # PERSONAL INFORMATION
        sheet1_row_aux2 = sheet1.row(17) # PUBLICATION INFORMATION

        #sheet1_row_aux1_len = str(len(sheet1_row_aux1))
        #sheet1_row_aux2_len = str(len(sheet1_row_aux2))
        #print("checking cols of personal information = " + sheet1_row_aux1_len)
        #print("checking cols of article information = " + sheet1_row_aux2_len)

        sheet1_row_aux1_col2 = str(sheet1_row_aux1[1])
        sheet1_row_aux1_col3 = str(sheet1_row_aux1[2])
        sheet1_row_aux1_col4 = str(sheet1_row_aux1[3])
        sheet1_row_aux1_col5 = str(sheet1_row_aux1[4])
        sheet1_row_aux1_col6 = str(sheet1_row_aux1[5])
        sheet1_row_aux1_col7 = str(sheet1_row_aux1[6])
        sheet1_row_aux1_col8 = str(sheet1_row_aux1[7])

        sheet1_row_aux2_col2 = str(sheet1_row_aux2[1])
        sheet1_row_aux2_col3 = str(sheet1_row_aux2[2])
        sheet1_row_aux2_col4 = str(sheet1_row_aux2[3])
        sheet1_row_aux2_col5 = str(sheet1_row_aux2[4])
        sheet1_row_aux2_col6 = str(sheet1_row_aux2[5])
        sheet1_row_aux2_col7 = str(sheet1_row_aux2[6])
        sheet1_row_aux2_col8 = str(sheet1_row_aux2[7])
        sheet1_row_aux2_col9 = str(sheet1_row_aux2[8])
        sheet1_row_aux2_col10 = str(sheet1_row_aux2[9])
        sheet1_row_aux2_col11 = str(sheet1_row_aux2[10])
        sheet1_row_aux2_col12 = str(sheet1_row_aux2[11])

        sheet1_row_aux1_col2_len = len(sheet1_row_aux1_col2)
        sheet1_row_aux1_col3_len = len(sheet1_row_aux1_col3)
        sheet1_row_aux1_col4_len = len(sheet1_row_aux1_col4)
        sheet1_row_aux1_col5_len = len(sheet1_row_aux1_col5)
        sheet1_row_aux1_col6_len = len(sheet1_row_aux1_col6)
        sheet1_row_aux1_col7_len = len(sheet1_row_aux1_col7)
        sheet1_row_aux1_col8_len = len(sheet1_row_aux1_col8)

        sheet1_row_aux2_col2_len = len(sheet1_row_aux2_col2)
        sheet1_row_aux2_col3_len = len(sheet1_row_aux2_col3)
        sheet1_row_aux2_col4_len = len(sheet1_row_aux2_col4)
        sheet1_row_aux2_col5_len = len(sheet1_row_aux2_col5)
        sheet1_row_aux2_col6_len = len(sheet1_row_aux2_col6)
        sheet1_row_aux2_col7_len = len(sheet1_row_aux2_col7)
        sheet1_row_aux2_col8_len = len(sheet1_row_aux2_col8)
        sheet1_row_aux2_col9_len = len(sheet1_row_aux2_col9)
        sheet1_row_aux2_col10_len = len(sheet1_row_aux2_col10)
        sheet1_row_aux2_col11_len = len(sheet1_row_aux2_col11)
        sheet1_row_aux2_col12_len = len(sheet1_row_aux2_col12)

        #print("checking personal information = " + sheet1_row_aux1_col5)
        #print("checking article information = " + sheet1_row_aux2_col5)

        
        #file_this_level_backup2 = path_maindir + "\\" + filename_backup + "\\" + file_this_level_aux
        #shutil.copy2(file_this_level_backup1, file_this_level_backup2)

        ############################################################################
        # SAVING REPORT FILE
        ############################################################################

        if citations_total == 0 or references_total == 0:
            failed_any = failed_any + 1
            
        filename1_source = path_maindir + "\\" + files_this_level_aux

        if failed_any == 0:
            filename1 = path_maindir + "\\" + filename_passed + "\\" + files_this_level_aux + '_report.txt'
            filename1_destination = path_maindir + "\\" + filename_passed + "\\" + files_this_level_aux
        else:
            filename1 = path_maindir + "\\" + filename_failed + "\\" + files_this_level_aux + '_report.txt' 
            filename1_destination = path_maindir + "\\" + filename_failed + "\\" + files_this_level_aux
        
        shutil.copy2(filename1_source, filename1_destination)


        f=open(filename1,"w+")
        #f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \r\n") # consider empty line below
        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        f.write("%%% Below you see questions regarding what is needed to be corrected %%% \n")
        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")

        #################
        # QUESTION 1 ####
        #################
        f.write("1 - Are there any issues in sheet-CITATIONS (classification of citations)? \n")

        aa = 0
        for zz in range(len(checking_classification)):
            checking_classification_aux = checking_classification[zz]
            #f.write(checking_classification_aux)
            #f.write("\n")

            if "PASSED" not in checking_classification_aux:
                f.write(checking_classification_aux)
                f.write("\n")
                aa = aa + 1
        if aa==0 and citations_total>0:
            f.write("Passed.")
            f.write("\n") 
        if aa==0 and citations_total==0:
            f.write("Failed. Empty sheet-CITATIONS")
            f.write("\n") 

        #################
        # QUESTION 2 ####
        #################
        f.write("2 - Are there any issues in sheet-CITATIONS (indicating position of citations)? \n")

        aa = 0
        for zz in range(len(checking_position)):
            checking_position_aux = checking_position[zz]
            #f.write(checking_position_aux)
            #f.write("\n")

            if "PASSED" not in checking_position_aux:
                f.write(checking_position_aux)
                f.write("\n")
                aa = aa + 1
        if aa==0 and citations_total>0:
            f.write("Passed.")
            f.write("\n") 
        if aa==0 and citations_total==0:
            f.write("Failed. Empty sheet-CITATIONS")
            f.write("\n") 

        #################
        # QUESTION 3 ####
        #################
        f.write("3 - Have you properly applied indexes-holder (#R) and (#%) in sheet-CITATIONS? \n")

        #print("total citatos = " + str(citations_total))
        #print("length of sheet2_row = " + str(len(checking_citation_index)))
        aa = 0
        for zz in range(citations_total):
            checking_citation_piece_checked_aux = checking_citation_piece_checked[zz]
            checking_citation_index_aux = checking_citation_index[zz]

            if "PASSED" not in checking_citation_piece_checked_aux:
                text_2print = checking_citation_index_aux + " = " + str(checking_citation_piece_checked_aux)
                f.write(text_2print)
                f.write("\n")
                aa = aa + 1
        if aa==0 and citations_total>0:
            f.write("Passed.")
            f.write("\n") 
        if aa==0 and citations_total==0:
            f.write("Failed. Empty sheet-CITATIONS")
            f.write("\n") 

        #################
        # QUESTION 4 ####
        #################
        f.write("4 - Have all references been cited in sheet-CITATIONS? \n")
        
        aa = 0
        for zz in range(references_total):
            checking_reference_index_checked_aux = checking_reference_index_checked[zz]
            checking_reference_index_aux = checking_reference_index[zz]

            if "PASSED" not in checking_reference_index_checked_aux:
                text_2print = checking_reference_index_aux + " = " + str(checking_reference_index_checked_aux)
                f.write(text_2print)
                f.write("\n")
                aa = aa + 1
        if aa==0 and citations_total>0:
            f.write("Passed.")
            f.write("\n") 
        if aa==0 and citations_total==0:
            f.write("Failed. Empty sheet-CITATIONS")
            f.write("\n") 



        #################
        # QUESTION 5 ####
        #################
        f.write("5 - Have you properly filled all cells in sheet-REFERENCES? \n")
        
        aa = 0
        for zz in range(len(checking_reference)):
            checking_reference_aux = checking_reference[zz]
            #f.write(checking_reference_aux)
            #f.write("\n")
        
            if "PASSED" not in checking_reference_aux:
                f.write(checking_reference_aux)
                f.write("\n")
                aa = aa + 1
        if aa==0 and references_total>0:
            f.write("Passed.")
            f.write("\n")
        if aa==0 and references_total==0:
            f.write("Failed. Empty sheet-REFERENCES")
            f.write("\n")      

        #################
        # QUESTION 6 ####
        #################
        f.write("6 - Have you completed your personal information for cells in sheet-MAIN? \n")
        

        if "empty" in sheet1_row_aux1_col2 or "empty" in sheet1_row_aux1_col3 or "empty" in sheet1_row_aux1_col4:
                f.write("Family-name, or name, or citation-name failed: check cells (B12, C12, D12)")
                f.write("\n")
        else:
                f.write("Cells (B12, C12, D12), passed.")
                f.write("\n")            

        if "@" not in sheet1_row_aux1_col5 or sheet1_row_aux2_col5_len<5:
                f.write("Email failed: check cell (E12)")
                f.write("\n")                
        else:
                f.write("Cell (E12), passed.")
                f.write("\n")   

        if "empty" in sheet1_row_aux1_col6 or "empty" in sheet1_row_aux1_col7 or "empty" in sheet1_row_aux1_col8:
                f.write("Additional personal information failed: check cells (F12, G12, H12), and consider N/A for empty cells")
                f.write("\n")
        else:
                f.write("Cells (F12, G12, H12), passed.")
                f.write("\n")   

        f.write("7 - Have you completed the information of your published article for cells in sheet-MAIN? \n")

        if "empty" in sheet1_row_aux2_col2:
                f.write("Indication of author in publucations failed: check cell (B18)")            
                f.write("\n")
        else:
                f.write("Cell (B18), passed.")
                f.write("\n") 

        if "empty" in sheet1_row_aux2_col3 or "empty" in sheet1_row_aux2_col4 or "empty" in sheet1_row_aux2_col5:
                f.write("Title, or author(s), or doi failed: check cells (C18, D18, E18)")
                f.write("\n")
        else:
                f.write("Cells (C18, D18, E18), passed.")
                f.write("\n")   

        if "empty" in sheet1_row_aux2_col7 or "empty" in sheet1_row_aux2_col8 or "empty" in sheet1_row_aux2_col9 or "empty" in sheet1_row_aux2_col10 or "empty" in sheet1_row_aux2_col11 or "empty" in sheet1_row_aux2_col12:
                f.write("Journal, or volume, or edition, or pages, or main-area, or specific area failed: check cells (G18, H18, I18, J18, K18, L18), and use N/A for empty cells")
                f.write("\n")
        else:
                f.write("Cells (G18, H18, I18, J18, K18, L18), passed.")
                f.write("\n")    

        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        f.write("%%%% Thank you for providing quality assurance on your contribution %%%% \n")
        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")

        f.close() 



for xx in range(files_this_level_size):
    file_this_level_aux = files_this_level[xx]
    
    file_this_level_passed = path_maindir + "\\" + filename_passed + "\\" + file_this_level_aux
    
    file_this_level_failed = path_maindir + "\\" + filename_failed + "\\" + file_this_level_aux
    if os.path.exists(file_this_level_failed) and os.path.exists(file_this_level_passed):
        os.remove(file_this_level_failed)
    
    file_this_level_failed2 = path_maindir + "\\" + filename_failed + "\\" + file_this_level_aux + '_report.txt'
    if os.path.exists(file_this_level_failed2) and  os.path.exists(file_this_level_passed):
        os.remove(file_this_level_failed2)




#print(checking_classification)

#for zz in range(len(checking_classification)):
#    checking_classification_aux = checking_classification[zz]
#    f.write(checking_classification_aux)
#    f.write("\n")

# END TIME
t1 = time.time()

total_time = t1-t0
text1 = "total processing time = " + str(total_time) + " seconds"
print(text1)


if total_files_processed>0:
    time_per_file = total_time/total_files_processed
    text2 = "total processed files = " + str(total_files_processed) + ", with the average time per file = " + str(time_per_file) + " seconds"
    print(text2)
else:
    text2 = "Files processed = 0"
    print(text2)


text3 = "\n" + "Process complete!\n" + text1 + "\n" + text2
def print_complete():
    root = Tk()
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('+%d+%d' % (x, y)) ## this part allows you to only change the location
    root.geometry("500x100") #Width x Height
    #w = Label(root, text="\n \n ###[ Processing complete! ]###")
    w = Label(root, text=text3)
    w.pack()
    dt = 30 # seconds
    root.after(dt*1000, lambda: root.destroy()) # Destroy the widget after 1 seconds
    root.mainloop()

print_complete()
