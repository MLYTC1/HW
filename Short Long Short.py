def solution(a, b):
    if len(a)>len(b):
        return b+a+b
    return a+b+a