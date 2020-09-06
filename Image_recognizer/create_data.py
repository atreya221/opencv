import os
import pathlib  
import zipfile
import shutil
import pyfastcopy

# print(os.system('where python'))

classes = []
count = 0

# Minimum of 2 classes
for i in range(2):
  count = count + 1
  class_name = input(f'Enter title of class {count}:\n')
  classes.append(class_name)

# Additional classes
while True:
  more_classes = input('Add another class? Press Y for yes, N for no.\n')
  if more_classes.lower() == 'y':
    count = count + 1
    class_name = input(f'Enter title of class {count}:\n')
    classes.append(class_name)
  elif more_classes.lower() == 'n':
    break
  else:
    print('Please enter a valid choice.')

print("This code may take a couple of minutes to run depending on your system and size of dataset.")
print("Preparing your dataset ...")
suc = 1
for class_cat in sorted(classes):
    dir_loc = input(f"Enter location of directory containing images of class '{class_cat}':\n")
    try:
        if(os.path.exists(f'./data/train/{class_cat}')): # if path to the directory already exists then delete the directory
          shutil.rmtree('./data/', ignore_errors = True)
        shutil.copytree(dir_loc, f'./data/train/{class_cat}')
    except:
        print("Please enter a valid location.")
        suc = 0
        break
if suc == 1 :
    print("Dataset stored successfully")
else :
    print("Run this code again.")
