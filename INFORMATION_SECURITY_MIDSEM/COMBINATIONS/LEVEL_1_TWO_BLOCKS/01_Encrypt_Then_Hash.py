# MODIFICATION:
# Syllabus-grounded combination exercise. This is a student-friendly addition derived from the official exercise; no source listing was supplied.

import hashlib
from pathlib import Path
# Reuse AES-GCM as the encryption block.
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
key=AESGCM.generate_key(128); nonce=os.urandom(12); msg=input('Message: ').encode(); ct=AESGCM(key).encrypt(nonce,msg,None); print('Ciphertext:',ct.hex()); print('SHA-256:',hashlib.sha256(ct).hexdigest())
