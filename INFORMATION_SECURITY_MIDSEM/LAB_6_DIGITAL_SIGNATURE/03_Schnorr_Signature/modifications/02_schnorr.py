# MODIFICATION:
# tamper detection. This is a student-friendly addition derived from the official exercise; no source listing was supplied.


import hashlib,secrets
P=23; Q=11; G=2
def H(r,m): return int.from_bytes(hashlib.sha256(str(r).encode()+m).digest(),'big')%Q
def sign(m,x): k=secrets.randbelow(Q-1)+1; r=pow(G,k,P); e=H(r,m); return e,(k+e*x)%Q
def verify(m,sig,y): e,s=sig; r=(pow(G,s,P)*pow(pow(y,e,P),-1,P))%P; return H(r,m)==e
if __name__=='__main__':
 x=7;y=pow(G,x,P);m=input('Message: ').encode();s=sign(m,x);print('Signature:',s,'Valid:',verify(m,s,y),'Tampered:',verify(m+b'!',s,y))
