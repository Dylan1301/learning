def maxVowels( s: str, k: int) -> int:
        max, current = 0, 0
        vowels = {"a","o", "i", "u", "e"}

        for i in range(0, k):
            if s[i] in vowels:
                current += 1
        
        max = current
        
        for i in range(k, len(s)):
            if (s[i] in vowels) and (s[i -k] not in vowels):
                current +=1
                print(f"{s[i]} is in vowel and {s[i-k]} is not in vowel current += 1 from value {current}")
            elif (s[i] not in vowels) and (s[i-k]  in vowels):
                current -= 1
                print(f"{s[i]} is not in vowel and {s[i-k]} is in vowel current -= 1 from value {current}")
            else:
                 print(f"Both {s[i]} and {s[i-k]} is not in vowels or in vowels")

            if current > max:
                max = current

        return max


s ="abciiidef"
maxVowels(s = s, k = 3)

# This code based on sliding window => We loop through each of the element to compare next element vs previous first element 
# => update the current count based on each elem
