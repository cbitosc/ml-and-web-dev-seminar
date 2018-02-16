#config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #Use this for relative directory representation

''' Include all your API calls and database initialisations here(like API key,
	Secret Key,etc); Keep in mind that we only add initialisations here and not 
	the definations nor do we create the database here. All we do is initialise
	the object references.'''