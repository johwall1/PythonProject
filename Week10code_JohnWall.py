# This program will show different actions
# performed on files. Users will create a file
# in a direcory, write to it and then have the 
# contents displayed to view.
# Author: John Wall
# Created: 2/20/2022

# Importing the OS library
import os

# prints the current working directory for the user
cwd = os.getcwd()
print(cwd)

# Loop to get an existing directory
while True:

  # Path to directory to be worked in
  dir_path = input('Please enter a directory path: ')

  # Test wether directory exists or not
  dirtest = os.path.isdir(dir_path)
  if dirtest == True:
    print('Directory exists.')
    print()
    break
  else:
    print('Directory does not exist.')
    print()
    continue


# Loop to verify the creation of a new file
while True:

  # Name of file to be created
  file = input('Please enter the file name to be created: ')

  # Creating the file in the specified directory
  file_path = dir_path+'/'+file

  # If statement to prompt if the file was created or already exists
  if os.path.isfile(file_path):
    print('File already exists.')
    continue
  else:
    print('File created')
    print()
    break

# variable used to open the file
testfile = open('file_path', 'x')

# Writing the specifed information in the file to be read
Info = 'Name, Address, Phone Number '
testfile.write(Info)
testfile.close()

# Appending the file with user input comma seperated on a new line
testfile = open('file_path', 'a')
testfile.write("\n")
testfile.write(input('Please enter your Name: '))
testfile.write(', ')
testfile.write(input('Please enter your Address: '))
testfile.write(', ')
testfile.write(input('Please enter your Phone Number: '))
testfile.close()

# Reading the saved file back to the user
testfile = open('file_path', 'r')
print(testfile.read())
testfile.close()
print('File saved at ' , file_path)