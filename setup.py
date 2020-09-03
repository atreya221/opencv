import os
import platform

if platform.system() == 'Windows':
  os.system('python -m pip install --user virtualenv')
  os.system('python -m venv .env')
  os.system('.\.env\Scripts\\activate & pip install setuptools wheel')
  os.system('.\.env\Scripts\\activate & pip install -r requirements.txt')
  

if platform.system() == 'Linux':
  os.system('python -m pip install --user virtualenv')
  os.system('python -m venv .env')
  os.system('. .env/bin/activate; pip install setuptools wheel')
  os.system('. .env/bin/activate; pip install -r requirements.txt')
  

