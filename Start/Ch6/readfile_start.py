#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents
sample_file = open("textfile.txt", "r")
if sample_file.mode == 'r':
    # use the read() function to read the entire file
    # contents = sample_file.read()
    # print(contents)
    file_lines = sample_file.readlines()
    for line in file_lines:
        print(line)


import os
from os import path

dir_path = "/workspaces/learning-python-3980343/"
for i in os.listdir(dir_path):
    if ".txt" in os.path.basename(i):
        print(os.path.splitext(i))
        print(os.path.getsize(i))

# def file_info():
    
#     return 0

# totalsize = 0
# for i in os.listdir(dir_path):
#     if ".txt" in os.path.basename(i):
#         totalsize = totalsize + os.path.getsize(i)
#     else: totalsize = totalsize
# print(totalsize)

def file_info():
    dir_path = "deps"
    totalsize = 0
    for i in os.listdir(dir_path):
        if ".txt" in os.path.basename(i):
           totalsize = totalsize + os.path.getsize(i)
        else: totalsize = totalsize
    return totalsize