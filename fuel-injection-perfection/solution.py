import math

def solution(n):
    # Your code here
    n = int(n)
    count = 0
    while (n > 1):
        if (n < 4):
            count += n-1
            break
        if (n % 2 == 0):
            p = math.log(n,2)
            if (p-int(p) == 0):
                count += int(p)
                break
            else:
              n = n//2
        elif (n % 4 == 1):
            n = n - 1
        else:
            n = n + 1
        count += 1
    return count