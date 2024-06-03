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

