import njm128 as enc
from colored import fg, bg, attr

def hash(jsont="XOP",key="XOP",locallaw="XOP",mode="XOP",demo=1):

  warn = bg('red_3a') + fg('white')
  noti = bg('yellow_1') + fg('black')
  reset = attr('reset')
  
  ch = [-1,0,1,2]
  ff = [-1,0]
  if jsont=="XOP":
    print(warn + "Warning! Missing 4 Required Fields! (Input, Key, Local, Mode)" + reset)
    return(False)
  elif key=="XOP":
    print(warn + "Warning! Missing 3 Required Fields! (Key, Local, Mode)" + reset)
    return(False)
  elif locallaw=="XOP":
    print(warn + "Warning! Missing 2 Required Fields! (Local, Mode)" + reset)
    return(False)
  elif mode=="XOP":
    print(warn + "Warning! Missing A Required Field! (Mode)" + reset)
    return(False)
  elif "\\" in jsont:
    print(warn + "Warning! Unallowed Character In Input! (Probably \"\\\"!)" + reset)
  elif isinstance(key, int) == False:
    print(warn + "Warning! Unallowed Type in Your Key! (Make Sure It's Not A String!)" + reset)
  elif isinstance(locallaw, int) == False:
    print(warn + "Warning! Unallowed Type in Your Local Law! (Make Sure It's Not A String!)" + reset)
  elif mode not in ch:
    print(noti + "Notice >> Invalid Mode Type! Defaulting To Plaintext..." + reset)
    m = 0
    return(enc.njm128(jsont,key,locallaw,m))  
  elif mode not in ff:
    print(noti + "Notice >> This Type Will Be Supported Soon. Defaulting To Plaintext..." + reset)
    m = 0
    return(enc.njm128(jsont,key,locallaw,m))
  elif demo == 1:
    w = 5
    print("""
Note: This is a demonstration project meant to explain the fundamentals. Set the 5th class operative to '0' to switch to classical usage.
      
NJM supports 4 operatives:
      
1: ASCII in TXT format (Plain)
2: Key Pillar (Exactly Dupes to SHA256)
3: Local Law Temp: 2-8 Digit SECID
4: Output Mode  (-1 = Debug, 0 = Plaintext, 1 = JSON, 2 = XLS)
5: Demo Switch (0 = Off)

  --------------------

Local Law CPU (Per 1000 Clocks):
  2 | 6 MB         | Home Devices
  3 | 55 MB        | Home Devices
  4 | 600 MB       | Home Devices
  5 | 2 GB         | Home Devices
  6 | 17 GB        | Server Network
  7 | 46 GB        | Server Network
  8 | 120 GB       | High Tangibility Processor

Based on your CPU, we recommend a {} digit Local Law.
          
""".format(w))
    return(enc.njm128(jsont,key,locallaw,mode))
  else:
    return(enc.njm128(jsont,key,locallaw,mode))