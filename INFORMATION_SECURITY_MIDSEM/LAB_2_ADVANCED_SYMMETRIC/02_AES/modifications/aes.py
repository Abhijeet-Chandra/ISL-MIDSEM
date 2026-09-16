# MODIFICATION:
# AES-CBC encrypt/decrypt with PKCS7 padding; use 16/24/32-byte keys. This is a student-friendly addition derived from the official exercise; no source listing was supplied.

from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.primitives import padding
import os
def crypt(data,key,iv,decrypt=False):
 c=Cipher(algorithms.AES(key),modes.CBC(iv)); x=c.decryptor() if decrypt else c.encryptor(); return x.update(data)+x.finalize()
def encrypt(text,key):
 p=padding.PKCS7(128).padder(); data=p.update(text.encode())+p.finalize(); iv=os.urandom(16); return iv,crypt(data,key,iv)
def decrypt(iv,data,key):
 raw=crypt(data,key,iv,True); u=padding.PKCS7(128).unpadder(); return (u.update(raw)+u.finalize()).decode()
if __name__=='__main__':
 m=input('Message: '); key=b'0123456789ABCDEF'; iv,c=encrypt(m,key); print('Ciphertext:',c.hex()); print('Decrypted:',decrypt(iv,c,key))
