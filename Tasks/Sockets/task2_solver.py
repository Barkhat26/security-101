#!/usr/bin/python

from socket import *  
import re
from hashlib import md5, sha1, sha224, sha256, sha384, sha512

serverHost = 'localhost'                       
serverPort = 9090

pattern = r'^(?P<hash>\w+) hash of (?P<string>\w+) equals'

def get_hash(hash_algo, message):
    if hash_algo == "md5":
        return md5(rand_str).hexdigest()
    elif hash_algo == "sha1":
        return sha1(rand_str).hexdigest()
    elif hash_algo == "sha224":
        return sha224(rand_str).hexdigest()
    elif hash_algo == "sha256":
        return sha256(rand_str).hexdigest()
    elif hash_algo == "sha384":
        return sha384(rand_str).hexdigest()
    else:
        return sha512(rand_str).hexdigest()

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort)) 

# First response with greetings
data = sockobj.recv(1024).strip()
print data
hash_algo = re.search(pattern, data.split('\r\n')[-1]).group('hash')
rand_str = re.search(pattern, data.split('\r\n')[-1]).group('string')
sockobj.sendall(get_hash(hash_algo, rand_str) + '\r\n')

while True:
    data = sockobj.recv(1024).strip()
    print data
    try:
        hash_algo = re.search(pattern, data).group('hash')
        rand_str = re.search(pattern, data).group('string')
        sockobj.sendall(get_hash(hash_algo, rand_str) + '\r\n')
    except Exception:
        import IPython; IPython.embed()
    