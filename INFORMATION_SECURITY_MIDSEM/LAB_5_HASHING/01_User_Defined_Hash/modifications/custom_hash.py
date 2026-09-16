# MODIFICATION:
# interactive and multiple inputs. This is a student-friendly addition derived from the official exercise; no source listing was supplied.


def lab_hash(text):
 h=5381
 for ch in text:
  h=((h*33)+ord(ch)) & 0xffffffff
  h ^= (h >> 16)
 return h & 0xffffffff
if __name__=='__main__': print(f'{lab_hash(input("Text: ")):08x}')
