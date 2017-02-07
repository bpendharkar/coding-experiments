def pramp():
   print "Practice Makes Perfect"

pramp()

sample = [Sample(1440055737,   3,  "enter" ),
          Sample(1440584737,  10,  "exit"  ),
          Sample(1440054737,   9,  "enter" ),
          Sample(1440085737,   2,  "exit"  ),
          Sample(1440084537,   6,  "enter" ),
          Sample(1440084757,  12,  "exit"  )]

#time  => 1  2 3 4 5 6 7 9 
#count => 3  1 7 8 1 -3 -1 2 

class Sample(object):
   def __init__(self, x, y, z ):
     self.time = x
     self.count = y
     self.type = z

   
def findBusiestTime(arr):
  
  if arr is None or len(arr) == 0:
    return None
  
  dc = dict()
  timelist = list()
  arr = sorted(arr, key = lambda x : x.time)
  for x in range(len(arr)):
    sample = arr[x]
      
    if sample.time not in dc:
     dc[sample.time] = 0
     y = 0         
    else:
     y = dc[sample.time]
         
    if sample.type == "enter":
     y += sample.count
    elif sample.type == "exit":
     y =- sample.count
         
    dc[sample.time] = y
      
    timelist.append([sample.time, y])
      
   # { 2453345 : 12 ,  23424354 : 3 , 45353434534: -4}

  sum = 0
  maxsum = 0
  startime = timelist[0][0]
  endtime = None
   
   #time  => 1  2 3 4 5 6 7 9 
   #count => 3  1 7 8 1 -3 -1 2    
   
  for x in range(len(timelist)):
    timestp = timelist[x][0]
    timect = timelist[x][1]
      
    sum += timect
    if sum > maxsum:
     maxsum = sum
     endtime = timestp
    elif sum <= 0:
     starttime = timestp
     endtime = timestp
    
   
  return [ startime, endtime]
      
   
      
   