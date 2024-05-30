class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max = 0



        for i in range(0, len(flowerbed)):
            if i == 0:
                previous = 0 
            else:
                previous = flowerbed[i-1]

            if i == len(flowerbed)-1:
                next = 0
            else:
                next = flowerbed[i+1]

            if flowerbed[i]==0 and previous==0 and next==0:
                flowerbed[i] = 1
                max +=1
        
        if n <= max:
            return True
        else:
            return False
        


#Good solution:
class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        for i, flower in enumerate(f):
            if flower == 0 and (i==0 or f[i-1]==0) and (i==len(f)-1 or f[i+1]==0):
                f[i]=1
                n -= 1
            if n<=0:
                return True
        return False