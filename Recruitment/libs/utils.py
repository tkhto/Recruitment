import hashlib

def md5(string):
    """ MD5加密 """
    hash_object = hashlib.md5()
    hash_object.update(string.encode('utf-8'))
    return hash_object.hexdigest()