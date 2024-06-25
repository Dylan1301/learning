from math import ceil
from collections import deque
def kthGrammar(n: int, k: int) -> int:
    stack = deque()
    cur = k
    while cur > 1:
        stack.appendleft(cur)
        cur = ceil(cur/2)

    print(stack)

    for i in range(len(stack)):
        if stack[i] == 2:
            stack[i] = 1
            continue
        
        if stack[i] %2 == 1:
            if stack[i-1] == 0:
                stack[i] = 0
            else:
                stack[i] = 1
        elif stack[i]%2 == 0:
            if stack[i-1] == 0:
                stack[i] = 1
            else:
                stack[i] = 0

    print(stack)
    if not stack:
        return 0
    
    return stack[-1]


print(kthGrammar(2,4))