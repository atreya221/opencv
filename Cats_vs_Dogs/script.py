import os
import platform

if platform.system() == 'Windows':
  os.system('.\opencv1\Scripts\\activate & python create_data.py')

if platform.system() == 'Linux':
  os.system('. ../opencv2/bin/activate; python create_data.py')
