class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        maxi = i = 0
        b1 = b2 = None
        b1_count = b2_count = 0
        for j in range(len(fruits)):
            if b1==fruits[j]:
                b1_count+=1

            elif b2==fruits[j]:
                b2_count+=1
            elif b1==None:
                b1 = fruits[j]
                b1_count = 1
            elif b2==None:
                b2 = fruits[j]
                b2_count = 1
            else:
                if fruits[j]!=b1 and fruits[j]!=b2:
                    while(b1_count!=0 and b2_count!=0):
                        if fruits[i]==b1:
                            b1_count-=1
                        elif fruits[i]==b2:
                            b2_count-=1
                        i+=1
                    
                    if b1_count==0:
                        b1 = fruits[j]
                        b1_count = 1
                    else:
                        b2 = fruits[j]
                        b2_count = 1
                
            maxi = max(maxi,abs(j-i)+1)
            
        return maxi
