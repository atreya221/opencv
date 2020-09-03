import os
import platform

if platform.system() == 'Windows':
  os.system('python -m pip install virtualenv')
  os.system('python -m venv opencv1')
  os.system('.\opencv1\Scripts\\activate & pip install -r requirements.txt')
  

if platform.system() == 'Linux':
  os.system('python -m pip install --user virtualenv')
  os.system('python -m venv opencv2')
  os.system('. opencv2/bin/activate; pip install --upgrade pip setuptools wheel')
  os.system('. opencv2/bin/activate; pip install -r requirements.txt')
  

