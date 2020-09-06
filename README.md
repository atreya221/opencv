# A clone of Teachable Machine

Follow the instructions in requirements.txt
Objective of this code is to differentiate between two classes(cats vs dogs) using tensorflow and convolutional neural network model

First step is to execute the setup.py file for installing all the required/to upgrade the modules in a virtual environment. 
Second step is to run the script.py file which is an user interface within which the entire code will run
In script.py file, create_data.py file will be executed first where a new dataset can be created to identify an extra component.
Next train_model.py file will train the model and summary of the model will be printed. The trained model will be saved as "model.h5".
predict_model.py file will predict the output and incase you want to continue with a different set of datas, restore.py file will be excuted, within which the previously trained model will be removed.
Finally if you want to continue, run the script.py file again.
