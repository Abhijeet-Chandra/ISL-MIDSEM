# GENERATED BASELINE (ADDITION):
# Derived from the official manual exercise; no source listing was supplied.


import secrets,time
class KeyManager:
 def __init__(self): self.keys={}; self.audit=[]
 def generate(self,name,lifetime=60):
  self.keys[name]={'key':secrets.token_hex(16),'expires':time.time()+lifetime,'revoked':False}; self.audit.append(('generate',name)); return self.keys[name]['key']
 def distribute(self,name):
  r=self.keys[name]
  if r['revoked'] or time.time()>r['expires']: raise PermissionError('Key unavailable')
  self.audit.append(('distribute',name)); return r['key']
 def revoke(self,name): self.keys[name]['revoked']=True; self.audit.append(('revoke',name))
 def renew(self,name,lifetime=60): self.audit.append(('renew',name)); return self.generate(name,lifetime)
if __name__=='__main__':
 k=KeyManager(); print('Generated:',k.generate('Hospital-A')); print('Distributed:',k.distribute('Hospital-A')); k.revoke('Hospital-A'); print('Audit:',k.audit)
