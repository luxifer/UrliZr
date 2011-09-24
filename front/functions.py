import string
from random import choice

def genUid():
  chars = string.letters + string.digits
  return u''.join(choice(chars) for i in range(8))
