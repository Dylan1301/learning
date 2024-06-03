class Solution:
    def compress(self, chars: List[str]) -> int:
        output = []
        count = 1
        j = 0
        for i in range(1, len(chars)+1):
            previous = chars[i-1]
            if i == len(chars):
                output.append(previous)

                if count >1 :
                    for s in str(count):
                        output.append(s)
                break
    
            current = chars[i]

            if current != previous:
                output.append(previous)

                if count > 1:
                    for s in str(count):
                        output.append(s) 
                
                count = 1
            else:
                count +=1

        for i in output:
            chars[j] = i
            j +=1

        return len(output)



# More optimized

def compress(self, chars: List[str]) -> int:
        count = 1
        i = 0
        j = 0
        while i < len(chars) +1:
            i+=1

            previous = chars[i-1]
            if i == len(chars):
                chars[j] = previous
                j+=1
                if count >1 :
                    for s in str(count):

                        chars[j] = s
                        j +=1
                break
    
            current = chars[i]

            if current != previous:
                chars[j] = previous
                j+=1
                if count > 1:
                    for s in str(count):
                        chars[j] = s
                        j +=1
                
                count = 1
            else:
                count +=1

        return j


# Best solution

class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        count = 1
        for i in range(1,len(chars)+1):
            if i < len(chars) and chars[i] == chars[i-1]:
                count = count + 1
            else:
                chars[index] = chars[i-1]
                index = index + 1
                if count > 1:
                    for d in str(count):
                        chars[index] = str(d)
                        index = index + 1
                count = 1
        return index