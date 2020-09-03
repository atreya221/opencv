import os
import platform

if platform.system() == 'Windows':
  os.system('python -m pip install virtualenv')
  os.system('.\opencv1\Scripts\\activate & pip install -r requirements.txt')
  

if platform.system() == 'Linux':
  os.system('python -m pip install --user virtualenv')
  os.system('source opencv2/bin/activate; pip install -r requirements.txt')
  

