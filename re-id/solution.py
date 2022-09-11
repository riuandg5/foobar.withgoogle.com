def solution(i):
    # Your code here
    primes_string = "2"
    primes_arr = [2]
    num = 3
    while (len(primes_string) <= i+5):
        idx = 0
        while (primes_arr[idx]*primes_arr[idx] <= num):
            if (num%primes_arr[idx] == 0):
                num += 2
                idx = 0
            idx += 1
        primes_arr.append(num)
        primes_string += str(num)
        num += 2
    return primes_string[i:i+5]