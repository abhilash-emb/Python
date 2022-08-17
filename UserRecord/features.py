#program to check and verify login attempts for a given User
#whenever a new user is registered, create a unique id for the user 
#store this id in a list and store the user details against this id in a json file
#when a delete request is processed successfully 
#the corresponding user and associate details are deleted from the list and the json file

import json
from time import time
import uuid
import hashlib
import os
from datetime import datetime
from datetime import timedelta

PATH = "UserRecord"
FAKEUSERREC = "FakeUserRecord.json"

# user class
class User:
    
    def __init__(self, first_name, last_name, dob, gender, phone_number, profession=None, religion=None):
        self.first_name = first_name
        self.last_name  = last_name
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.profession = profession
        self.religion = religion
        self.login_attemps = 0
        self.uid = str(uuid.uuid4())

    def delete_user(self):
        self.first_name = None
        self.last_name  = None
        self.dob = None
        self.gender = None
        self.phone_number = None
        self.profession = None
        self.religion = None
        self.login_attemps = 0
        self.uid = None

    def update_info(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_user_info(self):
        return (self.first_name, self.last_name, self.dob, self.gender, self.profession, self.phone_number, self.login_attemps)
    
    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.last_name
    
    def get_dob(self):
        return self.dob
    
    def get_phone_number(self):
        return self.phone_number

    def increment_login_attempts(self):
        self.login_attemps += 1

    def reset_login_attempts(self):
        self.login_attemps = 0
    
    def print_user_info(self):
        print(self.phone_number)
        
    def get_user_id(self):
        return self.uid

# unique name of the user record file
def user_record_name(user):
    user_record = user.get_firstname() + user.get_lastname() + user.get_dob()
    return str(hashlib.md5(user_record.encode('utf-8')).hexdigest())[-8:]

# save the user details to the user record json file
def save_user(user, users_id, users):
    
    # get the user record filename
    user_record_file = user.get_firstname() + user.get_lastname() + user_record_name(user)

    user_id = user.get_user_id()
    if user_id not in users_id:
        users_id.append(user_id)
    
    # load updated info to the dict
    users[user_id] = user.get_user_info()

    # create the directory if it does not exists
    user_file = user_record_file + ".json" 
    if not os.path.exists(PATH):
        os.makedirs(PATH)

    # write to the json file
    with open(os.path.join(PATH, user_file), 'w') as f:
        json.dump({user_id: users[user_id]},f)
       
# TO-DO
# 2 similar functions : club them into one
def read_user_records_into_dict():
    directory = os.fsencode(PATH)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json") and (filename != FAKEUSERREC): 
            with open(os.path.join(PATH, filename), 'r') as f:
                return json.load(f)

def read_fake_records_into_dict():
    directory = os.fsencode(PATH)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json") and (filename == FAKEUSERREC): 
            with open(os.path.join(PATH, filename), 'r') as f:
                return json.load(f)

# read from the user record file and populate the user id list and user info dict
def read_and_populate_user_details(users_id, users):
    data = read_user_records_into_dict()
    users_id.append(list(iter(data))[0])
    users.update(data)

# delete the user entry from user id list and user info dict. also delete the user record file
def delete_user(user, users_id, users):
    
    # get the user record filename
    user_record_file = user.get_firstname() + user.get_lastname() + user_record_name(user)
    
    user_id = user.get_user_id()
    del users[user_id]
    users_id.remove(user_id)

    # delete file
    if os.path.isfile(user_record_file+".json"):
        os.remove(user_record_file+".json")

    user.delete_user()

# compare the difference of 3 consecutive timestamps, if it is less than 1 hr, then report it
def verify_user_login(user_id, uname):
    
    print("verifying user login attempts for user : ", uname)
    data = read_fake_records_into_dict()
    time_entries = []
    
    for item in sorted(data[user_id]):
        time_entries.append(datetime.fromisoformat(item))
    
    login_error = False
    for e1, e3 in zip(time_entries, time_entries[2:]):
        if (e3 - e1) < timedelta(minutes=60):
            login_error = True
    
    if login_error:
        print("Login Error Found")
    else:
        print("Login is OK")
        

# TO-DO add a main function
# main program 
users_id = []
users = {}

# u = User(first_name="Abhilash", last_name="Thomas", dob="16-03-1983", gender="Male", phone_number="8884266682")
# save_user(u, users_id, users)
# u.update_info(profession="Programmer", phone_number="9886889561")
# save_user(u, users_id, users)
# delete_user(u, users_id, users)

read_and_populate_user_details(users_id, users)

verify_user_login(users_id[0], users.get(users_id[0])[0])

# print(users_id)
# print(users)
