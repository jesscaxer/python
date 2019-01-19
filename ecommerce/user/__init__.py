import hashlib


def encrption_pwd(password):
    password = password
    password = hashlib.md5(password.encode('utf-8'))
    password = password.hexdigest()
    return password