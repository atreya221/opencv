import os
import platform
import sys

if platform.system() == 'Windows':
  os.system('..\.env\Scripts\\activate & python create_data.py')

if platform.system() == 'Linux':
  os.system('. ../.env/bin/activate; python create_data.py')

#################################

trained = False

#################################

if trained == False:
  if platform.system() == 'Windows':
    os.system('..\.env\Scripts\\activate & python train_model.py')
    trained = True

  if platform.system() == 'Linux':
    os.system('. ../.env/bin/activate; python train_model.py')
    trained = True

##################################

print('Do you wish to test images now?')
ans = input('Do you wish to test images now? Press Y to continue and any other key if you wish to quit the program\n')
if ans.lower() == 'y':
  while(1):
    if trained == True:
      if platform.system() == 'Windows':
        os.system('..\.env\Scripts\\activate & python predict_model.py')

      if platform.system() == 'Linux':
        os.system('. ../.env/bin/activate; python predict_model.py')
    cont = input('Do you wish to test another image? Press Y to upload another image and any other key to quit.\n')
    if cont.lower() == 'y':
      continue
    else :
      break

else :
  # Delete model, weights and training data
  
  if platform.system() == 'Windows':
    os.system('..\.env\Scripts\\activate & python restore.py')

  if platform.system() == 'Linux':
    os.system('. ../.env/bin/activate; python restore.py')
    
  control = ("Thank you for being with us. We hope you enjoyed our application.\nPress 'r' to rerun the application and 'q' to exit")
  if control == 'r' :
    if platform.system() == 'Windows':
      os.system('..\.env\Scripts\\activate & python script.py')

    if platform.system() == 'Linux':
      os.system('. ../.env/bin/activate; python script.py')
  if control == 'q' :
    sys.exit()
  
  sys.exit()
  
  
