# MODIFICATION:
# time-limited grants. This is a student-friendly addition derived from the official exercise; no source listing was supplied.


import time
ROLE_RIGHTS={'admin':{'read','write','revoke'},'doctor':{'read','write'},'auditor':{'read'}}
def allowed(role,right,expires=float('inf')): return right in ROLE_RIGHTS.get(role,set()) and time.time()<=expires
if __name__=='__main__':
 role=input('Role: '); right=input('Right: '); print('Access granted:',allowed(role,right)); print('Expired grant:',allowed(role,right,time.time()-1))
