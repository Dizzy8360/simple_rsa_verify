from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64decode,b64encode


'''generate a pem file to use'''
def export_pub_key(pub_key):
    file = open("key","wb")
    file.write(pub_key.exportKey('PEM'))
    file.close()

def import_pub_key():
    file = open("key","rb")
    pub_key = RSA.importKey(file.read())
    return pub_key

def main():
    #temp strings
    signature = "te9RK03MLlRaUazMAnvYuaJ5sCYPwIAGFlE9nNKNfOBBku0HwykhPgz23mGQvZ8oFdaUp6xWVOFmcCfvzj25J4gTiq81m6NUCIt5o7hM1LYy5F2zAadDminWFXFG7PFicqh4djq09odyU6LNyUP2Bk7rlPEHQaHWtP8OAp5ciX0CzBcHRxazFodoSnYhchvCLYCHhokvbjPiOaTbj18Wv7kwlJOZT9MwFCKBqDpHdqd2Ivo0pAUHaox1cWRzBZzF"
    hash_result = "VcZo6l1E1dKDBZcUGKAFX7BzkeBenYHy"
    
    #comment this out after first time
    #we want to replace the key with our own
    keypair = RSA.generate(2048)
    pub_key = keypair.publickey()
    export_pub_key(pub_key)
    
    pub_key = import_pub_key()
    #does the RSA verify
    verifier = PKCS1_v1_5.new(pub_key)
    #the hash we compare to
    digest = SHA256.new()
    
    #hash string is UTF-8 encoded
    digest.update(hash_result.encode())
    #decrypt signature and compare to digest
    verified = verifier.verify(digest, b64decode(signature))
    print(verified)

main()
