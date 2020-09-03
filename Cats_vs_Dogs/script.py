import os
import platform

if platform.system() == 'Windows':
  os.system('..\.env\Scripts\\activate & python create_data.py')

if platform.system() == 'Linux':
  os.system('. ../.env/bin/activate; python create_data.py')
