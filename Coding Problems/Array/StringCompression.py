from typing import List

def compress(chars: List[str]) -> int:
        output = []
        count = 1
        for i in range(len(chars)):
            current = chars[i]

            # Check if current char not previous char
            if current != previous or (i == len(chars) -1):
                print("Current ", current, " is different previous: ", previous)
                if count > 1:
                    for char in str(count):
                        output.append(char)
                
                output.append(current)

                previous = current
                count = 1
            else:
                print("just count + 1 for ", previous, " and ", current)
                count +=1
                print(count)

            print(" End loop                   ", i )
        if output != chars:
            chars = output + chars

        print(output)


a= ["a","a","b","b","c","c","c"]

compress(chars=a)