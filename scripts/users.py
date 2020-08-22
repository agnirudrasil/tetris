import json
from scripts import openfile, encrypt


def load_user():
    encrypt.decrypt()
    with open((openfile('data/users.json')), 'r+') as f:
        user = json.load(f)
    encrypt.encrypt()
    return user


def save_user(user):
    with open(openfile('data/users.json'), 'w') as f:
        json.dump(user, f, indent=6)
    encrypt.encrypt()
