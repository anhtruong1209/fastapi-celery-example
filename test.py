from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

import os 

user_name = os.environ.get('mongo_user')
password = os.environ.get('mongo_password')

print(user_name, password)
