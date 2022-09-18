def solution(l):
    # Your code here
    return sorted(l, key=lambda s: list(map(int, s.split('.'))))