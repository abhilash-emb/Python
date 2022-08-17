# create a fakeuserrecord json file with the userid to timestamps mapping
from faker import Faker
import os
import json

USERDIRPATH = "UserRecord"
FAKEUSERREC = "FakeUserRecord.json"

faker = Faker()

def read_and_extract_user_id(filename):
    with open(os.path.join(USERDIRPATH, filename), 'r') as f:
        data = json.load(f)
        return list(iter(data))[0]

def create_fake_user_record(userid):
    
    user_dict = {}
    fake_datetime_list = []
    for i in range(10):
        fake_datetime_list.append(str(faker.date_time_between(start_date='-24h', end_date='now')))
    
    user_dict[userid] = fake_datetime_list
    return user_dict

def write_user_id(userid):
    with open(os.path.join(USERDIRPATH, FAKEUSERREC), 'a') as f:
        user_dict = create_fake_user_record(userid)
        json.dump(user_dict,f)

if not os.path.exists(USERDIRPATH):
    os.makedirs(USERDIRPATH)


filepath = USERDIRPATH+"/"+FAKEUSERREC
if os.path.isfile(filepath):
    os.remove(filepath)

directory = os.fsencode(USERDIRPATH)
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".json") and (filename != FAKEUSERREC): 
        userid = read_and_extract_user_id(filename)
        write_user_id(userid)
         