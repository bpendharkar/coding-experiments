/*
 * Returns true if the input string is a number and false otherwise. 
 * Note that you canNOT use Double.toDouble(), but need to parse the input string character-by-character
 */
 
public boolean isNumber(String toTest)
{
    // implementation here
}

#13423553364675674837435635647547435647  =>  True
#35345363a  => False
#35.3435 => True
#-53633 =>
#-34343-343 => False


#def isNumber(s):

public boolean isNumber(string s)
{
    if(s == null || s.Length == 0)
    {
        return false;
    }
    
    double n = 0;
    int len = s.Length;
    int i = 0;
    int dec = 0


    /*
    
    #35345363a  => False
    #35.3435 => True
    #-53633 =>
    #fssfsdf
    #646464466.
    #456465-.
    
    */
    while(i < len)
    {
        /*
        valid nos, char, -ve, decimals
        */
        char c = s[i];
        if (c == '-')
        {
            if (i != 0)
            {
                return false;
            }        
        }
        else
        {      
             if (c >= '0' && c <= '9')
             {
                  continue;
             }
             else if (c == '.')
             {
                 if (dec == 1)
                 {
                     return false;
                 }
                 else
                 {
                     dec++;
                     continue;
                 }                     
             }
             else
             {
                 return false                         
             }     
        }
        i++;
    }
    
    
    return true;


}



public interface Intervals {
 
    /**
     * Adds an interval [from, to) into an internal structure.
     */
    void addInterval(int from, int to);
 
    /**
     * Returns a total length covered by the added intervals.
     * If several intervals intersect, the intersection should be counted only once.
     * Example:
     *
     * addInterval(3, 6)
     * addInterval(8, 9)
     * addInterval(1, 5)
     *
     * getTotalCoveredLength() -> 6
     *
     * i.e. [1,5) and [3,6) intersect and give a total covered interval [1,6) with a length of 5.
     *      [1,6) and [8,9) don't intersect, so the total covered length is a sum of both intervals, that is 5+1=6.
     *
     *          |__|__|__|                  (3,6)
     *                         |__|         (8,9)
     *    |__|__|__|__|                     (1,5)
     *
     * 0  1  2  3  4  5  6  7  8  9  10
     *
     */
    int getTotalCoveredLength();
 
}


class IntervalImpl(object):
    
    def __init__(self):
        self.lst = list()
    
    #list
    
    def addInterval(self, from, to):
        
        itvl = [from, to]
        self.lst.append(itvl)
        
    
    
    #after 3 calls
    [3,6     8,9    1,5]
    
    
    def getTotalCoveredLength(self):
        
        #sort   = > 1 5     3 6     8 9 
        # n log n 
        self.lst.sort(key = lambda x : (x[0], x[1]))
        
        #merge into a new list
        merged = list()
        merged.append(self.lst[0])   
        #1, 5
        
        i = 1
        # n 
        while i < len(self.lst):
        
            #compare
            current= self.lst[i]   # 8 9 
            last = merged[len(merged) - 1]   # 1 6
             
            if last[1] > current[0]:
                
                start = last[0]
                end = current[1] if current[1] > last[1] else last[1]
                merged.pop()
                merged.append([start, end])
                # 1, 6
            
            else:
                merged.append(current)
            
            i +=1
        
        # 1 6    8 9 
        
        # n
        totallen = 0
        for x in range(len(merged)):            
            curr = merged[x]
            diff = curr[1] - curr[0]
            totallen += diff
            
        
        
        return totallen
        
            
            
            
        
        
        





    