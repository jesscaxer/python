import hashlib


def set_password(password):
    password = hashlib.md5(password.encode('utf-8'))
    password = password.hexdigest()
    return password