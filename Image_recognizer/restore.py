import shutil
import pyfastcopy
import os

path = './data/'
try:
    shutil.rmtree(path, ignore_errors = True)
except:
    pass
try:
    os.remove('model.json')
except:
    pass
try:
    os.remove('model.h5')
except:
    pass
