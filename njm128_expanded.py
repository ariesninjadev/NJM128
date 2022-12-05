import hashlib
from textwrap import wrap

def njm128(jsont,key,locallaw,mode):
  if mode == 0:
    return(a(jsont,key,locallaw))
  elif mode == -1:
    return(b(jsont,key,locallaw))


def a(jsont,key,locallaw):
  r = None
  r = jsont
  for i in range(locallaw):
    r = hashlib.sha256(r.encode()).hexdigest()
  r = list(r)
  for i in range(len(r)):
    r[i] = ord(r[i])
  c = ""
  for j in r: 
    c += str(j)
  c = c[::-1]
  c = wrap(c, 3)
  for k in range(len(c)):
    c[k] = int(c[k])
    c[k] += key
    c[k] = str(c[k])
  c = "".join(c)
  z = ""
  for j in r: 
    c += str(j)
  c = c[::-1]
  c = wrap(c, 3)
  for i in range(len(c)):
    if int(c[i]) <= 254 and int(c[i]) >= 33:
      z += str(chr(int(c[i])))
    else:
      z += str(c[i])
  z = z.replace(' ', '.')
  while len(z) != 128:
    if len(z) >= 129:
      tent = len(z)-128
      z = z[tent:]
    elif len(z) <= 127:
      z = z+z
  z = z.replace(' ', '.')
  return(z)

def b(jsont,key,locallaw):
  r = None
  r = jsont
  for i in range(locallaw):
    r = hashlib.sha256(r.encode()).hexdigest()
  r = list(r)
  print("a: {}".format(r))
  for i in range(len(r)):
    r[i] = ord(r[i])
  print("b: {}".format(r))
  c = ""
  for j in r: 
    c += str(j)
  c = c[::-1]
  print("c: {}".format(c))
  c = wrap(c, 3)
  print("d: {}".format(c))
  for k in range(len(c)):
    c[k] = int(c[k])
    c[k] += key
    c[k] = str(c[k])
  print("e: {}".format(c))
  c = "".join(c)
  print("f: {}".format(c))
  z = ""
  for j in r: 
    c += str(j)
  c = c[::-1]
  c = wrap(c, 3)
  print("g: {}".format(c))
  for i in range(len(c)):
    if int(c[i]) <= 254 and int(c[i]) >= 33:
      z += str(chr(int(c[i])))
    else:
      z += str(c[i])
  print("h: {}".format(z))
  while len(z) != 128:
    if len(z) >= 129:
      tent = len(z)-128
      z = z[tent:]
    elif len(z) <= 127:
      z = z+z
  print("i: {}".format(z))
  z = z.replace(' ', '.')
  return(z)
