from random import randint as rand
import time
from rich.console import Console

cns = Console(color_system="auto")

str = ["/","\\","#$+","z","pq","pqr"]
color = ["red","yellow","blue","green"]
while True:
#  clr = color[rand(0, len(color)-1)]
  clr = color[-1]
  chunk = f'{chr(9)*rand(1,4)}{str[rand(0,len(str)-1)]}{chr(9)*rand(0,6)}{str[rand(0,len(str)-1)]}' 
  cns.print(chunk,style="bold green",end="") 
  time.sleep(0.00001)

  