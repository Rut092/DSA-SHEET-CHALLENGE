class Solution:
    def candy(self, ratings: list[int]) -> int:
        l = len(ratings)
        total = i = 1

        while(i<l):
            while(i<l and ratings[i]==ratings[i-1]):
                total+=1
                i+=1
            
            peak = 1
            while(i<l and ratings[i]>ratings[i-1]):
                peak+=1
                total+=peak
                i+=1

            down = 1
            while(i<l and ratings[i]<ratings[i-1]):
                total+=down
                down+=1
                i+=1
            
            if down>peak:
                total+= (down-peak)

        return total