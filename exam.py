import json
import requests
from firebase import firebase

class User:
    city = ""
    l_name = ""
    f_name = None

    def __init__(self, city, l_name, f_name):
        self.city = city
        self.l_name = l_name
        self.f_name = f_name


url = "https://api.vk.com/method/groups.getMembers?group_id=33393308&fields=city"
firebase_url = "https://int-test-cff7f.firebaseio.com/"

resp = requests.get(url).text
dic = json.loads(resp)
#print(dic)

allUsers = []

if "response" in dic:
    people = dic["response"]
    if "users" in people:
        people_list = people['users']

        for user in people_list:
            if "city" in user and "first_name" in user and "last_name" in user:
                city = user['city']
                l_name = user['last_name']
                f_name = user['first_name']

                allUsers.append(User(city, l_name, f_name))

#print(allUsers)

db = firebase.FirebaseApplication(firebase_url)

for user in allUsers:
    print(user.__dict__)
    db.put("/users3", data=user.__dict__, name='name')
    #db.post("/users2", user.__dict__)

print(db.get("/users3", None))