# MODIFICATION:
# Triple-DES CBC encrypt/decrypt with padding. This is a student-friendly addition derived from the official exercise; no source listing was supplied.

from cryptography.hazmat.decrepit.ciphers.algorithms import TripleDES
from cryptography.hazmat.primitives.ciphers import Cipher,modes
from cryptography.hazmat.primitives import padding
import os
def key24(k8):
 if len(k8)!=24: raise ValueError('3DES key must be 24 bytes')
 return k8
def encrypt(text,k8):
 iv=os.urandom(8); p=padding.PKCS7(64).padder(); d=p.update(text.encode())+p.finalize(); e=Cipher(TripleDES(key24(k8)),modes.CBC(iv)).encryptor(); return iv,e.update(d)+e.finalize()
def decrypt(iv,c,k8):
 d=Cipher(TripleDES(key24(k8)),modes.CBC(iv)).decryptor(); raw=d.update(c)+d.finalize(); u=padding.PKCS7(64).unpadder(); return (u.update(raw)+u.finalize()).decode()
if __name__=='__main__':
 m=input('Message: '); k=b'12345678ABCDEFGH87654321'; iv,c=encrypt(m,k); print('Ciphertext:',c.hex()); print('Decrypted:',decrypt(iv,c,k))
