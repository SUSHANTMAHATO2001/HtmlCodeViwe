import os
import time
import sys
import mechanize

##
class color:
        r = '\x1b[;33m'
        g = '\x1b[;32m'

def susan(s):
  for a in s + '\n':
      sys.stdout.write(a)
      sys.stdout.flush()
      time.sleep(1./12)


susan(color.r + "Program By Sushant Mahato")
susan("Devlop By Nepal")
time.sleep(1)
os.system('clear')

b = raw_input("inter the traget url:-")
a = mechanize.urlopen(b)
c = a.read()
print('\n' + color.g + c)
