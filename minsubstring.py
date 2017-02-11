'''
Given an array with unique characters arr and a string str, find the smallest substring of str containing all characters of arr.

Example:
arr: [x,y,z], str: xyyzyzyx
result: zyx
'''

# start with end pointer to find all the elements in the unique array, 
# slide down start pointer till the the elements are not in the set , measure the length
# if length == arr size return 
# remove the first character 

def findsmallestsubstring(string, array):
  
  if array is None or len(array) == 0 or string is None or len(string) == 0:
    return None
  
  start = 0
  end = 0
  
  arraySet = set(array)
  dc = {}
  minlen = len(string)
  minend = 0
  minstart= 0
  charsSeen = 0
  
  while end < len(string):
    
    while end < len(string):
      c = string[end]
      if c in arraySet:
        count = 0
        if c not in dc or dc[c] == 0 :
          charsSeen +=1
        else:
          count = dc[c]
        dc[c] = count + 1
        
      if charsSeen == len(arraySet):
        break
      end += 1
  
    #end is at a point where all char are present
    while start < end:
      c = string[start]
      if c in dc:
        if dc[c] == 1:
          break
        else:
          dc[c] = dc[c] - 1
      start +=1
    
    #start and end contain the characters 
    strlen = end - start + 1
    if strlen == len(array):
      return string[start : end + 1]
      
    if end - start + 1 < minlen:
      minlen = end - start + 1
      minend = end + 1
      minstart = start
      print(minstart, minend, string[minstart : minend])
    
    #remove the first char from substring
    if start< end:
      c = string[start]
      dc[c] = dc[c] - 1
      
      if end == len(string) and dc[c]  ==  0:
        break
      
      charsSeen -=1
      start += 1
    
    end = end + 1
    