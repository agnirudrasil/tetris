from cryptography.fernet import Fernet
from scripts import openfile

with open(openfile('data/56f3db44e25e3057caa2b78751fa212c'), 'rb') as file:
    key = Fernet(file.read())


def encrypt():
    with open(openfile('data/users.json'), 'rb') as f:
        encrypted = f.read()

    with open(openfile('data/users.json'), 'wb') as f:
        f.write(key.encrypt(encrypted))


def decrypt():
    with open(openfile('data/users.json'), 'rb') as f:
        encrypted = f.read()

    with open(openfile('data/users.json'), 'wb') as f:
        f.write(key.decrypt(encrypted))


def generate_key():
    global key
    with open(openfile('data/56f3db44e25e3057caa2b78751fa212c'), 'wb') as f:
        key = Fernet.generate_key()
        f.write(key)