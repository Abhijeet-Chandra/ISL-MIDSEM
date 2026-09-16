# MODIFICATION:
# Syllabus-grounded combination exercise. This is a student-friendly addition derived from the official exercise; no source listing was supplied.

import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes
msg=input('Message: ').encode(); digest=hashlib.sha256(msg).digest(); key=rsa.generate_private_key(public_exponent=65537,key_size=2048); sig=key.sign(digest,padding.PKCS1v15(),hashes.SHA256()); key.public_key().verify(sig,digest,padding.PKCS1v15(),hashes.SHA256()); print('Digest:',digest.hex(),'Signature valid: True')
